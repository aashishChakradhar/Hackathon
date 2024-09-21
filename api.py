from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, conlist
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
from sklearn.cluster import KMeans
import random

app = FastAPI()

# Adding CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.post('/predict')
def predict():
    try:
        # Read the dataset
        data = pd.read_csv('Data/data.csv')

        # Define the skillset for clustering
        skillset = ['Coding', 'Leadership', 'Communication Skill', 'Presentation designing']

        # Ensure the required columns exist in the data
        if not all(skill in data.columns for skill in skillset):
            raise HTTPException(status_code=400, detail="Required columns missing from dataset")

        # Apply KMeans clustering
        kmeans = KMeans(n_clusters=4, random_state=42)
        kmeans.fit(data[skillset])
        data['cluster'] = kmeans.labels_

        # Create separate dataframes for each cluster
        dataframes = {f'data_{x}': data[data['cluster'] == x] for x in data['cluster'].unique()}

        # Find the smallest dataset
        smallest_dataset_name = min(dataframes, key=lambda k: len(dataframes[k]))
        minvalue = len(dataframes[smallest_dataset_name])

        # Assuming you have a list of DataFrames
        dataframes = [data[data['cluster'] == x] for x in data['cluster'].unique()]# List of your DataFrames

        print(dataframes)

        # Initialize an empty list to store the groups
        groups = []

        # Create a list of iterators for each DataFrame
        dataframe_iters = [df.iterrows() for df in dataframes]
        while True:
            group = []
            
            # Continue to fill the group until it has 4 elements
            while len(group) < 4:
                all_empty = True  # To track if all iterators are exhausted
                
                for _, dataframe_iter in enumerate(dataframe_iters):
                    try:
                        # Try to get the next element from the current DataFrame iterator
                        index, element = next(dataframe_iter)
                        group.append(element)
                        all_empty = False  # Mark as not empty if at least one DataFrame has data
                        if len(group) == 4:
                            break  # Stop once we have 4 elements
                    except StopIteration:
                        # This DataFrame is exhausted, continue to the next
                        continue
                
                if all_empty:
                    # If all DataFrames are exhausted and no more elements are found, stop
                    break

            # Add the group to the list of groups if it has 4 elements
            if len(group) == 4:
                groups.append(group)
            else:
                # Break if we can't form any more full groups of 4
                break
        
        return groups
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Data file not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))