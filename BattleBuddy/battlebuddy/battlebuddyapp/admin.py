from django.contrib import admin

# Register your models here.
from .models import Statblock, DamageType, ConditionType, Participant, SpecialAbility, AttackMethod, Faction, Battle, Affliction, Boon

admin.site.register(DamageType)
admin.site.register(ConditionType)
admin.site.register(SpecialAbility)
admin.site.register(AttackMethod)
admin.site.register(Boon)
admin.site.register(Affliction)
admin.site.register(Faction)
admin.site.register(Battle)
admin.site.register(Statblock)
admin.site.register(Participant)