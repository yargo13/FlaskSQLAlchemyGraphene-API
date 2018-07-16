import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from models import Todo as TodoModel

class Todo(SQLAlchemyObjectType):
    class Meta:
        model = TodoModel

class Query(graphene.ObjectType):
    todos = graphene.List(Todo)

    def resolve_todos(self, info):
        query = Todo.get_query(info)
        return query.all()

schema = graphene.Schema(query=Query)
