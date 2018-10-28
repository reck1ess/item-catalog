#!/usr/bin/env python

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_utils import database_exists, drop_database, create_database

from database_setup import Category, CategoryItem, User, Base

engine = create_engine('sqlite:///itemcatalog.db')

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

user1 = User(name="Tyler McGinnis", email="tylermcginnis@gmail.com",
             picture='https://tylermcginnis.com/would-you-rather/tyler.jpg')
session.add(user1)
session.commit()

category1 = Category(name="Top", user_id=1)

session.add(category1)
session.commit()

item1 = CategoryItem(name="Darius", user_id=1, description="the Hand of Noxus",
                     picture="https://ddragon.leagueoflegends.com/cdn/8.21.1/img/champion/Darius.png", category=category1)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Rumble", user_id=1, description="the Mechanized Menace",
                     picture="https://ddragon.leagueoflegends.com/cdn/8.21.1/img/champion/Rumble.png", category=category1)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Singed", user_id=1, description="the Mad Chemist",
                     picture="https://ddragon.leagueoflegends.com/cdn/8.21.1/img/champion/Singed.png", category=category1)

session.add(item3)
session.commit()


category2 = Category(name="Jungle", user_id=1)

session.add(category2)
session.commit()

item1 = CategoryItem(name="Lee Sin", user_id=1, description="the Blind Monk",
                     picture="https://ddragon.leagueoflegends.com/cdn/8.21.1/img/champion/LeeSin.png", category=category2)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Master Yi", user_id=1,  description="the Wuju Bladesman",
                     picture="https://ddragon.leagueoflegends.com/cdn/8.21.1/img/champion/MasterYi.png", category=category2)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Fiddlesticks", user_id=1, description="the Harbinger of Doom",
                     picture="https://ddragon.leagueoflegends.com/cdn/8.21.1/img/champion/Fiddlesticks.png", category=category2)

session.add(item3)
session.commit()


category3 = Category(name="Mid", user_id=1)

session.add(category3)
session.commit()

item1 = CategoryItem(name="Galio", user_id=1, description="the Colossus",
                     picture="https://ddragon.leagueoflegends.com/cdn/8.21.1/img/champion/Galio.png", category=category3)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Azir", user_id=1,  description="the Emperor of the Sands",
                     picture="https://ddragon.leagueoflegends.com/cdn/8.21.1/img/champion/Azir.png", category=category3)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Jayce", user_id=1, description="the Defender of Tomorrow",
                     picture="https://ddragon.leagueoflegends.com/cdn/8.21.1/img/champion/Jayce.png", category=category3)

session.add(item3)
session.commit()

category4 = Category(name="ADC", user_id=1)

session.add(category3)
session.commit()

item1 = CategoryItem(name="Ezreal", user_id=1, description="the Prodigal Explorer",
                     picture="https://ddragon.leagueoflegends.com/cdn/8.21.1/img/champion/Ezreal.png", category=category4)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Sivir", user_id=1,  description="the Battle Mistress",
                     picture="https://ddragon.leagueoflegends.com/cdn/8.21.1/img/champion/Sivir.png", category=category4)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Lucian", user_id=1, description="the Purifier",
                     picture="https://ddragon.leagueoflegends.com/cdn/8.21.1/img/champion/Lucian.png", category=category4)

session.add(item3)
session.commit()


category5 = Category(name="Support", user_id=1)

session.add(category5)
session.commit()

item1 = CategoryItem(name="Sona", user_id=1,
                     description="Maven of the Strings", picture="https://ddragon.leagueoflegends.com/cdn/8.21.1/img/champion/Sona.png", category=category5)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Janna", user_id=1,
                     description="the Storm's Fury", picture="https://ddragon.leagueoflegends.com/cdn/8.21.1/img/champion/Janna.png", category=category5)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Soraka", user_id=1,
                     description="the Starchild", picture="https://ddragon.leagueoflegends.com/cdn/8.21.1/img/champion/Soraka.png", category=category5)

session.add(item3)
session.commit()


categories = session.query(Category).all()
for category in categories:
    print "Category: " + category.name
