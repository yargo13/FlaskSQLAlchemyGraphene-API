def init_db():
    from models import Todo, Person
    from database import Base,engine, db_session
    
    Base.metadata.drop_all(bind = engine)
    Base.metadata.create_all(bind = engine)

    yargo = Person(name = 'Yargo')
    matheus = Person(name = 'Matheus')
    db_session.add(yargo)
    db_session.add(matheus)
    db_session.commit()

    yargo_id = Person.query.filter(Person.name=='Yargo').first().id
    matheus_id = Person.query.filter(Person.name=='Matheus').first().id
    iron = Todo(item = "iron clothes",person_id = yargo_id)
    programming = Todo(item = "do programming hw",person_id = matheus_id)
    startup = Todo(item = "build a startup", person_id = yargo_id)
    db_session.add(iron)
    db_session.add(programming)
    db_session.add(startup)
    db_session.commit()

from requests import put, get, delete

init_db()

print(get('''http://localhost:5000/graphql?query={
    allTodos{
        id,item
    }
}''').json())

print(get('''http://localhost:5000/graphql?query={
    getChores(person:"Yargo"){
    chore {
      item
    }
  }
}''').json())