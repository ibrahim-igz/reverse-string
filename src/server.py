import json
import flask
from flask import Flask
server = Flask(__name__)

@server.route("/", methods=['POST'])
def hello():

  input_1 = json.loads(flask.request.data.decode('utf-8'))['input1']
  # input_2 = json.loads(flask.request.data.decode('utf-8'))['input2']
  # output = input_1 + input_2
 

  return input_1[::-1]

if __name__ == "__main__":
  server.run(host='0.0.0.0', debug=True)