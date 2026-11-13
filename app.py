from fastapi import FastAPI, File, UploadFile, Form
import joblib
import pandas as pd
import tensorflow as tf
from PIL import Image
import io
import numpy as np


app = FastAPI(title="Ne3ma Sequential ML & CV Pipeline API")

ml_model = joblib.load('ml_model.joblib')


interpreter = tf.lite.Interpreter(model_path="Ne3ma_Food_Classifier.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


CV_FOOD_CLASSES = [
    "Baked goods",
    "Dairy products",
    "Fruits",
    "Meat",
    "Prepared meals",
    "Vegetables"
]

#mapping to ML

STORAGE_MAP = {
    'Refrigerated': 0,
    'Room Temperature': 1
}

PRICING_MAP = {
    'High': 0,
    'Low': 1,
    'Moderate': 2
}


FOOD_TYPE_MAP = {
    'Baked Goods': 0,
    'Baked goods': 0,
    'Dairy Products': 1,
    'Dairy products': 1,
    'Fruit': 2,
    'Fruits': 2,
    'Meat': 3,
    'Prepared Meals': 4,
    'Prepared meals': 4,
    'Vegetables': 5
}


TARGET_MAP = {
    0: 'Safe for Consumption (Repake)',
    1: 'Safe for Donation (Food Banks)',
    2: 'Animal Feed Transformation',
    3: 'Biogas'
}

@app.get("/")
def home():
    return {"message": "Ne3ma Sequential API is Live & Running!"}


# Pipeline Endpoint

@app.post("/process-food-waste")
async def process_food_waste(
    file: UploadFile = File(...),           
    storage_conditions: str = Form(...),    
    number_of_guests: int = Form(...),      
    pricing: str = Form(...)                 
):
    try:
       
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        image = image.resize((224, 224))
       
        img_array = np.array(image, dtype=np.float32)
        img_array = np.expand_dims(img_array, axis=0)
        
        interpreter.set_tensor(input_details[0]['index'], img_array)
        interpreter.invoke()
        predictions = interpreter.get_tensor(output_details[0]['index'])
        
        detected_type_of_food = CV_FOOD_CLASSES[np.argmax(predictions[0])]

    
        clean_storage = storage_conditions.strip().title()
        clean_pricing = pricing.strip().title()
        clean_food_type = detected_type_of_food.strip()

    
        encoded_storage = STORAGE_MAP.get(clean_storage, 0)
        encoded_pricing = PRICING_MAP.get(clean_pricing, 0)
        encoded_food_type = FOOD_TYPE_MAP.get(clean_food_type, 0)

      
        input_df = pd.DataFrame([{
            'Storage Conditions': encoded_storage,
            'Number of Guests': number_of_guests,
            'Type of Food': encoded_food_type,
            'Pricing': encoded_pricing
        }])
        
       
        prediction_num = int(ml_model.predict(input_df)[0])
        final_classification = TARGET_MAP.get(prediction_num, f"Class {prediction_num}")
        
        return {
            "status": "success",
            "detected_food_type": clean_food_type,
            "final_decision_code": prediction_num,
            "final_decision_label": final_classification
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }