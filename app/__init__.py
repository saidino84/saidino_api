import cv2 as cv
from flask import Flask, render_template,request,url_for,redirect,jsonify,session,flash
img=cv.Videocam()

def create_app():
    app=Flask('__main__')

    @app.route('/')
    def index():
        return 'Tudo bom'

