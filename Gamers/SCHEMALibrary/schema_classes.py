import graphene
from graphql_auth import mutations
from graphql_auth.schema import UserQuery, MeQuery
from graphene_django import DjangoObjectType, DjangoListField
from graphql_jwt.decorators import login_required
from ..models import ExtendUser

#[0, [0, 0, 0, 0, 0, 0]]
initializedClass = [[0 for j in range(12)] for i in range(6)]
initializePrimaryAttachments = [0 for i in range(8)]
initializeSecondaryAttachments = [0 for i in range(8)]
initializedUnlocked = [[0 for j in range(30)] for i in range(10)]
initializedUnlockedAttachments = [[[0 for j in range(30)] for k in range(30)] for i in range(2)]
initializedUnlockedCamos = [[[0 for j in range(100)] for k in range(30)] for i in range(2)]

for i in range(0, 5):
    #initializedClass[i][0] = 1
    initializedUnlocked[i][0] = 1
    if i < 2:
        for j in range(30):
            initializedUnlockedAttachments[i][j][0] = 1
            initializedUnlockedCamos[i][j][0] = 1

#Primary TEST
initializedUnlocked[0][4] = 1
#Secondary TEST
initializedUnlocked[1][3] = 1

#Perks Default
initializedUnlocked[2][1] = 1
initializedUnlocked[3][1] = 1
initializedUnlocked[4][1] = 1

initializedUnlockedAttachments[0][4][2] = 1
initializedUnlockedAttachments[1][3][2] = 1


class AccountClassesType(DjangoObjectType):
    class Meta:
        model = ExtendUser
        fields = ["classes", "unlocked_specs", "unlocked_gunattachments", "unlocked_guncamos"]


