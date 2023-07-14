import pandas as pd
import sqlite3




#Opening & Reading disease and gene files
disease_df = pd.read_csv("../data/disease_mappings_to_attributes.tsv.gz", sep="\t")
gene_df = pd.read_csv("../data/gene_associations.tsv.gz", sep= "\t")


#print(disease_df.head())


#Connect to database
conn = sqlite3.connect('disease.db')




# Create a cursor
c = conn.cursor()




#Upload disease data file to SQLite
disease_df.to_sql('neurodegen_diseases', conn, if_exists='replace')




# c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='neurodegen_diseases'")
# if c.fetchone() is None:
#     print("The 'neurodegen_diseases' table does not exist.")


# print(conn)


#Drop existing 'n_diseases' & 'other_diseases' table
c.execute("DROP TABLE IF EXISTS n_diseases")
c.execute("DROP TABLE IF EXISTS other_diseases")


#Partitioning tables by 'neurological' disorders
c.execute("CREATE TABLE n_diseases AS SELECT * FROM neurodegen_diseases WHERE diseaseClassNameMSH = 'Nervous System Diseases'")
c.execute("CREATE TABLE other_diseases AS SELECT * FROM neurodegen_diseases WHERE diseaseClassNameMSH <> 'Nervous System Diseases'")


# # View contents of n_diseases
# c.execute("SELECT * FROM n_diseases")
# n_diseases_data = c.fetchall()
# print("n_diseases:")
# for row in n_diseases_data:
#     print(row)


# Read data from 'n_diseases' table into a dataframe
d_df = pd.read_sql_query("SELECT * FROM n_diseases", conn)


#Close connection
conn.close()


#Check if the data from 'n_diseases' succesfully transferred into df
#print(d_df.head())