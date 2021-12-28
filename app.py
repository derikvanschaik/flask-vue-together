from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

# this just redirects on initial load of app 
@app.route("/")
def index():
    return redirect(url_for("increment", flask_count=0))   

@app.route("/<flask_count>")  
def increment(flask_count=None):   
        return render_template('index.html',flask_count = int(flask_count ))         

