from amazon_scrap import Amazon_Scraper

from flask import Flask, render_template, request,jsonify
#from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq

app = Flask(__name__)  # initialising the flask


@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    return render_template('index.html')


@app.route('/scrap', methods=['GET','POST']) # route with allowed methods as POST and GET
def index():
    if request.method == 'POST':
        #try:
            scraper = Amazon_Scraper(keyword=request.form['content'],num_books=3, slp_time=1)
            result = scraper.get_books()
            print('Result:-')
            print(result)
            return render_template('results.html', reviews=result)  # showing the review to the user
        #except:
        #    return 'something is wrong'


if __name__ == "__main__":
    app.run(port=8000,debug=True)



#web: gunicorn data_collection:app