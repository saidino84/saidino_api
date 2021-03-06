from flask import Flask, jsonify, request, url_for, render_template,Response
# from flask_migrate import Migrate
import time
import os
import random
from modulos import get_current_directory
from flask_migrate import Migrate

from flask_admin import Admin, BaseView,expose
from flask_admin.contrib.sqla import ModelView
# from flask.ext.admin import Admin
# from app.admin import config_admin,AdminView
from app.db.database import json_dbs,json_mercearia



appUrls = 'https://flaskchatbotmoz.herokuapp.com'


def create_app():
    app = Flask(__name__)
    'DEPRECATED USING SQLITE MIGRATE TO POSTGRL'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    #     os.path.join(os.path.dirname(__file__), 'dados.db')
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['SQLALCHEMY_DATABASE_URI']='postgresql://rlvawhxyajskth:1ae752d1119605d1d6d12e8724461d7eea12a5d9bae4d8c5ad8a77a6e32aa33a@ec2-34-194-14-176.compute-1.amazonaws.com:5432/d5t6ibvkjcp7gq'

    from app.db import init_db

    init_db(app)





    from app.models.admin import User
    from app.views.users.bp_users import users_bp
    app.register_blueprint(users_bp, url_prefix='/users_page')


    from app.models.image import ImageModel
    from app.views.image.bp_image import image_pb
    app.register_blueprint(image_pb,url_prefix='/image_api')


    from app.api.notification import notificat_bp_spar
    app.register_blueprint(notificat_bp_spar,url_prefix='/spar')


    from app.api.scrapper import scraper
    app.register_blueprint(scraper,url_prefix='/scraper')

    # TODO
    Migrate(app,app.db)
    # config_admin(app)

    # registando todos os modelos necessarios para o meu gerenciador de Admin
    admin=Admin(app)
    admin.add_view(ModelView(User,app.db.session))
    admin.add_view(ModelView(ImageModel,app.db.session))




    @app.route("/", methods=['GET', 'POST'])
    def index():

        return render_template('index.html')
    @app.route('/get_fruits',methods=['POST','GET'])
    def get_files():
    	# file= url_for('static',filename='fruits.json')
        # file= url_for('static',filename='casa_cozinha_1.json')
        return app.send_static_file('databases/fruits.json')

    	# return Response(file,mimetype='json' )
    	# return app.send_static_file('casa_cozinha_0.json')
    @app.route('/get_casa/cozinha/<page_id>',methods=['POST','GET'])
    def get_casa(page_id):
        file=''
        if int(page_id)==1:
    	    file= 'casa_cozinha_0.json'

        else:
            file= 'casa_cozinha_1.json'
        return app.send_static_file(file)




    @app.route('/getproducts/<indice>',methods=['GET'])
    def get_products_by_category(indice):
        _db_path='databases'
        fruits=_db_path+'/fruits.json',
        elect=_db_path+'/casa_electronicos.json',
        lavand=_db_path+'/casa_lavandaria.json',
        try:
            id=int(indice)
            if(id >=len(json_dbs)):
                return 'Numero Invalido'
            else:
                return app.send_static_file(json_dbs[id])
        except  Exception as e:
            # return 'NUMEROS APENAS'
            return app.send_static_file('databases/fruits.json')
    @app.route('/getmercearia/<index>',methods=['GET','POST'])
    def get_mercearia(index):
        _db_path='databases/17-10-2021/'
        talho=_db_path+'talho.json'
        try:
            id=int(index)
            if(id>=len(json_mercearia)):
                return jsonify({'response':200,'error':'digite apenas numeros'})
            return app.send_static_file(json_mercearia[id])
        except  Exception as e:
            return app.send_static_file(_db_path+'merc_arroz.json')

    routa2 = 'https://flaskchatbotmoz.herokuapp.com/bot'

    # @app.shell_context_processor
    # def make_shell_context():
    #     # com isto aki posso entrar no shell e fazer testes esporatico
    #     '''
        # db.create_all()  >> criare o banco
    #     '''
        # return dict(app=app, db=app.db, User=User)

    @app.route('/bot', methods=['POST', 'GET'])
    def response():
        print(request.method)
        if request.method == 'GET':
            return jsonify({'method': request.method, 'info': 'fizeste um GET por isso esta tendo esta resposta queira entao fazer um POST?'})
        # recebo o posto mandado por cliente
        # e devolvo para ele o result + a hora que este response foi feita
        query = dict(request.form)['query']
        result = 'comando nao reconhecido'
        if 'name' in query:
            result = 'my name is saidinoBot from python'
        elif 'image' in query.lower():
            result = 'thats is saidino image https://flaskchatbotmoz.herokuapp.com/static/image/hacking_tool.png'
        else:
            result = 'That command have not implemented yet'

        response = result+" \ntime is :"+time.ctime()
        return jsonify(response)

    return app


def main():
    app = create_app()
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()
