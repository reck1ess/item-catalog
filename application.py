from flask import Flask, render_template, url_for, request, redirect, jsonify, make_response, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, CategoryItem, User
from flask import session as login_session
import random
import string
import json
import httplib2
import requests


app = Flask(__name__)

engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def createUser(login_session):
    newUser = User(name=login_session['username'],
                   email=login_session['email'], picture=login_session['picture'])
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


@app.route('/')
@app.route('/catalog')
def showCategories():
    categories = session.query(Category).all()
    categoryItems = session.query(CategoryItem).all()

    return render_template('categories.html', categories=categories, categoryItems=categoryItems)


@app.route('/catalog/<int:catalog_id>')
@app.route('/catalog/<int:catalog_id>/items')
def showCategory(catalog_id):
    categories = session.query(Category).all()
    category = session.query(Category).filter_by(id=catalog_id).first()
    categoryName = category.name
    categoryItems = session.query(CategoryItem).filter_by(
        category_id=catalog_id).all()
    categoryItemsCount = session.query(
        CategoryItem).filter_by(category_id=catalog_id).count()

    return render_template('category.html', categories=categories, categoryItems=categoryItems, categoryName=categoryName, categoryItemsCount=categoryItemsCount)


@app.route('/catalog/<int:catalog_id>/items/<int:item_id>')
def showCategoryItem(catalog_id, item_id):
    categoryItem = session.query(CategoryItem).filter_by(id=item_id).first()
    author = getUserInfo(categoryItem.user_id)

    return render_template('categoryItem.html', categoryItem=categoryItem, author=author)


if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'super_secret_key'
    app.run(host='0.0.0.0', port=5000)
