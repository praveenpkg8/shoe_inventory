import json
import redis

from flask import Flask

app = Flask(__name__)
r = redis.Redis(port=6379)
r.set('foo', 'bar')


@app.route('/', methods=['GET'])
def welcome():
    message = {
        "hello": "world",
        "redis": r.get('foo').decode("utf-8")
    }
    return json.dumps(message), 200


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
