from flask import render_template, flash
from piston import Steem

from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return render_template('basic_info.html', result=form)
    return render_template('login.html', title='Sign In', form=form)


# rpcuser='ekhlyzov'
# rpcpassword='P5KBaPy7XurbVwCK1CUSKDNVGVVrh29xbvXQuYczjYNbdvcw2KYK'
def after_login(username, password):
    steem = Steem(node='wss://ws.testnet3.golos.io', rpcuser=username,
                  rpcpassword=password)
    account_info = steem.info()

    return 'Your account info{}'.format(account_info)


app.jinja_env.globals.update(after_login=after_login)
