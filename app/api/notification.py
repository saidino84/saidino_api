from flask import Blueprint,render_template,request,redirect,url_for,jsonify
import requests as rq
import json
notificat_bp_spar=Blueprint('spar',__name__,)


@notificat_bp_spar.route('/postproduct/',methods=['POST','GET'])
def postproduct():
    # firebase project Server key
    # print(request.data)
    if request.method=='POST':
        print(f"+++++++++++Request data is {request.json}")
        dados=json.loads(request.json)
        print(f" ###########{dados['to']}")
        try:
            print('puting into json')
            data={
            'to':dados['to'],
            'notification':{
            'body':dados['body'],
            'title':dados['title'],
            'image':dados['image']
            }
            
            }
            print('++++++++ ENCODE DONE ++++++++=')
            auth='key=AAAAT7I801w:APA91bFyk0q5leLPRR8YtKy3Q1s1wA38IcLdhZbkXF3ysCY7HdwOZ2IJEMQoaO8t5zKTwE_A8hockdmrL1FgkKkbqfK6FX4eCP5R7o1XLliD-e3OYFY1aruXPxac9rc_x6Dr6ly17nER'

            headers ={
            'Content-Type': 'application/json', 'Authorization': auth,
            }
            fcm_uri='https://fcm.googleapis.com/fcm/send'
            print(f"This is data {data}")
            response=rq.post(fcm_uri,headers=headers,data=json.dumps(data))
            print(f'The response is {response.json}')
        except  Exception as e:
            return jsonify({"estatus":"falhou a enviar","message":f"verifique os dados , pk eles sao invalidos {e}","code":300},),203

        return jsonify({"code":200,'status':'sucessfuly',"message":"received"}),200
    else:
        return 'your need to upload some things '
