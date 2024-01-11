import torch 
from torch_geometric.nn import GCNConv, SAGEConv, to_hetero

from torch_geometric.utils import negative_sampling
import torch_geometric.transforms as T
from sklearn.metrics import roc_auc_score
from graph_generation import gm, gm_graph
import torch.nn.functional as F

device = torch.device("cpu")

train_data, val_data, test_data = gm[0]


class GNN(torch.nn.Module):
    def __init__(self, hidden_channels, out_channels=0):
        super().__init__()
        self.conv1 = SAGEConv((-1, -1), hidden_channels)
        self.conv2 = SAGEConv((-1, -1), hidden_channels) # out_channels
    
    def forward(self, x, edge_index): #encode
        x = self.conv1(x, edge_index).relu()
        x = self.conv2(x, edge_index)
        return x



class Classifier(torch.nn.Module):
    def forward(self, x_gene, x_disease, edge_label_index): #decode
        edge_feat_gene = x_gene[edge_label_index[0]]
        edge_feat_disease = x_disease[edge_label_index[1]]
        return (edge_feat_gene * edge_feat_disease).sum(dim=-1)

    
class Model(torch.nn.Module):
    def __init__(self, hidden_channels):
        super().__init__()
        self.lin = torch.nn.Linear(20, hidden_channels)
        # create n x e tensors instead of n x f  (embeddings have less features than original node)
        self.gene_emb = torch.nn.Embedding(gm_graph["gene"].num_nodes, hidden_channels) 
        self.disease_emb = torch.nn.Embedding(gm_graph["disease"].num_nodes, hidden_channels)

        self.gnn = GNN(hidden_channels)
        self.gnn = to_hetero(self.gnn, metadata=gm_graph.metadata())

        self.classifier = Classifier()

    def forward(self, data):
        x_dict = {
            "gene": self.gene_emb(data["gene"].node_id),
            "disease": self.disease_emb(data["disease".node_id])
        }

        x_dict = self.gnn(x_dict, data.edge_index_dict)
        pred = self.classifier(
            x_dict["gene"],
            x_dict["disease"],
            data["gene", "gda", "disease"].edge_label_index
        )

        return pred


# model = GNN(hidden_channels=64, out_channels=len(gm_graph.num_node_features))
model = Model(hidden_channels=64)
optimizer = torch.optim.Adam(params=model.parameters(), lr=0.001)
criterion = torch.nn.BCEWithLogitsLoss()



# Training
'''
    define loss and optimizer
    model.train() primes the model to get ready for training
    optimizer.zero_grad() resets the gradients

    - make a prediction of the graph;  decode algorithm ~ makes graph prediction

    - need to use negative edge sampling to compute loss (compare with negative-edge samples with prediction to see if negative-edge samples are found)
    - needs to account for multiple kinds of edges; gene-gene, disease-desease, gene-disease

    - use binary_cross_entripy_with_logits_loss for the loss function
    - loss.backward()
    - optimizer.step()
'''

def train():
    model.train()
    optimizer.zero_grad()
    pred = model(gm_graph)
    loss = criterion(pred, gm_graph["gene", "gda", "disease"].edge_label)
    loss.backward()
    optimizer.step()
    return loss


def test(data):
    model.eval()
