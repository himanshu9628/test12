


import sqlite3
# from turtle import update

# import imp
from flask import Flask, jsonify,render_template,request,redirect,url_for,session,send_file
# from flask_restful import Resource, Api
from datetime import datetime
import json,requests,random

app = Flask(__name__)




@app.route('/path')
def path():
    print(app.root_path)
    return app.root_path

@app.route('/download')
def downloadFile ():
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = app.root_path+"/project1.db"
    return send_file(path, as_attachment=True)


@app.route('/')
def home():
    return "Welcome"




if __name__ == '__main__':
  
    app.run(debug = True)
