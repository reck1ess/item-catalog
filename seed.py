#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

category1 = Category(name="Support", user_id=1)

session.add(category1)
session.commit()

item1 = CategoryItem(name="Sona", user_id=1, description="Sona is Demacia's foremost virtuoso of the stringed etwahl, speaking only through her graceful chords and vibrant arias. This genteel manner has endeared her to the highborn, though others suspect her spellbinding melodies to actually emanate magic—a Demacian taboo. Silent to outsiders but somehow understood by close companions, Sona plucks her harmonies not only to soothe injured allies, but also to strike down unsuspecting enemies", category=category1)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Janna", user_id=1,  description="Armed with the power of Runeterra's gales, Janna is a mysterious, elemental wind spirit who protects the dispossessed of Zaun. Some believe she was brought into existence by the pleas of Runeterra's sailors who prayed for fair winds as they navigated treacherous waters and braved rough tempests. Her favor and protection has since been called into the depths of Zaun, where Janna has become a beacon of hope to those in need. No one knows where or when she will appear, but more often than not, she's come to help.", category=category1)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Soraka", user_id=1, description="A wanderer from the celestial dimensions beyond Mount Targon, Soraka gave up her immortality to protect the mortal races from their own more violent instincts. She endeavors to spread the virtues of compassion and mercy to everyone she meets—even healing those who would wish harm upon her. And, for all Soraka has seen of this world's struggles, she still believes the people of Runeterra have yet to reach their full potential.", category=category1)

session.add(item3)
session.commit()

category2 = Category(name="Jungle", user_id=1)

session.add(category2)
session.commit()

item1 = CategoryItem(name="Lee Sin", user_id=1, description="A master of Ionia's ancient martial arts, Lee Sin is a principled fighter who channels the essence of the dragon spirit to face any challenge. Though he lost his sight many years ago, the warrior-monk has devoted his life to protecting his homeland against any who would dare upset its sacred balance. Enemies who underestimate his meditative demeanor will endure his fabled burning fists and blazing roundhouse kicks", category=category2)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Master Yi", user_id=1,  description="Master Yi has tempered his body and sharpened his mind, so that thought and action have become almost as one. Though he chooses to enter into violence only as a last resort, the grace and speed of his blade ensures resolution is always swift. As one of the last living practitioners of the Ionian art of Wuju, Yi has devoted his life to continuing the legacy of his people—scrutinizing potential new disciples with the Seven Lenses of Insight to identify the most worthy among them", category=category2)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Fiddlesticks", user_id=1, description="Fiddlesticks is a ghastly, living scarecrow who stalks the darkness, wielding a cruel scythe and preying upon the unwary. Once a lonely man accused of bringing famine to his village, he was tied up and left to starve in his own barren field. Resurrected by the savage murder of crows that fed on his remains, Fiddlesticks now relishes terrorizing his victims before claiming their lives amid a flurry of feathers and blood-splattered beaks.", category=category2)

session.add(item3)
session.commit()

category3 = Category(name="Top", user_id=1)

session.add(category3)
session.commit()

item1 = CategoryItem(name="Darius", user_id=1, description="There is no greater symbol of Noxian might than Darius, the nation's most feared and battle-hardened leader. Rising from humble origins to become the Hand of Noxus, he cleaves through the empire's enemies—many of them Noxians themselves. Knowing that he never doubts his cause is just, and never hesitates once his axe is raised, those who stand against the commander of the Trifarian Legion can expect no mercy.", category=category3)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Rumble", user_id=1, description="Rumble is a young inventor with a temper. Using nothing more than his own two hands and a heap of scrap, the feisty yordle constructed a colossal mech suit outfitted with an arsenal of electrified harpoons and incendiary rockets. Though others may scoff and sneer at his junkyard creations, Rumble doesn't mind—after all, he's the one with the flamespitter.", category=category3)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Singed", user_id=1,
                     description="Singed is a Zaunite alchemist of unmatched intellect, who has devoted his life to pushing the boundaries of knowledge—with no price, even his own sanity, too high to pay. Is there a method to his madness? His concoctions rarely fail, but it appears to many that Singed has lost all sense of humanity, leaving a toxic trail of misery and terror in his wake.", category=category3)

session.add(item3)
session.commit()

category4 = Category(name="Mid", user_id=1)

session.add(category4)
session.commit()


categories = session.query(Category).all()
for category in categories:
    print "Category: " + category.name
