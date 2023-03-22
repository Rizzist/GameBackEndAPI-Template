#@classmethod
#@superuser_required


import graphene
from graphql_auth import mutations
from graphql_auth.schema import UserQuery, MeQuery
from graphene_django import DjangoObjectType, DjangoListField
from graphql_jwt.decorators import login_required, superuser_required
from ..models import ExtendUser



class Stats_AddMoney(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        amount = graphene.Int(required=True)
        token = graphene.String(required=True)
    current_amount = graphene.Int(0)
    success = graphene.Boolean(False)
    @classmethod
    @superuser_required
    def mutate(cls, root, info, username, amount, token):
        yourself = ExtendUser.objects.get(username=username)
        yourself.account_currency = yourself.account_currency + amount
        yourself.save()
        return Stats_AddMoney(success=True, current_amount = yourself.account_currency)
    


class Stats_AddXP(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        amount = graphene.Float(required=True)
        token = graphene.String(required=True)
    current_amount = graphene.Float(0)
    success = graphene.Boolean(False)
    @classmethod
    @superuser_required
    def mutate(cls, root, info, username, amount, token):
        yourself = ExtendUser.objects.get(username=username)
        yourself.account_XP = yourself.account_XP + amount
        #LEVELING UP LOGIC
        if (yourself.account_XP > 2500*1.1^(yourself.account_level - 1)):
            if yourself.account_level < 70:
                temp = yourself.account_XP - 2500*1.1^(yourself.account_level - 1)
                yourself.account_level += 1
                yourself.account_XP = temp

        yourself.save()
        return Stats_AddMoney(success=True, current_amount = yourself.account_currency)
    
class StatInfo_Mutation(graphene.ObjectType):
    addMoney = Stats_AddMoney.Field()
    addXP = Stats_AddXP.Field()





