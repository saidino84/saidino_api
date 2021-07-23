from flask import Blueprint,render_template,request,redirect,url_for,jsonify
from app.models.admin import User,Comentario
from app.db import db


users_bp=Blueprint('users_bp',__name__, url_prefix='/users_page',static_folder='static',template_folder='templates')


@users_bp.route("/")
def index():
    users=User.query.all()
    # adm="sadino PyProgrammer"
    return render_template('home.html',users=users, users_size=len(users))

@users_bp.route('/add',methods=['POST','GET'])
def add():
    if request.method=='POST':
        print('added')
        form=request.form.to_dict()
        print(form)
        try:
            user=User.from_json(form)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('users_bp.index')), 200
        except Exception as e:
            return jsonify({'Erro aso salval':str(e)})
        else:
            return jsonify({'sucess':'salvado com sucesso'})
    else:
        return render_template('add.html'), 200

@users_bp.route('/comments',methods=['POST','GET'])
def commentarios():
    return render_template(
    'coments.html',commets=Comentario.query.order_by(
    Comentario.id).limit(20).all())

 
