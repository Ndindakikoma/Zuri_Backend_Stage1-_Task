'''- Create an **(GET)** api endoint that returns the following  json response:
    
     { "**slackUsername**": String, "**backend**": Boolean, "**age**": Integer, "**bio**": String }
    
    - SlackUsername should be a **string** datatype and your slack username
    - Backend should be a **boolean** datatype
    - Age should be an  **integer** datatype
    - Bio(description about yourself) should be a **string** d'''


from flask import Flask
import json

app = Flask(__name__)


@app.route('/user/', methods=['GET'])
def home_page():
    data_set = {"slackUsername": 'Ndinda Kikoma',
                "backend": True, "age": 24, "bio": 'I am a junior software engineer currently enrolled in Zuri intership'}
    json_dump = json.dumps(data_set)
    return json_dump
