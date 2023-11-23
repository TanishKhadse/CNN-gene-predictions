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

@app.route('/')
def index():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)