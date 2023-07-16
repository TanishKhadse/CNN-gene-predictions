### Predicting Gene Mutations Using Convolutional Neural Networks for Neurodegenerative Diseases

Python, Tensorflow, Scikit-learn, Node.js, React.js, Bootstrap, C++,
Node.js version 8.11.0 and above

### About


### Setup
Set up ```.env``` file in the root directory with the following contents:
```
API_USER=
API_PW=
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

### Run C++:
```
cd graphs
make; ./bin/exec
```

### To run frontend (from root directory):
```
cd app
npm i
npm start
```
