from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField


'''
Gamer Information:
- DONE: Login info (username, password, email)
- Account Info
    - In-game currency
    - User Level
    - User XP (to Level)
    - Friends List

    - Character Decision
    - Classes (Below)
    - Calling Card & Emblem

- Class Information
    - Gun Type
    - Gun Level (for Camo)
    - Gun Attachments
    - Perks & Level
    - Equipment
'''


class AccountField(models.JSONField):
    pass

# Create your models here.
class ExtendUser(AbstractUser):
    
    email = models.EmailField(blank=False, max_length=255, verbose_name="email")
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    account_status = models.BooleanField(default=False)

    account_currency = models.IntegerField(default=0)
    account_level = models.IntegerField(default=1)
    account_XP = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    account_friends = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    success = models.BooleanField(default=True)
    #ROW 1: Primary, Secondary, Lethal, Tactical, Deathstreak, Perk 1, Perk 2, Perk 3
    #ROW 2: Primary Attachments: Scope, Magazine, Muzzle, Laser
    #ROW 3: Secondary Attachments: Scope, Magazine, Muzzle, Laser
    #ROW 4: Primary Camo, Secondary Camo, Scope Lens, Laser Color

    classes = ArrayField(
        ArrayField(                         
            models.IntegerField(default=0, blank=True),
            size=12
        ),
        size=6, null=True
    )

    current_primary_attachments = ArrayField(models.IntegerField(default=0, blank=True),size=8, null=True)
    current_secondary_attachments = ArrayField(models.IntegerField(default=0, blank=True),size=8, null=True)


    #ROW 1: PRIMARY WEAPONS
    #ROW 2: SECONDARY WEAPONS
    #ROW 3: PERK 1
    #ROW 4: PERK 2
    #ROW 5: PERK 3
    #ROW 6: LETHAL
    #ROW 7: TACTICAL
    #ROW 8: DEATHSTREAK
    unlocked_specs = ArrayField(
        ArrayField(
            models.IntegerField(default=0, blank=True),
            size=30
        ),
        size=10, null=True
    )

    #ROW 1: ROW K = PRIMARY WEAPON K, ATTACHMENTS
    #ROW 2: ROW K = SECONDARY WEAPON K, ATTACHMENTS
    unlocked_gunattachments = ArrayField(
        ArrayField(
            ArrayField(
                models.IntegerField(default=0, blank=True),
                size=30
            ),
            size=30, null=True
        ), 
        size=2, null=True
    )

    #ROW 1: ROW K = PRIMARY WEAPON K, CAMOS
    #ROW 2: ROW K = SECONDARY WEAPON K, CAMOS
    unlocked_guncamos = ArrayField(
        ArrayField(
            ArrayField(
                models.IntegerField(default=0, blank=True),
                size=100
            ),
            size=30, null=True
        ), 
        size=2, null=True
    )
    
    
    #Team A or B
    character = ArrayField(models.IntegerField(default=0, blank=True), size=12, null=True)
    
    

