### Predicting Gene Mutations Using Convolutional Neural Networks for Neurodegenerative Diseases

Python, PyTorch, PyTorch Geometric, Node.js, React.js, Tailwind, Neo4J
Node.js version 8.11.0 and above

### About
Currently, humanity holds lots of data that demonstrate which genes can cause certain Neuodegenerative Diseases to occur. However, there is still lots about Gene-Gene interactions that have not been explored yet. Gene-Disease associations can be modelled graphically, which formed the basis of this project. 

We employed a Heterogenous Graphical Neural Network (GraphSAGE) with processes for Encoding and Decoding to assist with our link-prediction task; after assembling Gene-Disease data into graphical form, we ran this massive data through our GNN to output justified edge-predictions.

All Gene-Disease-Association data is displayed on the frontend network after the user inputs the disease of interest and number of genes to include in the network. 

### Setup
Set up ```.env``` file in the root directory with the following contents:
```
OMIM_API_key=
NEO4J_USERNAME=
NEO4J_PASSWORD=
NEO4J_URI=
```

### Install Python dependencies (from root directory):

Set up virtual environment:
```
cd src
```

For Mac
```
# make venv
python3 -m venv venv

# activate venv
source venv/bin/activate
```

For Windows
```
# make venv
python -m venv venv

# activate venv
.\venv\Scripts\activate
```


Install dependencies
```
pip3 install -r requirements.txt
```

SSL certificate: Install Certificates.command


To Run Python files
Make sure you are in the ```src``` directory, then you can run the files. 

### To run frontend (from root directory):
```
cd app
npm i
npm start
```

### Run backend:
```
cd src
// activate venv
python3 app.py
```
