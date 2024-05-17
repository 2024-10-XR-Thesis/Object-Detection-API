from flask import Flask, render_template, request, jsonify
from PIL import ImageGrab

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/screenshot", methods=["POST", "GET"]) 
def screenshot():
    if request.method == "POST":
        data = request.get_json()
        ss_key = "screenshot_name"
        try:
            ss_name = data[ss_key]
            screenshot = ImageGrab.grab()
            screenshot.save("{fname}.png".format(fname=ss_name))
            screenshot.close()
            result = "Screenshot with name '{fname}' created".format(fname=ss_name)
            return result, 201
        except:
            if ss_key not in data:
                error = "The body of your request did not have screennshot_name key, please try again"
                return error, 400
            else:
                error = "Internal server error"
                return error, 500
    elif request.method == "GET": 
        return render_template("screenshot.html")
