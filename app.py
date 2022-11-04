


import sqlite3
# from turtle import update

# import imp
from flask import Flask, jsonify,render_template,request,redirect,url_for,session
# from flask_restful import Resource, Api
from datetime import datetime
import json,requests,random

app = Flask(__name__)




@app.route('/path')
def path():
    print(app.root_path)
    return app.root_path

@app.route('/')
def home():
    return "Welcome"