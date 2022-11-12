from flask import Flask, render_template, request

# __name__ => refers to the name of the current file 
# this line thells python; hey python turn this file into a flask application
app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name")
    return render_template("index.html", name=name)
