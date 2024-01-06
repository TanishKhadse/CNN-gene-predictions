import torch 
from torch_geometric.nn import GCNConv, SAGEConv, to_hetero
from torch_geometric.utils import negative_sampling
import torch_geometric.transforms as T
from sklearn.metrics import roc_auc_score
from torch_geometric.data import InMemoryDataset
from torch_geometric.utils.convert import to_networkx
from torch_geometric.transforms import ToUndirected
import torch_geometric.data as dt

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import h5py

import scipy.sparse as sp

# Build dataset

# Load data from .mat files
gf_data = h5py.File("../data/GeneFeatures.mat", 'r')
gp_data= h5py.File("../data/genes_phenes.mat", 'r')
cf_data = h5py.File("../data/clinicalfeatures_tfidf.mat", 'r')

gene_ids = gp_data["geneIds"]
phene_ids = gp_data["pheneIds"]

gene_network_adj = sp.csc_matrix((np.array(gp_data['GeneGene_Hs']['data']),
    np.array(gp_data['GeneGene_Hs']['ir']), np.array(gp_data['GeneGene_Hs']['jc'])),
    shape=(12331,12331)).tocoo()

disease_network_adj = sp.csc_matrix((np.array(gp_data['PhenotypeSimilarities']['data']),
    np.array(gp_data['PhenotypeSimilarities']['ir']), np.array(gp_data['PhenotypeSimilarities']['jc'])),
    shape=(3215, 3215)).tocoo()

dg_ref = gp_data['GenePhene'][0][0]
gene_disease_adj = sp.csc_matrix((np.array(gp_data[dg_ref]['data']),
    np.array(gp_data[dg_ref]['ir']), np.array(gp_data[dg_ref]['jc'])),
    shape=(12331, 3215)).tocoo()


# load up Gene Features into a tensor
gene_nodes = torch.tensor(gf_data["GeneFeatures"][:]).T
disease_nodes = torch.tensor(cf_data["F"][:]).T

gene_rows = gene_network_adj.row
gene_cols = gene_network_adj.col
gene_data = gene_network_adj.data

disease_rows = disease_network_adj.row
disease_cols = disease_network_adj.col
disease_data = disease_network_adj.data

gene_disease_rows = gene_disease_adj.row
gene_disease_cols =  gene_disease_adj.col
gene_disease_data = gene_disease_adj.data



gm_graph = dt.HeteroData()
gm_graph["gene"].x = gene_nodes

gm_graph["gene", "gene_gene", "gene"].edge_index = torch.tensor([gene_rows, gene_cols])
gm_graph["gene", "gene_gene", "gene"].edge_attr = torch.tensor(gene_data)

gm_graph["disease"].x = disease_nodes
gm_graph["disease", "dis_dis", "disease"].edge_index = torch.tensor([disease_rows, disease_cols])
gm_graph["disease", "dis_dis", "disease"].edge_attr = torch.tensor(disease_data)

gm_graph["gene", "gda", "disease"].edge_index = torch.tensor([gene_disease_rows, gene_disease_cols])
gm_graph["gene", "gda", "disease"].edge_attr = torch.tensor(gene_disease_data)

gene_mutations = [gm_graph]



class GeneMutations(InMemoryDataset):
    def __init__(self, root, transform=None, pre_transform=None, data_list=None):
        super(GeneMutations, self).__init__(root, transform, pre_transform)
        self.data, self.slices = self.collate(data_list)


transform = T.Compose([
        T.ToUndirected(),
        T.RandomLinkSplit(
            num_val=0.05,
            num_test=0.1,
            is_undirected=True,
            neg_sampling_ratio=2.0,
            edge_types=gm_graph.edge_types,
            # rev_edge_types=("disease", "gda", "gene"),
            add_negative_train_samples=False
        )
    ]
)


gm = GeneMutations(".", transform=transform, data_list=gene_mutations)
train_data, val_data, test_data = gm[0]