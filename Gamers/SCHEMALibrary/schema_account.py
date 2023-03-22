import graphene
from graphql_auth import mutations
from graphql_auth.schema import UserQuery, MeQuery
from graphene_django import DjangoObjectType, DjangoListField
from graphql_jwt.decorators import login_required
from ..models import ExtendUser

class AccountFriendsType(DjangoObjectType):
    class Meta:
        model = ExtendUser
        fields = ["account_friends"]


class AccountFriends_AddMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        friend = graphene.String(required=True)
        token = graphene.String(required=True)
    account_friends = graphene.List(graphene.String)
    success = graphene.Boolean(False)
    @login_required
    def mutate(cls, root, username, friend, token):
        yourself = ExtendUser.objects.get(username=username)
        if (yourself.account_friends == None): 
            yourself.account_friends = []
        yourself.account_friends.append(friend)
        yourself.save()
        return AccountFriends_AddMutation(success=True, account_friends=yourself.account_friends)
    

class AccountFriends_DelMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        friend = graphene.String(required=True)
        token = graphene.String(required=True)
    account_friends = graphene.List(graphene.String)
    success = graphene.Boolean(False)
    @login_required
    def mutate(cls, root, username, friend, token):
        yourself = ExtendUser.objects.get(username=username)
        if (yourself.account_friends == None): 
            yourself.account_friends = []
        yourself.account_friends.remove(friend)
        yourself.save()
        return AccountFriends_DelMutation(success=True, account_friends=yourself.account_friends)

class AccountInfo_Mutation(graphene.ObjectType):
    add_friend = AccountFriends_AddMutation.Field()
    remove_friend = AccountFriends_DelMutation.Field()
