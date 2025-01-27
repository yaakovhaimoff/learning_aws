from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Configure MongoDB connection
client = MongoClient("mongodb://mongo-container:27017/")  # Update with your MongoDB URI if needed
db = client["mydatabase"]
collection = db["counter"]

# Initialize count in MongoDB if it doesn't exist
if collection.count_documents({}) == 0:
    collection.insert_one({"count": 0})

@app.route('/hello', methods=['GET'])
def hello():
    # Retrieve the current count from MongoDB
    counter = collection.find_one({})
    count = counter["count"]

    # Increment the count
    count += 1

    # Update the count in MongoDB
    collection.update_one({}, {"$set": {"count": count}})

    return jsonify(message=f'Hello from the server! {count}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)