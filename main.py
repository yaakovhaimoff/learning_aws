from flask import Flask, jsonify
from pymongo import MongoClient
# from prometheus_flask_exporter import PrometheusMetrics

app = Flask( __name__ )
# metrics = PrometheusMetrics( app )

#client = MongoClient( "mongodb://mongodb-service:27017" )
client = MongoClient( "mongodb://mongodb-service.default.svc.cluster.local:27017" )
db = client[ "mydatabase" ]
collection = db[ "counter" ]

if collection.count_documents( {} ) == 0:
    collection.insert_one( { "count": 0 } )

@app.route( '/hello', methods=[ 'GET' ] )
def hello():
    counter = collection.find_one( {} )
    count = counter[ "count" ] + 1
    collection.update_one( {}, { "$set": { "count": count } } )
    return jsonify( message=f'Hello from the server and not new ! { count }' )

if __name__ == '__main__':
    app.run( host='0.0.0.0', port=80 )
