import pandas as pd
import sqlite3


#Opening & Reading disease and gene files
disease_df = pd.read_csv("../data/disease_mappings_to_attributes.tsv.gz", sep="\t")
gene_df = pd.read_csv("../data/gene_associations.tsv.gz", sep= "\t")

print(disease_df.head())

#Connect to database
conn = sqlite3.connect('disease.db')


# Create a cursor
c = conn.cursor()


#Upload disease data file to SQLite
disease_df.to_sql('neurodegen_diseases', conn, if_exists='replace')


#Close connection
conn.close()
