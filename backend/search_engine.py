import os
import requests

def reverse_image_search(image_path: str, imgbb_key: str, serpapi_key: str):
    # 1. Upload to ImgBB
    with open(image_path, "rb") as file:
        res = requests.post("https://api.imgbb.com/1/upload", data={"key": imgbb_key}, files={"image": file}).json()
        if not res.get("success"): return None
        img_url = res["data"]["url"]

    # 2. Search via Google Lens / SerpApi
    data = requests.get("https://serpapi.com/search.json", params={"engine": "google_lens", "url": img_url, "api_key": serpapi_key}).json()
    matches = data.get("visual_matches", [])
    
    for item in matches:
        link = item.get("link", "")
        if any(domain in link for domain in ["linkedin.com", "twitter.com", "instagram.com", "github.com"]):
            return {"title": item.get("title"), "link": link}
    
    return {"title": matches[0].get("title"), "link": matches[0].get("link")} if matches else None