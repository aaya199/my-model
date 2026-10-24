from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# Find the project folder
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Load the trained model
MODEL_PATH = PROJECT_ROOT / "model.joblib"
model = joblib.load(MODEL_PATH)

# Create the FastAPI application
app = FastAPI(
    title="Customer Churn Prediction API",
    description="API for predicting customer churn probability",
    version="1.0.0",
)


# Define the expected input data
class Customer(BaseModel):
    tenure_months: int = Field(ge=0)
    monthly_charges: float = Field(ge=0)
    contract: str
    internet_service: str
    support_calls: int = Field(ge=0)


# Health check endpoint
@app.get("/health")
def health():
    return {"status": "healthy"}


# Prediction endpoint
@app.post("/predict")
def predict(customer: Customer):
    try:
        customer_data = pd.DataFrame([customer.model_dump()])

        probability = model.predict_proba(customer_data)[0][1]

        return {
            "churn_probability": round(float(probability), 4)
        }

    except Exception as error:
        raise HTTPException(
            status_code=400,
            detail=f"Prediction failed: {error}",
        ) from error