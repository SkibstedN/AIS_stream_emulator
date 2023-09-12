from flask import Flask, request

app = Flask(__name__)

import time

@app.route('/', methods=['POST'])
def index():
    start_time = time.time()
    content = request.json
    print(f"Received: {content}")
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")
    return 'OK', 200

if __name__ == '__main__':
    app.run(port=5000)
