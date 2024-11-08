# Creation of APIS using python
# required packages : Flask
# Developed by : Sai  Kumar

#importing the required functions from Flask
from flask import Flask,request,jsonify

#Creating app of Flask 
app = Flask(__name__)

@app.route("/")
def home():
    return "This is Home"
#starting of Main 
if __name__ == "__main__":
    app.run(debug=True)