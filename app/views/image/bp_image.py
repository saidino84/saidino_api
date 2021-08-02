from flask import Blueprint,render_template,request,redirect,url_for,jsonify
from app.models.image import ImageModel
from app.db import db
from werkzeug.utils import secure_filename

from base64 import b64encode
import base64
from io import BytesIO

image_pb=Blueprint('image_pb',__name__, url_prefix='/image_api',static_folder='static',template_folder='templates')




def render_picture(data):
    render_picture =base64.b64encode(data).decode('ascii')
    return render_picture
@image_pb.route('/',methods=['GET','POST'])
@image_pb.route('/index')
def index():
    pics =ImageModel.query.all()
    print('Are at index of images api')
    if pics:
        all_pics = pics
        if request.method == 'POST':
             flash('UPLOAD SUCESSFULL !')
             return redirect(url_for('upload'))
        return render_template('index.html',all_pic=all_pics)
    else:
        return render_template('upload.html')

@image_pb.route('/create',methods=['POST','GET'])
def create():
    return render_template('upload.html')
@image_pb.route('/upload',methods=['POST'])
def upload():
    # pegando os dados digitados do formulario
    print('tryin')
    if 'inputFile' not in request.files:
        flash('No file part ')
        return redirect(request.url)

    file =request.files['inputFile']


    if file.filename =='':
        flash('No selected file')
        return redirect(request.url)
    data =file.read()
    descricao =request.form['descricao']
    #converto em dado para o db entender atraves da fucao que criei
    render_file =render_picture(data)


    filename=request.form['filename']
    if filename ==None or filename=='':
        filename=secure_filename(file.filename)

    new_file=ImageModel(filename=filename,descricao=descricao,rendered_data=render_file,data=data)
    filename=new_file.filename.split('.')[0]
    type=new_file.filename.split('.')[-1]
    description=new_file.descricao
    file_data=new_file.data
    file_render=new_file.rendered_data
    created_at=new_file.created_at
    file_id=new_file.id
    # try:
    print('uploading...')
    db.session.add(new_file)
    db.session.commit()
    print('upload done !')
    # except Exception as err:
    #     return render_template('index.html')
    return render_template(
    'done.html',
        filename=filename,
        file_description=description,
        file_type=type,
        file_id=file_id,
        created=created_at,
        file_render=file_render
        )
