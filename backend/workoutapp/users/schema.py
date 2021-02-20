from graphene_django import DjangoObjectType
import graphene
from .models import Trainees

class UserType(DjangoObjectType):
    class Meta:
        model = Trainees



class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user_by_id = graphene.Field(UserType, id=graphene.Int())

    def resolve_users(self, info):
        return Trainees.objects.all()

    def resolve_user_by_id(self, info, id):
        return Trainees.objects.get(id=id)




class CreateUser(graphene.Mutation):
    id = graphene.Int()
    userName = graphene.String()
    workout_type = graphene.String()

    class Arguments:
        userName = graphene.String()
        workout_type = graphene.String()
    
    def mutate(self, info, userName, workout_type):
        user = Trainees(userName=userName, workout_type=workout_type)
        user.save()
        return CreateUser(
            id=user.id,
            userName = user.userName,
            workout_type = user.workout_type,
        )


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()




schema = graphene.Schema(
    query = Query,
    mutation = Mutation
)