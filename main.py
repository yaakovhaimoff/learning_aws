from flask import Flask, jsonify

app = Flask(__name__)

count = 0

@app.route('/hello', methods=['GET'])
def hello():
    global count
    count += 1
    return jsonify(message=f'Hello from the server!{count}')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
