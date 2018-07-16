import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from models import Todo as TodoModel
from models import Person as PersonModel

class Todo(SQLAlchemyObjectType):
    class Meta:
        model = TodoModel

class Person(SQLAlchemyObjectType):
    class Meta:
        model = PersonModel

class Query(graphene.ObjectType):
    # Get a list of all chores
    all_todos = graphene.List(Todo)
    def resolve_all_todos(self, info, **args):
        query = Todo.get_query(info)
        return query.all()
    
    # Get chores separated by person and can search for a specific one
    get_chores = graphene.List(Person, person=graphene.String())
    def resolve_get_chores(self, info, **args):
        query = Person.get_query(info)
        person = args.get('person')
        if person is not None:
            print(person)
            return query.filter(PersonModel.name.contains(person)).all()
        else:
            return query.all()

schema = graphene.Schema(query=Query)
