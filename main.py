# Creation of APIS using python
# required packages : Flask
# Developed by : Sai  Kumar

#importing the required functions from Flask
from flask import Flask,request,jsonify

#Creating app of Flask 
app = Flask(__name__)

#Get Methods
@app.route("/")
def home():
    return "This is Home"

@app.route("/get-student/<student_id>")
def get_student(student_id):
    student ={
        "id":student_id,
        "name" : "sai Kumar",
        "Class" : "Intermediate"
    }
    # if we sent data to api using Query Parameter called Marks then we can use them in like this
    marks = request.args.get("marks")

    if marks:
        student["Marks"]=marks

    return jsonify(student),200

#post Method
@app.route("/create-user",methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data),201

#starting of Main 
if __name__ == "__main__":
    app.run(debug=True)