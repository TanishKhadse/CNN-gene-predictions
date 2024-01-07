from flask import Flask, request
from neo4j import GraphDatabase, basic_auth  
from dotenv import load_dotenv
from neomodel import StructuredNode, StringProperty, RelationshipTo, RelationshipFrom, config
import os

load_dotenv()

user = os.getenv("NEO4J_USER")
password = os.getenv("NEO4J_PW")
uri = os.getenv("NEO4J_URI")

app = Flask(__name__)

with GraphDatabase.driver(uri, auth=(user,password)) as driver:
    driver.verify_connectivity()

# driver.run("CREATE (a:Disease) SET a.name=$name RETURN a", name="dummy disease")

# read in graph from model
# post graph to neo4J



# take parameters from frontend (REST)
# use this to query Neo4J to return correct disease/gene and LIMIT num
# return results to frontend, apply attributes to the nodes




# use this file to POST to graph DB based on neural network edge predictions.

@app.route('/bio_data')
def index():
    return {"bio_data": ["bio_data1", "bio_data2", "bio_data3", "bio_data4"]}

if __name__ == "__main__":
    app.run(debug=True)