class AccountClasses_ChangePrimary(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        value = graphene.Int(required=True)
        iclass = graphene.Int(required=True)
        token = graphene.String(required=True)
    current_class = graphene.List(graphene.Int)
    success = graphene.Boolean(False)
    error = graphene.String(None)
    @login_required
    def mutate(cls, root, username, value, iclass, token):
        yourself = ExtendUser.objects.get(username=username)
        #if (yourself.classes == None): 
        yourself.classes = initializedClass
        if value < 30:
            #if (yourself.unlocked_specs == None): 
            yourself.unlocked_specs = initializedUnlocked
            #    yourself.save()
            if yourself.unlocked_specs[0][value] == 1:
                yourself.classes[iclass][0] = value
                yourself.current_primary_attachments = initializePrimaryAttachments
                yourself.current_secondary_attachments = initializeSecondaryAttachments
                yourself.save()
                return AccountClasses_ChangePrimary(current_class=yourself.classes[iclass], success=True, error=None)
            return AccountClasses_ChangePrimary(current_class=yourself.classes[iclass], success=False, error="Not Unlocked Yet.")
        return AccountClasses_ChangePrimary(current_class=yourself.classes[iclass], success=False, error="Not Possible.")
    







class AccountClasses_ChangePrimaryAttachment(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        level = graphene.Int(required=True)
        value = graphene.Int(required=True)
        iclass = graphene.Int(required=True)
        token = graphene.String(required=True)
    current_class = graphene.List(graphene.Int)
    success = graphene.Boolean(False)
    error = graphene.String(None)
    @login_required
    def mutate(cls, root, username, value, iclass, level, token):
        yourself = ExtendUser.objects.get(username=username)
        if (yourself.classes == None): 
            yourself.classes = initializedClass
        if value < 30:
            if (yourself.unlocked_gunattachments == None): 
                yourself.unlocked_gunattachments = initializedUnlockedAttachments
                yourself.current_primary_attachments = initializePrimaryAttachments
                yourself.current_secondary_attachments = initializeSecondaryAttachments
                yourself.save()
            #GET CURRENT CLASS PRIMARY
            class_primary = yourself.classes[iclass][0]
            if yourself.unlocked_gunattachments[0][class_primary][level * 4 + value] == 1:
                yourself.current_primary_attachments[level] = value
                yourself.save()
                return AccountClasses_ChangePrimaryAttachment(current_class=yourself.classes[iclass], success=True, error=None)
            return AccountClasses_ChangePrimaryAttachment(current_class=yourself.classes[iclass], success=False, error="Not Unlocked Yet.")
        return AccountClasses_ChangePrimaryAttachment(current_class=yourself.classes[iclass], success=False, error="Not Possible.")
    

class AccountClasses_ChangeSecondaryAttachment(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        level = graphene.Int(required=True)
        value = graphene.Int(required=True)
        iclass = graphene.Int(required=True)
        token = graphene.String(required=True)
    current_class = graphene.List(graphene.Int)
    success = graphene.Boolean(False)
    error = graphene.String(None)
    @login_required
    def mutate(cls, root, username, value, iclass, level, token):
        yourself = ExtendUser.objects.get(username=username)
        if (yourself.classes == None): 
            yourself.classes = initializedClass
        if value < 30:
            if (yourself.unlocked_gunattachments == None): 
                yourself.unlocked_gunattachments = initializedUnlockedAttachments
                yourself.current_primary_attachments = initializePrimaryAttachments
                yourself.current_secondary_attachments = initializeSecondaryAttachments
                yourself.save()
            #GET CURRENT CLASS PRIMARY
            class_secondary = yourself.classes[iclass][1]
            if yourself.unlocked_gunattachments[1][class_secondary][level * 4 + value] == 1:
                yourself.current_secondary_attachments[level] = value
                yourself.save()
                return AccountClasses_ChangeSecondaryAttachment(current_class=yourself.classes[iclass], success=True, error=None)
            return AccountClasses_ChangeSecondaryAttachment(current_class=yourself.classes[iclass], success=False, error="Not Unlocked Yet.")
        return AccountClasses_ChangeSecondaryAttachment(current_class=yourself.classes[iclass], success=False, error="Not Possible.")
    










class AccountClasses_ChangeSecondary(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        value = graphene.Int(required=True)
        iclass = graphene.Int(required=True)
        token = graphene.String(required=True)
    current_class = graphene.List(graphene.Int)
    success = graphene.Boolean(False)
    error = graphene.String(None)
    @login_required
    def mutate(cls, root, username, value, iclass, token):
        yourself = ExtendUser.objects.get(username=username)
        if (yourself.classes == None): 
            yourself.classes = initializedClass
        if value < 30:
            if (yourself.unlocked_specs == None): 
                yourself.unlocked_specs = initializedUnlocked
                yourself.save()
            if yourself.unlocked_specs[1][value] == 1:
                yourself.classes[iclass][1] = value
                yourself.save()
                return AccountClasses_ChangeSecondary(current_class=yourself.classes[iclass], success=True, error=None)
            return AccountClasses_ChangeSecondary(current_class=yourself.classes[iclass], success=False, error="Not Unlocked Yet.")
        return AccountClasses_ChangeSecondary(current_class=yourself.classes[iclass], success=False, error="Not Possible.")





'''

'''
class AccountClasses_ChangePerk1(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        value = graphene.Int(required=True)
        iclass = graphene.Int(required=True)
        token = graphene.String(required=True)
    current_class = graphene.List(graphene.Int)
    success = graphene.Boolean(False)
    error = graphene.String(None)
    @login_required
    def mutate(cls, root, username, value, iclass, token):
        yourself = ExtendUser.objects.get(username=username)
        if (yourself.classes == None): 
            yourself.classes = initializedClass
        if value < 30:
            if (yourself.unlocked_specs == None): 
                yourself.unlocked_specs = initializedUnlocked
                yourself.save()
            if yourself.unlocked_specs[2][value] == 1:
                yourself.classes[iclass][2] = value
                yourself.save()
                return AccountClasses_ChangePerk1(current_class=yourself.classes[iclass], success=True, error=None)
            return AccountClasses_ChangePerk1(current_class=yourself.classes[iclass], success=False, error="Not Unlocked Yet.")
        return AccountClasses_ChangePerk1(current_class=yourself.classes[iclass], success=False, error="Not Possible.")
class AccountClasses_ChangePerk2(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        value = graphene.Int(required=True)
        iclass = graphene.Int(required=True)
        token = graphene.String(required=True)
    current_class = graphene.List(graphene.Int)
    success = graphene.Boolean(False)
    error = graphene.String(None)
    @login_required
    def mutate(cls, root, username, value, iclass, token):
        yourself = ExtendUser.objects.get(username=username)
        if (yourself.classes == None): 
            yourself.classes = initializedClass
        if value < 30:
            if (yourself.unlocked_specs == None): 
                yourself.unlocked_specs = initializedUnlocked
                yourself.save()
            if yourself.unlocked_specs[3][value] == 1:
                yourself.classes[iclass][3] = value
                yourself.save()
                return AccountClasses_ChangePerk2(current_class=yourself.classes[iclass], success=True, error=None)
            return AccountClasses_ChangePerk2(current_class=yourself.classes[iclass], success=False, error="Not Unlocked Yet.")
        return AccountClasses_ChangePerk2(current_class=yourself.classes[iclass], success=False, error="Not Possible.")
class AccountClasses_ChangePerk3(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        value = graphene.Int(required=True)
        iclass = graphene.Int(required=True)
        token = graphene.String(required=True)
    current_class = graphene.List(graphene.Int)
    success = graphene.Boolean(False)
    error = graphene.String(None)
    @login_required
    def mutate(cls, root, username, value, iclass, token):
        yourself = ExtendUser.objects.get(username=username)
        if (yourself.classes == None): 
            yourself.classes = initializedClass
        if value < 30:
            if (yourself.unlocked_specs == None): 
                yourself.unlocked_specs = initializedUnlocked
                yourself.save()
            if yourself.unlocked_specs[4][value] == 1:
                yourself.classes[iclass][4] = value
                yourself.save()
                return AccountClasses_ChangePerk3(current_class=yourself.classes[iclass], success=True, error=None)
            return AccountClasses_ChangePerk3(current_class=yourself.classes[iclass], success=False, error="Not Unlocked Yet.")
        return AccountClasses_ChangePerk3(current_class=yourself.classes[iclass], success=False, error="Not Possible.")
    








class AccountClasses_ChangeLethal(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        value = graphene.Int(required=True)
        iclass = graphene.Int(required=True)
        token = graphene.String(required=True)
    current_class = graphene.List(graphene.Int)
    success = graphene.Boolean(False)
    error = graphene.String(None)
    @login_required
    def mutate(cls, root, username, value, iclass, token):
        yourself = ExtendUser.objects.get(username=username)
        if (yourself.classes == None): 
            yourself.classes = initializedClass
        if value < 30:
            if (yourself.unlocked_specs == None): 
                yourself.unlocked_specs = initializedUnlocked
                yourself.save()
            if yourself.unlocked_specs[5][value] == 1:
                yourself.classes[iclass][5] = value
                yourself.save()
                return AccountClasses_ChangeLethal(current_class=yourself.classes[iclass], success=True, error=None)
            return AccountClasses_ChangeLethal(current_class=yourself.classes[iclass], success=False, error="Not Unlocked Yet.")
        return AccountClasses_ChangeLethal(current_class=yourself.classes[iclass], success=False, error="Not Possible.")
    





class AccountClasses_ChangeTactical(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        value = graphene.Int(required=True)
        iclass = graphene.Int(required=True)
        token = graphene.String(required=True)
    current_class = graphene.List(graphene.Int)
    success = graphene.Boolean(False)
    error = graphene.String(None)
    @login_required
    def mutate(cls, root, username, value, iclass, token):
        yourself = ExtendUser.objects.get(username=username)
        if (yourself.classes == None): 
            yourself.classes = initializedClass
        if value < 30:
            if (yourself.unlocked_specs == None): 
                yourself.unlocked_specs = initializedUnlocked
                yourself.save()
            if yourself.unlocked_specs[6][value] == 1:
                yourself.classes[iclass][6] = value
                yourself.save()
                return AccountClasses_ChangeTactical(current_class=yourself.classes[iclass], success=True, error=None)
            return AccountClasses_ChangeTactical(current_class=yourself.classes[iclass], success=False, error="Not Unlocked Yet.")
        return AccountClasses_ChangeTactical(current_class=yourself.classes[iclass], success=False, error="Not Possible.")
    







class AccountClasses_ChangeDeathstreak(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        value = graphene.Int(required=True)
        iclass = graphene.Int(required=True)
        token = graphene.String(required=True)
    current_class = graphene.List(graphene.Int)
    success = graphene.Boolean(False)
    error = graphene.String(None)
    @login_required
    def mutate(cls, root, username, value, iclass, token):
        yourself = ExtendUser.objects.get(username=username)
        if (yourself.classes == None): 
            yourself.classes = initializedClass
        if value < 30:
            if (yourself.unlocked_specs == None): 
                yourself.unlocked_specs = initializedUnlocked
                yourself.save()
            if yourself.unlocked_specs[7][value] == 1:
                yourself.classes[iclass][7] = value
                yourself.save()
                return AccountClasses_ChangeDeathstreak(current_class=yourself.classes[iclass], success=True, error=None)
            return AccountClasses_ChangeDeathstreak(current_class=yourself.classes[iclass], success=False, error="Not Unlocked Yet.")
        return AccountClasses_ChangeDeathstreak(current_class=yourself.classes[iclass], success=False, error="Not Possible.")
    

class AccountClasses_Mutation(graphene.ObjectType):
    changePrimary = AccountClasses_ChangePrimary.Field()
    changeSecondary = AccountClasses_ChangeSecondary.Field()
    changePerk1 = AccountClasses_ChangePerk1.Field()
    changePerk2 = AccountClasses_ChangePerk2.Field()
    changePerk3 = AccountClasses_ChangePerk3.Field()
    changeLethal = AccountClasses_ChangeLethal.Field()
    changeTactical = AccountClasses_ChangeTactical.Field()
    changeDeathstreak = AccountClasses_ChangeDeathstreak.Field()
    changePrimaryAttachment = AccountClasses_ChangePrimaryAttachment.Field()
    changeSecondaryAttachment = AccountClasses_ChangeSecondaryAttachment.Field()

