from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.translator import translate_to_arabic
from uuid import uuid4

app = FastAPI()

# Define a schema for the request body
class TranslationRequest(BaseModel):
    text: str

# Simulating a database for requests
translation_requests = {}

@app.post("/translate/en2ar")
async def translate_en_to_ar(request: TranslationRequest):
    """
    Translate English text to Arabic.
    """
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Input text cannot be empty")
    try:
        request_id = str(uuid4())  # Generate unique ID for the translation request
        translated_text = translate_to_arabic(request.text)
        
        # Save the request status and result in the simulated "database"
        translation_requests[request_id] = {
            "status": "completed",
            "result": translated_text
        }
        
        return {"request_id": request_id, "translated_text": translated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/translate/en2ar/status/{id}")
async def get_translation_status(id: str):
    """
    Get the status of the translation request.
    """
    if id not in translation_requests:
        raise HTTPException(status_code=404, detail="Request ID not found")
    return translation_requests[id]
