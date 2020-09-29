from pymongo import MongoClient
from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/mongo', methods=['POST'])
def mongoTest():
    client = MongoClient('mongodb://localhost27017/')
    db = client.newDatabase
    collection = db.mongoTest
    results = collection.find()
    client.close()
    return render_template('mongo.html', data=results)