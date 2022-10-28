'''- Create an **(GET)** api endoint that returns the following  json response:
    
     { "**slackUsername**": String, "**backend**": Boolean, "**age**": Integer, "**bio**": String }
    
    - SlackUsername should be a **string** datatype and your slack username
    - Backend should be a **boolean** datatype
    - Age should be an  **integer** datatype
    - Bio(description about yourself) should be a **string** d'''


from flask import *
import json
import time

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
    data_set = {"slackUsername": 'hngi9',
                "backend": True, "age": 24, "bio": 'I am a junior software engineer'}
    json_dump = json.dumps(data_set)
    return json_dump


if __name__ == '__main__':
    app.run(port=4040)
