from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Category, Item, User

engine = create_engine('sqlite:///categoryitemwithusers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create dummy user
User1 = User(name="Kikyo", email="kikyo@flower.com",
             picture='http://bluegreen.jp/photo/wp-content/uploads/2011/09/008_10243-500x333.jpg')
session.add(User1)
session.commit()

#  test1
category1 = Category(user_id=1, name="Test")

session.add(category1)
session.commit()

item1 = Item(user_id=1, name="aaa", description="aaaaa", category=category1)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="bbb", description="bbbbb", category=category1)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="ccc", description="ccccc", category=category1)

session.add(item3)
session.commit()


#  test2
category2 = Category(user_id=1, name="Test2")

session.add(category2)
session.commit()

item1 = Item(user_id=1, name="ddd", description="dddddd", category=category2)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="eee", description="eeeee", category=category2)

session.add(item2)
session.commit()

#  test3
category3 = Category(user_id=1, name="Test3")

session.add(category3)
session.commit()

item1 = Item(user_id=1, name="fff", description="ffffff", category=category3)

session.add(item1)
session.commit()
