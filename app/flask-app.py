from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://mongodb:27017/")
db = client["testdb"]
collection = db["items"]

@app.route("/", methods=["GET"])
def start_page():
    collection.insert_one({"msg": "Hello from MongoDB"})
    doc = collection.find_one(sort=[('_id', -1)])
    return jsonify({"message": doc["msg"]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
