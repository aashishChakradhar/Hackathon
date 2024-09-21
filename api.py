from fastapi import FastAPI, HTTPException
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

                    # Find the skill with the maximum value
                    max_value = selected_item[skillset].max()  # Find max value across the skillset columns

                    # Find the skill corresponding to the max value
                    mainskill = selected_item[skillset].idxmax()  # This gives the skill name

                    # Set the skill in the selected item
                    selected_item = selected_item.to_dict()  # Convert the pandas Series to a dictionary
                    selected_item['skills'] = mainskill

                    # Check if the mainskill is not 'Presentation designing'
                    if mainskill != 'Presentation designing':
                        singlegroup.append(selected_item)  # Append the dict version
                        dataframes[x] = dataframes[x].drop(dataframes[x].index[item]).reset_index(drop=True)
                else:
                    # If the cluster is exhausted, pick a random item from the original dataset for that cluster
                    resample_item = random.randint(0, len(data[data['cluster'] == int(x[-1])]) - 1)
                    selected_item = data[data['cluster'] == int(x[-1])].iloc[resample_item].to_dict()
                    singlegroup.append(selected_item)

            # Ensure that singlegroup has exactly 4 elements
            while len(singlegroup) < 4:
                # If somehow there are fewer than 4 elements, resample from any existing clusters
                fallback_item = random.randint(0, len(data) - 1)
                fallback_selected = data.iloc[fallback_item].to_dict()
                singlegroup.append(fallback_selected)

            group[y] = singlegroup

        return group

    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Data file not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
