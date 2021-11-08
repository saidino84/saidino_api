from flask import Blueprint,render_template,request,redirect,url_for,jsonify
import requests as rq
import json
notificat_bp_spar=Blueprint('spar',__name__,)


@notificat_bp_spar.route('/postproduct/',methods=['POST','GET'])
def postproduct():
    # firebase project Server key
    print(request.data)
    if request.method=='POST':
        # message,title,image_url
        print("+++++++++++++++++++++++++++++++++++++++++++++")
        print(request.json)
        print("+++++++++++++++++++++++++++++++++++++++++++==")
        data={
        'to':str(request.json['to']),
        'notification':{
        'message':str(request.json['notification']['message']),
        'title':str(request.json['notification']['title']),
        'image':str(request.json['notification']['image_url'])},
        "data":{
            "body":str(request.json['notification']['message']),
            "title":str(request.json['notification']['title']),
            "image":str(request.json['notification']['image_url'])
        }}
        # print(f'Body:{message},\nTile {message}, \nImage: {image_url}')
        auth='key=AAAAT7I801w:APA91bFyk0q5leLPRR8YtKy3Q1s1wA38IcLdhZbkXF3ysCY7HdwOZ2IJEMQoaO8t5zKTwE_A8hockdmrL1FgkKkbqfK6FX4eCP5R7o1XLliD-e3OYFY1aruXPxac9rc_x6Dr6ly17nER'

        headers ={
        'Content-Type': 'application/json', 'Authorization': auth,
        }
        fcm_uri='https://fcm.googleapis.com/fcm/send'
        # payload={
        # 'to':'/topics/ADMIN',
        # 'collapse_key':'type_a','data':{
        # "body":message,"title":title,"image":image_url
        # }
        # }
        # print(f'MESSAGE ****************{message}')

        response=rq.post(fcm_uri,headers=headers,data=json.dumps(data))
        print(response.text)
        return response.text
        return jsonify({"code":200,'status':'done'})
    else:
        return 'your need to upload some things '
