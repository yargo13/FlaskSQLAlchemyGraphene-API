def init_db():
    from models import Todo
    from database import Base,engine, db_session
    
    Base.metadata.drop_all(bind = engine)
    Base.metadata.create_all(bind = engine)

    iron = Todo(item = "iron clothes")
    programming = Todo(item = "do programming hw")
    startup = Todo(item = "build a startup")
    db_session.add(iron)
    db_session.add(programming)
    db_session.add(startup)
    db_session.commit()

from requests import put, get, delete

init_db()

print(get('http://localhost:5000/graphql?query={todos{id,item}}').json())