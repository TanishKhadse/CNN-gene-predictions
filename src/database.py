import pandas as pd
import sqlite3
import numpy as np
import h5py as hp
import os 
from api import OMIM_key
from api import get_disease_name

#Opening & Reading disease files
parent = os.path.dirname(os.getcwd())
phene_id_filename = os.path.join(parent, os.path.join('data','phene_ids_df.csv'))
disease_id_df = pd.read_csv(phene_id_filename)

#Opening & Reading gene files
gene_id_filename = os.path.join(parent, os.path.join('data', 'gene_ids_df.csv'))
gene_id_df = pd.read_csv(gene_id_filename)

#Cleaning unneeded data
disease_id_df = disease_id_df.drop([0,1])

# print(disease_id_df.head())

# Connect to the database
conn = sqlite3.connect('disease.db')


# Create a cursor
c = conn.cursor()

# Drop existing 'allDiseases_ids' table if it exists
c.execute("DROP TABLE IF EXISTS allDiseases")
c.execute("DROP TABLE IF EXISTS diseases")

# Create new table 'allDiseases' with column 'disease_id'
c.execute("CREATE TABLE allDiseases (disease_id INT)")

# Create new table 'allGenes' with column 'gene_id'
# c.execute("CREATE TABLE allGenes (gene_id INT)")

# Upload disease data from 'disease_id_df' into 'allDiseases' table
disease_id_df.to_sql('allDiseases', conn, if_exists='replace')

#Upload gene data from 'gene_id_df' into 'allGenes' table
gene_id_df.to_sql('allGenes', conn, if_exists='replace')

c.execute("ALTER TABLE allDiseases RENAME COLUMN '0' TO 'disease_id'")
c.execute("ALTER TABLE allGenes RENAME COLUMN '0' TO 'gene_id'")

# count = c.execute("SELECT COUNT(*) as count_diseases FROM allDiseases")
# print(count)

c.execute("ALTER TABLE allDiseases ADD disease_name TEXT")
c.execute("ALTER TABLE allGenes ADD gene_name TEXT")

# print(disease_id_df.head())
query = "UPDATE allDiseases SET disease_name = ? WHERE disease_id = ?"

# for index in disease_id_df['0']:
#     str_i = str(index)
#     int_i = int(index)
#     dis_name = get_disease_name(int_i)
#     c.execute(query, (dis_name, str_i))
    
# Commit the changes
conn.commit()
    

# c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='neurodegen_diseases'")
# if c.fetchone() is None:
#     print("The 'neurodegen_diseases' table does not exist.")


# print(conn)


# #Drop existing 'n_diseases' & 'other_diseases' table
# c.execute("DROP TABLE IF EXISTS n_diseases")
# c.execute("DROP TABLE IF EXISTS other_diseases")


# #Partitioning tables by 'neurological' disorders
# c.execute("CREATE TABLE n_diseases AS SELECT * FROM neurodegen_diseases WHERE diseaseClassNameMSH = 'Nervous System Diseases'")
# c.execute("CREATE TABLE other_diseases AS SELECT * FROM neurodegen_diseases WHERE diseaseClassNameMSH <> 'Nervous System Diseases'")


# # View contents of n_diseases
# c.execute("SELECT * FROM n_diseases")
# n_diseases_data = c.fetchall()
# print("n_diseases:")
# for row in n_diseases_data:
#     print(row)


# # Read data from 'n_diseases' table into a dataframe
# d_df = pd.read_sql_query("SELECT * FROM n_diseases", conn)


#Close connection
conn.close()



