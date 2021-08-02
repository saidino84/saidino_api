from flask import Blueprint,render_template,request,redirect,url_for,jsonify
from app.models.image import Image
from app.db import db


image_pb=Blueprint('image_pb',__name__, url_prefix='/images',static_folder='static',template_folder='templates')


@image_pb.route('/',methods=['GET','POST'])
@image_pb.route('/index')
def index():
    pics =Image.query.all()

    if pics:
        all_pics = pics
        if request.method == POST:
             flash('UPLOAD SUCESSFULL !')
             return redirect(url_for('upload'))
        return render_template('index.html',all_pic=all_pics)
    else:
        return render_template('index.html')
