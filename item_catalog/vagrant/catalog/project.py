from flask import Flask, render_template, request, redirect,jsonify, url_for, flash
app = Flask(__name__)

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User

#new imports for this step
from flask import session as login_session
import random, string

# IMPORTS FOR THIS STEP
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)


#Connect to Database and create database session
engine = create_engine('sqlite:///categoryitemwithusers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/login')
def showLogin():
    return "login page"


@app.route('/fbconnect', methods=['POST'])
def fbconnect():
    return "fb connecting page"


@app.route('/gconnect', methods=['POST'])
def gconnect():
    return "gplus connecting page"


# DISCONNECT - Revoke a current user's token and reset their login_session
@app.route('/gdisconnect')
def gdisconnect():
    return "gplus disconnecting page"


@app.route('/fbdisconnect')
def fbdisconnect():
    return "fb disconnecting page"


# Disconnect based on provider
@app.route('/disconnect')
def disconnect():
    return "disconnecting function helper page"

#JSON APIs to view category Information
@app.route('/category/JSON')
def categoryJSON():
    return "json"

@app.route('/category/<int:category_id>/item/JSON')
def categoryItemJSON(category_id):
    return "json"


@app.route('/category/<int:category_id>/item/<int:item_id>/JSON')
def ItemJSON(category_id, item_id):
    return "json"

#Show all categories
@app.route('/')
@app.route('/category/')
def showCategories():
    return "show category"

#Create a new category
@app.route('/category/new/', methods=['GET','POST'])
def newCategory():
    return "make new category"

#Edit a category
@app.route('/category/<int:category_id>/edit/', methods = ['GET', 'POST'])
def editCategory(category_id):
    return "edit category"

#Delete a category
@app.route('/category/<int:category_id>/delete/', methods = ['GET','POST'])
def deleteCategory(category_id):
    return "delete category"

#Show a category item
@app.route('/category/<int:category_id>/')
@app.route('/category/<int:category_id>/item/')
def showitem(category_id):
    return "show an item of the category"

#Create a new item
@app.route('/category/<int:category_id>/item/new/',methods=['GET','POST'])
def newItem(category_id):
    return "make an item of the category"
#Edit a item
@app.route('/category/<int:category_id>/item/<int:item_id>/edit', methods=['GET','POST'])
def editItem(category_id, item_id):
    return "edit an item of the category"

#Delete a item
@app.route('/category/<int:category_id>/item/<int:item_id>/delete', methods = ['GET','POST'])
def deleteItem(category_id,item_id):
    return "delete an item of the category "

# User Helper Functions
def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id

def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


if __name__ == '__main__':
  app.secret_key = '6pKQC9BWFdQNtNHDkE'
  app.debug = True
  app.run(host = '0.0.0.0', port = 8000)
