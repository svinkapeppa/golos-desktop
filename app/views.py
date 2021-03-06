from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from piston import Steem, account

from app import app, db
from app.forms import LoginForm, RegistrationForm, TransferForm, PostForm
from app.models import User


class Man:
    def __init__(self, login="vgolos3", password="P5Hu2Vb5N2Gsrp5cWSZp4tHvaJr5cUBtmwEQJs7C6N6oU52E8q7d"):
        self.steem_instance_ = Steem(node="wss://ws.testnet3.golos.io", rpcuser=login, rpcpassword=password)
        self.user_ = account.Account(account_name=login, steem_instance=self.steem_instance_)

    def get_posts(self, limit=10,
                  sort="active",
                  category=None,
                  start=None):
        # list of dicts
        return self.steem_instance_.get_posts(limit=limit, sort=sort, category=category, start=start)

    def get_user_posts(self, ):
        pass


@app.route('/')
@app.route('/index')
@login_required
def index():
    users = User.query.all()
    username = users[0].username
    password = users[0].password_hash
    posts = top10(username, password)
    return render_template('index.html', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        posts = top10(form.username.data, form.password.data)
        return render_template('index.html', posts=posts)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/transfer')
@login_required
def transfer():
    form = TransferForm()
    if form.validate_on_submit():
        return redirect(url_for('login'))
    return render_template('transfer.html', title='Transfer', form=form)


@app.route('/post')
@login_required
def post():
    form = PostForm()
    if form.validate_on_submit():
        return redirect(url_for('login'))
    return render_template('post.html', title='Post', form=form)


def top10(username, password):
    user = Man(username, password)
    posts = user.get_posts(sort="active")
    return posts


app.jinja_env.globals.update(top10=top10)
