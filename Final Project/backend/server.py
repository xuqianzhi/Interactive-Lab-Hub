from flask import Flask, jsonify, Response
import time
import random
import threading

app = Flask(__name__)

@app.route('/humidity')
def humidity():

    data = random.uniform(0, 1)

    def long_running_get_data(**kwargs):
        your_params = kwargs.get('post_data', {})

    thread = threading.Thread(target=long_running_get_data, kwargs={
                    'post_data': data})
    thread.start()
    response = jsonify({"humidity": data})
    response.headers.add('Access-Control-Allow-Origin', '*') 
    return response

if __name__ == "__main__":
    # app.run(host="<Your PI IP address here>", port=4000)
