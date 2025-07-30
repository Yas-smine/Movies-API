import requests  # Imports the requests library for sending HTTP requests
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("OMDB_API_KEY")

# Base URL for the OMDb API
url = "https://www.omdbapi.com/" # Base URL for the OMDb API


def get_movie_data(title):
    # Packs the query parameters into a dictionary
    params = {"apikey": api_key,"s": title, 'plot': 'full'}

    # Sends a GET request with the parameters
    response = requests.get(url, params=params)

    # Checks if the HTTP request was successful
    if response.status_code == 200:
        if "Search" in response.json(): # Parses the JSON and checks if movie results are present
            results = response.json()["Search"] # Returns the list of movies
            return results
        else:
            print("No movies found.") # Informs the user if no movies matched the search
            return []
    else:  # Handles failed HTTP request
        print(f"Error: {response.status_code}")
        return []
    
def build_dataframe(results):
   
# Creating the DataFrame
# Simple conversion: each movie dictionary becomes a row in the DataFrame
    movies_df = pd.DataFrame(results) 
    return movies_df
