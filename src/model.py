import torch 
from torch_geometric.nn import GCNConv, SAGEConv, to_hetero
from torch_geometric.nn import GCNConv
from torch_geometric.utils import negative_sampling
import torch_geometric.transforms as T
from sklearn.metrics import roc_auc_score
from graph_generation import gm, gm_graph


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