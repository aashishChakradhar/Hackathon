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

        # Group creation
        group = {}
        for y in range(minvalue):
            singlegroup = []
            for x in dataframes.keys():
                if len(dataframes[x]) > 0:
                    item = random.randint(0, len(dataframes[x]) - 1)
                    
                    selected_item = dataframes[x].iloc[item]
                    
                    # Assign a random skill from the skills_data list
                    # max_value = max([selected_item[skill] for skill in skillset])

                    # mainskill = ''
                    # for skill in skillset:
                    #     if max_value == int(selected_item[skill]):
                    #         mainskill = skill
                    #         break

                    # # Set the skill in the selected item
                    # selected_item['skills'] = mainskill
                    
                    # # Check if the mainskill is not 'Presentation designing'
                    # if mainskill != 'Presentation designing':
                    #     singlegroup.append(selected_item.to_dict())  # Convert to dict
                    #     dataframes[x] = dataframes[x].drop(dataframes[x].index[item]).reset_index(drop=True)

                    singlegroup.append(selected_item)
                    dataframes[x] = dataframes[x].drop(dataframes[x].index[item])
                else:
                    singlegroup.append(None)  # Use None instead of 0 for clarity

            group[y] = singlegroup

        return group

    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Data file not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))