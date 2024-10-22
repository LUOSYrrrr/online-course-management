from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

MONGO_URI = "mongodb+srv://luosylois:HDQNHKbMDrxhLJz1@online-course.4tn3g.mongodb.net/"
client = MongoClient(MONGO_URI)
db = client["online_course"]

@app.route("/courses", methods=["GET"])
def get_courses():
    courses = list(db["courses"].find({}, {"_id": 0}))
    return jsonify(courses)

@app.route("/courses", methods=["POST"])
def add_course():
    data = request.json
    db["courses"].insert_one(data)
    return jsonify({"message": "Course added successfully!"}), 201

if __name__ == "__main__":
    app.run(debug=True)
