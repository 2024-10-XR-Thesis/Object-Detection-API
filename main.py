from flask import Flask, render_template, request
from PIL import ImageGrab
from io import BytesIO
import requests
import json

app = Flask(__name__)

with open("api_key.json", encoding="utf-8") as json_file:
    API_KEY = json.load(json_file)["api_key"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/detect", methods=["POST", "GET"]) 
def detect():
    if request.method == "POST":
        headers = {"Authorization": "Bearer " + API_KEY}
        url = "https://api.edenai.run/v2/image/object_detection"
        data = {
            "providers": "amazon",
            "fallback_providers": "google"
        }
        img = ImageGrab.grab()
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        buffer.seek(0)

        files = {'file': ('screenshot.png', buffer, 'image/png')}
        response = requests.post(url, data=data, files=files, headers=headers)
        result = json.loads(response.text)
        items = result['amazon']['items']
        labels = [i['label'] for i in items]

        return labels, 200
    
    elif request.method == "GET": 
        return render_template("detect.html")