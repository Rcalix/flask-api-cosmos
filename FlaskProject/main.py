"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskProject import app
import pydocumentdb
import pymongo
import pydocumentdb.document_client as document_client
try:
    # For c speedups
    from simplejson import loads, dumps, load
except ImportError:
    from json import loads, dumps, load

# try:
uri = "mongodb://mongo-cosmos-testing-1:IgdMkVdf3wHVjww2w8NFmJelEGwjzlgKQfMe4TJGw7jJVN3Au6Aeswjo0HiH6LpeKRVgZ6SwOMuIekE4u9729w==@mongo-cosmos-testing-1.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
client = pymongo.MongoClient(uri)

config = { 
    'ENDPOINT': 'https://cosmos-database-testing-1.documents.azure.com',
    'MASTERKEY': '9lbzHEYDSr150iTr4umujT1woYSFde5SFlkc6udRLkDaPgy6hti2AFhNiF7G6Lfb5EpdcpltyHvyULu2OiUbNw==',
    'DOCUMENTDB_DATABASE': 'store'
}

client = document_client.DocumentClient(config['ENDPOINT'], {'masterKey': config['MASTERKEY']})
db = client.ReadDatabase('dbs/' + config['DOCUMENTDB_DATABASE'])
options = {
    'offerEnableRUPerMinuteThroughput': True,
    'offerVersion': "V2",
    'offerThroughput': 400
}
collection = client.ReadCollection('dbs/' + config['DOCUMENTDB_DATABASE'] +'/colls/' +'cloud')

# except StandardError:
#     print 'fail'

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return "Hello Flask in Azure World"

@app.route('/set')
def setData():
    document1 = client.CreateDocument(collection['_self'],
    { 
        'id': 'server1',
        'Web Site': 0,
        'Cloud Service': 0,
        'Virtual Machine': 0,
        'name': 'some' 
    })
    document2 = client.CreateDocument(collection['_self'],
    { 
        'id': 'server2',
        'Web Site': 1,
        'Cloud Service': 0,
        'Virtual Machine': 0,
        'name': 'some' 
    })
    return "Only set Data"

@app.route('/view')
def viewData():
    query = { 'query': 'SELECT * FROM server s' } 
    options = {} 
    options['enableCrossPartitionQuery'] = True
    options['maxItemCount'] = 2
    result_iterable = client.QueryDocuments(collection['_self'], query, options)
    results = list(result_iterable)
    return dumps(results)