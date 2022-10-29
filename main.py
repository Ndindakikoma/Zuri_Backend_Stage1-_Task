'''- Create an **(GET)** api endoint that returns the following  json response:
    
     { "**slackUsername**": String, "**backend**": Boolean, "**age**": Integer, "**bio**": String }
    
    - SlackUsername should be a **string** datatype and your slack username
    - Backend should be a **boolean** datatype
    - Age should be an  **integer** datatype
    - Bio(description about yourself) should be a **string** d'''


from flask import *
from flask import Flask
import json
import time
from pickle import GET
from urllib.parse import uses_query

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
    data_set = {"slackUsername": 'Ndinda Kikoma', "backend": True, "age": 24,
                "bio": 'I\'m a junior software engineer, solving real world problems daily'}
    json_dump = json.dumps(data_set)

    return json_dump


@app.route('/user/', methods=['GET'])
def request_page():
    user_query = str(request.args.get('user'))  # /user/?user=USER_NAME

    data_set = {'Page': 'Request',
                'Message': f'Successfully got the request for {user_query}', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)

    return json_dump


if __name__ == '__main__':
    app.run()
