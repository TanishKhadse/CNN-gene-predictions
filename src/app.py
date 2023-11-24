from flask import Flask, request
from neo4j import GraphDatabase, basic_auth  
from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv("NEO4J_USER")
password = os.getenv("NEO4J_PW")
uri = os.getenv("NEO4J_URI")

app = Flask(__name__)
db = GraphDatabase.driver(uri, auth=(user, password))


# use this file to POST to graph DB based on neural network edge predictions.

@app.route('/bio_data')
def index():
    return {"bio_data": ["bio_data1", "bio_data2", "bio_data3"]}

if __name__ == "__main__":
    app.run(debug=True)