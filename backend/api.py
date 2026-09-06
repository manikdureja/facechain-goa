import os
from fastapi import FastAPI, UploadFile, File
from dotenv import load_dotenv
import shutil

from ai_engine import extract_face_vector
from search_engine import reverse_image_search
from blockchain import anchor_identity

load_dotenv()
app = FastAPI()

# Retrieve keys from backend/.env
IMGBB_KEY = os.getenv("IMGBB_API_KEY")
SERPAPI_KEY = os.getenv("SERPAPI_KEY")
RPC_URL = os.getenv("WEB3_RPC_URL")
PRIV_KEY = os.getenv("PRIVATE_KEY")
CONTRACT_ADDR = os.getenv("CONTRACT_ADDRESS") # Address from Hardhat deployment

@app.post("/verify-face")
async def verify_and_anchor_face(file: UploadFile = File(...)):
    # 1. Save uploaded image temporarily
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    try:
        # 2. Extract Biometrics
        vector = extract_face_vector(temp_path)
        if not vector: return {"error": "No face detected."}
        
        # 3. Open Web Search
        match = reverse_image_search(temp_path, IMGBB_KEY, SERPAPI_KEY)
        if not match: return {"error": "No social media match found on the web."}
        
        # 4. Smart Contract Execution
        tx_hash = anchor_identity(match["link"], vector, RPC_URL, PRIV_KEY, CONTRACT_ADDR)
        
        return {
            "status": "success",
            "social_identity": match["link"],
            "blockchain_receipt": tx_hash,
            "message": "Identity successfully verified and anchored to Sepolia."
        }
    finally:
        os.remove(temp_path)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)