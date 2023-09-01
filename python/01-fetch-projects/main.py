from flask import Flask, jsonify
from resemble import Resemble
Resemble.api_key('YOUR_API_TOKEN')


app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "pong"})

@app.route('/projects', methods=['GET'])
def project():
    page = 1
    page_size = 10
      
    response = Resemble.v2.projects.all(page, page_size)
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
