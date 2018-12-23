#!/usr/bin/python3
from flask import Flask, render_template, jsonify, request
import pymysql
import configparser
import os
import sys
from middleware import LoggerMiddleware

app = Flask(__name__)
app.config.from_object('config.flask_config.DevelopmentConfig')

if app.config['DEBUG'] == True:
    os.environ['FLASK_ENV'] = app.config['FLASK_ENV']
    os.environ['FLASK_APP'] = app.config['FLASK_APP']
    
app.wsgi_app = LoggerMiddleware(app.wsgi_app)
config = configparser.ConfigParser()
config.read(os.path.join('config', 'dev_config.ini'))

@app.route('/')
def main():   
    return render_template('index.html')

@app.route('/list', methods=['GET'])
def list_results():
    print(request.args.getlist('id[]'))
    db = pymysql.connect(host=config.get('mysql', 'host'),
                         user=config.get('mysql', 'user'),
                         password=config.get('mysql', 'password'),
                         database=config.get('mysql', 'database'))
    cur = db.cursor()
    cur.execute('SELECT * FROM table_1')
    db.close()
    return jsonify(data=cur.fetchall())

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'])