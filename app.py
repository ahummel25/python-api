#!/usr/bin/python3
from flask import Flask, render_template, jsonify, request
import pymysql
import configparser
import os

app = Flask(__name__)
config = configparser.ConfigParser()
config.read(os.path.join('config', 'dev_config.ini'))

@app.route('/')
def main():   
    return render_template('index.html')

@app.route('/list', methods=['GET'])
def list_results():
    print(request.args.get('id'))
    db = pymysql.connect(host=config.get('mysql', 'host'),
                         user=config.get('mysql', 'user'),
                         password=config.get('mysql', 'password'),
                         database=config.get('mysql', 'database'))
    cur = db.cursor()
    cur.execute('SELECT * FROM table_1')
    db.close()
    return jsonify(data=cur.fetchall())

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=80)