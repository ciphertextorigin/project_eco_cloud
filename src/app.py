from flask import Flask, jsonify, request
from favourite_tree import mfTree


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return 'Welcome to My Favourite Tree API'


@app.route('/tree', methods=['GET'])
def get_trees():
    return jsonify({'data': mfTree})  
    


if __name__ == '__main__': 
    app.run()