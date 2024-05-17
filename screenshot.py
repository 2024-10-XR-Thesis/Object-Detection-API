from flask import Flask, render_template, request
from PIL import ImageGrab
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/screenshot", methods=["POST", "GET"])
def screenshot():
    if request.method == "POST":
        data = request.get_json()
        ss_name = data["screenshot_name"]
        screenshot = ImageGrab.grab(bbox=(100, 100, 500, 500)) #FIXME: adjust ss size
        screenshot.save("{fname}.png".format(fname=ss_name))
        screenshot.close()
        result = "Screenshot with name {fname} created".format(fname=ss_name)
        return result, 201
    else:
        return render_template("screenshot.html")



