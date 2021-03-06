from flask import Blueprint,render_template,request,jsonify
from bs4 import BeautifulSoup 
import requests as rq


scraper=Blueprint('scraper',__name__,url_prefix='/scraper',template_folder='templates')
titles=[]

@scraper.route('/')
def index():
    # return jsonify([{'name':'saidie','idade':12}])
    return render_template('post.html',titles=titles,products=[])

@scraper.route('/admin',methods=['POST','GET'])
def admin():
    value =request.json
    print(value)
    return jsonify([{"you":'saidino','lover':'yes',"data":f'{value}'}])
@scraper.route("/scrap", methods=['POST','GET'])
def scrap():

    uri='=';
    description=' ( A DETERMINAR ...)'
    print('GETTING DATAS...')
    try:
        url=request.form['uri']
        print(f" posted by form :url {url}")
        uri=url
        
    except  Exception as e:
        try:
            json=request.json
            print(f'from json {json}')
            if json !=None:
                uri=json['uri']
                description=json['description']
        except  Exception as e:
            printf("sem  link reconecido {e}")
    
    print(f'by json post {uri}')

    if len(uri)<8:
        return "link invalid"
    print(f'{uri} has got')
    data =rq.get(uri).text
    list_product_xpath ='/html/body/div[1]/div[3]/div/div/div/div[4]/ul'
    soup = BeautifulSoup(data, 'html.parser')
    _products_inner =soup.find_all('div', class_='product-inner')
   
    print('I got products')
    products =[]
    for product in _products_inner:
        detail_uri =product.select('h2 a')[1]['href']
        title =product.select('h2 a')[0].get_text()
        titles.append(title)

        image_data = product.select('a img')
        image_og = product.select('a img')[0]['data-original']
        image = product.select('a img')[0]['src']
        price = product.find('span', class_='price').select('bdi')[0].get_text()
        print(f"\033[32m {title} \033[0m \033[34m {price} \033[0m DESC: \033[36m{description}\033[m")
        # details=get_details(detais_uri)
        products.append(
                {'product_name':title,
                    'url_img':image_og,
                    'prod_details':detail_uri,
                    'description':description,
                    'price':price,#details['price'],
                    'category':None,#details['category'],
                    'medida':None,#details['medida'],
                    })

    # print(products)
    # return render_template('post.html',titles=titles,products=products)
    return jsonify(products)
