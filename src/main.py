# main file

import requests
import numpy as np
import pandas as pd
import scipy.sparse as sp
import h5py
from IPython.display import display

path = 'genes_phenes.mat'
f = h5py.File(path, 'r')

# adjacency matrix for gene_gene associations
gene_gene_adj = sp.csc_matrix((np.array(f['GeneGene_Hs']['data']),
    np.array(f['GeneGene_Hs']['ir']), np.array(f['GeneGene_Hs']['jc'])),
    shape=(12331,12331))
gene_gene_adj = gene_gene_adj.tocsr()

# gene features
# TODO: import gene features file and create dataframe
path_gene_feat = 'GeneFeatures.mat'
f_gene_feat = h5py.File(path_gene_feat, 'r')
fgf = f_gene_feat
gene_feat_data = np.transpose(np.array(fgf['GeneFeatures']))
gene_feat_df = pd.DataFrame(gene_feat_data)
display(gene_feat_df)


# adjacency matrix for gene-phenotype associations
name = h5py.h5r.get_name(f['GenePhene'][0][0], f.id)
gda_data = f[name]
gda_adj = sp.csc_matrix((np.array(gda_data['data']), np.array(gda_data['ir']), np.array(gda_data['jc'])), shape=(12331,3215))
gda_adj = gda_adj.tocsr()
# print(gda_adj)

# load the clinical features sparse representation
df = pd.read_csv('clinicalfeatures_tfidf_sparse.csv')
df = df.drop('Unnamed: 0', axis=1)
# print("Disease Feature Vectors: clinical features tfidf sparse matrix representation")
# print("Row corresponds to disease, columns are terms, values = tf-idf of word")
# display(df)

# disease-disease network
dda_adj = sp.csc_matrix((np.array(f['PhenotypeSimilarities']['data']),
    np.array(f['PhenotypeSimilarities']['ir']), np.array(f['PhenotypeSimilarities']['jc'])),
    shape=(3215, 3215))
dda_adj = dda_adj.tocsr()
# print("Disease-Disease Adjacency List from Phenotype Similarities")
# print(dda_adj)

# obtaining phenotype ids
phene_ids = f['pheneIds']
human_name = h5py.h5r.get_name(phene_ids[0][0], f.id)
phene_ids_data = f[human_name]
phene_ids_df = pd.DataFrame(phene_ids_data)
phene_ids_df = phene_ids_df.transpose()

# obtaining gene ids
gene_ids = f['geneIds']
gene_ids_df = pd.DataFrame(gene_ids)
gene_ids_df = gene_ids_df.transpose()




















