from flask import Flask, request, jsonify
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


def create_disease_node(tx, name):
    query = (
        "CREATE (n:Disease {name: $name})"
        "RETURN n"
    )
    result = tx.run(query, name=name)

    return [{"id": record['n'].id} for record in result]


def query_nodes(name, num):
    query = (
        """MATCH (d:Disease {name: $name})-[gda]->(g:Gene)
        RETURN g
        LIMIT $num"""
    )

    records, summary, keys = driver.execute_query(query, name=name, num=num)
    return records, summary, keys


def serialize_node(node):
    return {"id": node.id, "name": node.name}
# use this file to POST to graph DB based on neural network edge predictions.



# @app.route('/data')
# def index():

#     return {"bio_data": ["bio_data1", "bio_data2", "bio_data3", "bio_data4"],
#             "graph_data": ["AIDS", "HIV"]}



@app.route('/graph', methods=["POST"])
def get_input_params():
    data = request.get_json()
    print(data)
    # return jsonify(data)
    try: 
        disease_name = data["disease_name"].lower().strip()
        num_nodes = int(data["num_nodes"])

        records, summary, keys = query_nodes(disease_name, num=num_nodes)
        print(summary.query)
        print(records)
        # with driver.session() as session:
        #     result = session.execute_write(create_disease_node, data["disease_name"].lower().strip())
        #     print(result)
        #     return jsonify(result)

        nodes = [{"name": disease_name}]
        for r in records:
            nodes.append({r.name})

        # # print("Query worked: " + nodes)
        return jsonify(nodes)

            
    except Exception as e:
        return jsonify({"Error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)