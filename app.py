from flask import Flask, request, render_template, session, redirect
from lib.pocket import PocketApi
import json

app = Flask(__name__)
app.config.from_file("config.json", load=json.load)

@app.route('/')
def home():
    if 'login_token' in session:
        return redirect('/items')
    return render_template('index.html')

@app.route('/login')
def login():
    session['pocket_request_token'] = PocketApi().get_access_token(app.config['POCKET_CONSUMER_KEY'])
    redirect_url = PocketApi().construct_redirect_url(session['pocket_request_token'])
    return redirect(redirect_url)

@app.route('/authorize')
def authorize():
    session['login_token'] = PocketApi().get_request_token(app.config['POCKET_CONSUMER_KEY'], session['pocket_request_token'])
    return redirect('/')

@app.route('/items')
def index():
    items = PocketApi().list_items(app.config['POCKET_CONSUMER_KEY'], session['login_token'])
    return render_template('items.html', items=items)