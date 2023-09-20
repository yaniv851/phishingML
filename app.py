from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf


# Load your Keras model
model = tf.keras.models.load_model("phishing_message_detector")

# Define the FastAPI app
app = FastAPI()

# Define a request input model
class TextRequest(BaseModel):
    text: str

# Define a route to handle text classification requests
@app.post("/classify/")
async def classify_text(req: TextRequest):
    text = req.text

    
    prediction = model.predict([text])

    threshold = 0.5
    result = 1 if prediction[0][0] > threshold else 0

    final_result = "Not a phishing message." if result == 0 else "Phishing message"

    

        

    return {"result": final_result}