#ICI ON BUILD NOTRE API
import pandas as pd

#on importe nos model
<<<<<<< HEAD
#from spot_photo.model import load_model ,compute_similarity
=======
from spot-photo....  import #load_model
>>>>>>> 92c31f070f67081df7424ab68ee2af25d2543d47

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# 💡 Preload the model to accelerate the predictions
# We want to avoid loading the heavy deep-learning model from MLflow at each `get("/predict")`
# The trick is to load the model in memory when the uvicorn server starts
# Then to store the model in an `app.state.model` global variable accessible across all routes!
# This will prove very useful for demo days
<<<<<<< HEAD
#app.state.model = load_model()


@app.get('/')
def root():
    return {'greeting': 'Hello',
            'pour faire une recherche': 'tapez : /recherche',
            'avec en param': 'la description de la photo que vous recherchez'}



#@app.get('/recherche')
#def recherche(query : object):
#    model = app.state.model
#    query_embedding = model.encode(query)
#    images_names = compute_similarity(query_embedding)

#    return images_names
=======
app.state.model = #load_model()

@app.get('#Function')
#def function similarity ...
#return show images

@app.get('/')
>>>>>>> 92c31f070f67081df7424ab68ee2af25d2543d47
