from model import *


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_restaurant(name,  picture_link, description):

    restaurant1 = restaurant(
        name=name,
        picture_link=picture_link,
        description=description)
    session.add(restaurant1)
    session.commit()


add_restaurant("Y.M.C.A","data:image/jpeg;base64,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","Nazareth")
add_restaurant("Rosemary","data:image/jpeg;base64,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","Old City, Nazareth")
add_restaurant("Cafe Greg","https://media-cdn.tripadvisor.com/media/photo-s/12/8e/b8/28/photo0jpg.jpg","Old City, Nazareth")
add_restaurant("Bayat","https://media-cdn.tripadvisor.com/media/photo-s/18/53/0b/e4/bayat-restaurant.jpg","Old City, Nazareth")
add_restaurant("Ronen","https://www.nazareth360.com/sites//default/files/600451_489813647768189_1439890877_n.jpg","Old City,Nazareth")

def delete_restaurant(the_name):
	
	session.query(restaurant).filter_by(
		name=the_name).first().delete()
	session.commit()

def update_restaurant(name, picture_link, description):

	restaurant1 = session.query(restaurant).filter_by(
		name=name).first()
	restaurant1.name = name
	restaurant1.picture_link = picture_link
	restaurant1.description = description

	session.commit()

def query_all():
	return session.query(
		restaurant).all()

def query_by_name(the_name):

	restaurant1 = session.query(
		restaurant).filter_by(
		name=the_name).first()
	return restaurant1
