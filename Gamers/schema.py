import graphene
from graphql_auth import mutations
from graphql_auth.schema import UserQuery, MeQuery
from graphene_django import DjangoObjectType, DjangoListField

from graphql_jwt.decorators import login_required



from .models import ExtendUser
from .SCHEMALibrary.schema_account import AccountInfo_Mutation
from .SCHEMALibrary.schema_classes import AccountClasses_Mutation
from .SCHEMALibrary.schema_stats import StatInfo_Mutation


class ExtendUserType(DjangoObjectType):
    class Meta:
        model = ExtendUser
        fields = ["email", "username", "account_status"]

class UserDataType(DjangoObjectType):
    class Meta:
        model = ExtendUser
        fields = ["username", "account_XP", "account_level", "account_currency", "account_friends", "success"]
'''
class AccountCurrencyType(DjangoObjectType):
    class Meta:
        model = ExtendUser
        fields = ["account_currency"]


class Account_InGameCurrency_Mutation(graphene.Mutation):
    class Arguments:
        amount = graphene.Int(required=True)
        id = graphene.ID()
    yourself = graphene.Field(AccountCurrencyType)

    @classmethod
    def mutate(cls, root, info, amount, id):
        yourself = ExtendUser.objects.get(id=id)
        yourself.account_currency = yourself.account_currency + amount
        yourself.save()
        return Account_InGameCurrency_Mutation(yourself=yourself)
'''



class Auth_Mutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    update_account = mutations.UpdateAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()

    # django-graphql-jwt inheritances
    token_auth = mutations.ObtainJSONWebToken.Field()
    verify_token = mutations.VerifyToken.Field()
    refresh_token = mutations.RefreshToken.Field()
    revoke_token = mutations.RevokeToken.Field()


class Query(UserQuery, MeQuery, graphene.ObjectType):
    viewer = graphene.Field(ExtendUserType, token=graphene.String(required=True))
    getUserData = graphene.Field(UserDataType, token=graphene.String(required=True))
    @login_required
    def resolve_viewer(self, info, **kwargs):
        return info.context.user
    def resolve_getUserData(self, info, **kwargs):
        return info.context.user
    #def resolve_all_users(root, info):
    #    return ExtendUser.objects.all()

class Mutation(
    AccountInfo_Mutation, 
    AccountClasses_Mutation,
    StatInfo_Mutation, 
    Auth_Mutation, 
    graphene.ObjectType):
    #update_currency = Account_InGameCurrency_Mutation.Field()
    #get_user_data = AuthClasses_GetUserData.Field()
    pass



schema = graphene.Schema(query=Query, mutation=Mutation)