import pandas as pd
import sqlite3


#Opening & Reading disease and gene files
disease_df = pd.read_csv(r"C:\\Users\snand\Documents\\CS Projects\\CNN-gene-predictions\disease_mappings_to_attributes.tsv.gz", sep="\t")
gene_df = pd.read_csv(r"C:\\Users\snand\Documents\\CS Projects\\CNN-gene-predictions\\gene_associations.tsv.gz", sep= "\t")


#Connect to database
conn = sqlite3.connect('disease.db')


# Create a cursor
c = conn.cursor()


#Upload disease data file to SQLite
disease_df.to_sql('neurodegen_diseases', conn, if_exists='replace')


#Close connection
conn.close()
