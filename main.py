from flask import Flask, render_template, request
from PIL import ImageGrab

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/screenshot", methods=["POST", "GET"]) 
def screenshot():
    if request.method == "POST":
        try:
            data = request.get_json()
            ss_name = data["screenshot_name"]
            screenshot = ImageGrab.grab()
            screenshot.save("{fname}.png".format(fname=ss_name))
            screenshot.close()
            result = "Screenshot with name {fname} created".format(fname=ss_name)
            return result, 201
        except:
            # FIXME: manejar errores adecuadamente
            error = "An error ocurred, please verify the body of your request is correct"
            return error, 500
    elif request.method == "GET": 
        return render_template("screenshot.html")
