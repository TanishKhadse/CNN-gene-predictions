import requests as req
from dotenv import load_dotenv
import os

# Set up the API request URL
base_url = 'https://api.omim.org/api'
load_dotenv()
OMIM_key=os.getenv('OMIM_API_key')
mim_number = 0 

# Go to api link
def get_url(mim):
  return f'{base_url}/entry?mimNumber={mim}&apiKey={OMIM_key}&format=json'

# Construct the full API request URL
def get_disease_name(mim):
    
    response = req.get(get_url(mim))
    
    # Successful response
    if response.status_code == 200:
        #Finding the name of the disease
        data = response.json()
        disease_name = ""
        if len(data['omim']['entryList']) > 0:  
          disease_name = data['omim']['entryList'][0]['entry']['titles']['preferredTitle']
        
        return disease_name
    #bad response
    else:
        print(f"Error accessing OMIM API. Status code: {response.status_code}")
        return None

# print(get_disease_name(101200))
