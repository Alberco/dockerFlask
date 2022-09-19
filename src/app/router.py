from . import app
from flask import jsonify


data = [
    {"game": "COD"}, 
    {"game": "COD"},
    {"game": "COD"}
]

@app.route("/",methods=['GET'])
def index():
    return jsonify({"message":"Docker Example"})

@app.route("/home", methods=['Get'])
def home():
    return jsonify({"data":data})
