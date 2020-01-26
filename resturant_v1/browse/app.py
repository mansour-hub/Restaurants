import requests
from flask import Flask, request, redirect, render_template
from flask import session as login_session

from databases import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/listings')
def listings():
    restaurants=query_all()
    return render_template('listings.html',restaurants=restaurants)
    
@app.route('/about')
def about():
    return render_template('about.html')
# @app.route('/login', methods=['POST'])
# def login():
#     user = get_user(request.form['username'])
#     if user != None and user.verify_password(request.form["password"]):
#         login_session['name'] = user.username
#         login_session['logged_in'] = True
#         return logged_in()
#     else:
#         return home()


# @app.route('/signup', methods=['POST'])
# def signup():
#     #check that username isn't already taken
#     user = get_user(request.form['username'])
#     if user == None:
#         add_user(request.form['username'],request.form['password'])
#     return home()


# @app.route('/logged-in')
# def logged_in():
#     return render_template('logged.html')


# @app.route('/logout')
# def logout():
#     login_session['name'] = None
#     login_session['logged_in'] = False
#     return home()
@app.route('/search', methods=['POST'])
def search():
    response = GenarateRestaurants(request.form['name'])
    return render_template('index.html', restlist=response)
def GenarateRestaurants(name):
    url = "https://geo-location1.p.rapidapi.com/address/%7Bwithin30.com%7D"

    headers = {
        'x-rapidapi-host': "geo-location1.p.rapidapi.com",
        'x-rapidapi-key': "8152020523mshf3110d3c051b512p1f135fjsn53cba009bdba"
        }

    response = requests.request("GET", url, headers=headers)

    print(response.text)

    return response

if __name__ == '__main__':
    app.run(debug=True)
