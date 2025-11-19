from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

#Configuration
MODEL_DIR = "Crystlfly/DistilBERT-CyberSec-Detector" 
MAX_LENGTH = 128

#Load Model
print("Loading model...")
try:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_DIR)
    model.eval()
    id2label = model.config.id2label
    print("Model loaded successfully!")
except Exception as e:
    print(f"Failed to load model: {e}")
    raise e

# API Setup
app = FastAPI(title="Cybersecurity Payload Classifier")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PayloadRequest(BaseModel):
    payload: str

@app.post("/analyze")
async def analyze_payload(request: PayloadRequest):
    payload_text = request.payload
    
    inputs = tokenizer(
        payload_text,
        truncation=True,
        padding="max_length",
        max_length=MAX_LENGTH,
        return_tensors="pt"
    )

    with torch.no_grad():
        outputs = model(**inputs)

    probabilities = torch.softmax(outputs.logits, dim=-1)
    confidence, predicted_class_id = torch.max(probabilities, dim=-1)
    confidence_score = confidence.item()
    predicted_label = id2label[predicted_class_id.item()]

    status = "malicious"
    if predicted_label == "benign":
        status = "safe"
    elif confidence_score < 0.60:
        status = "review_required"

    return {
        "payload": payload_text,
        "prediction": predicted_label,
        "confidence": round(confidence_score, 4),
        "status": status
    }

@app.get("/")
def health_check():
    return {"status": "Model is running"}