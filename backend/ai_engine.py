from deepface import DeepFace

def extract_face_vector(image_path: str):
    try:
        embeddings = DeepFace.represent(img_path=image_path, model_name="Facenet", enforce_detection=True)
        return embeddings[0]["embedding"]
    except Exception as e:
        print(f"Face Error: {e}")
        return None