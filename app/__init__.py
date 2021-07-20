import cv2 as cv
from flask import Flask, render_template,request,url_for,redirect,jsonify,session,flash

def create_app():
    app=Flask(__name__)
    app.add_url_rule('/', view_func=index)
    return app

def index():
        return 'Tudo bom'
