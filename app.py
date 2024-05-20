from flask import Flask, render_template, request
from PIL import ImageGrab
import requests
import json
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/detect", methods=["POST", "GET"]) 
def detetc():
    if request.method == "POST":
        data = request.get_json()
        ss_key = "screenshot_name"
        try:
            ss_name = data[ss_key]
            screenshot = ImageGrab.grab()
            ss_full_name = "{fname}.png".format(fname=ss_name)
            screenshot.save(ss_full_name)
            screenshot.close()

            headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZjg4ZWMyNDUtOGNhMi00MGE2LWE4NzEtMWM5ZmU0ZmE5YWNlIiwidHlwZSI6ImFwaV90b2tlbiJ9.BV9MP-DFCnUdMlrkkN9E-nWR_ThUmTlI11-eBlguDRM"}
            url = "https://api.edenai.run/v2/image/object_detection"
            data = {
                "providers": "amazon",
                "fallback_providers": "google"
            }
            files = {'file': open(ss_full_name, 'rb')}

            response = requests.post(url, data=data, files=files, headers=headers)
            result = json.loads(response.text)
            items = result['amazon']['items']
            labels = [i['label'] for i in items]

            os.remove(ss_full_name)

            return labels, 200
        except:
            if ss_key not in data:
                error = "The body of your request did not have screennshot_name key, please try again"
                return error, 400
    elif request.method == "GET": 
        return render_template("detect.html")
