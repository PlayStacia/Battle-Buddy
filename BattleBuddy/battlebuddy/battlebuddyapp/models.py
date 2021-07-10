from django.db import models

# Create your models here.

#  acid, bludgeoning, cold, fire, force, lightning, necrotic, piercing, poison, psychic, radiant, slashing, and thunder.

class Boon(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class Affliction(models.Model): 
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class DamageType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ConditionType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class SpecialAbility(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class AttackMethod(models.Model):
    name = models.CharField(max_length=200)
    attack_damage = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Faction(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Statblock(models.Model):
    name = models.CharField(max_length=200)
    initiative_bonus = models.IntegerField()
    armor_class = models.IntegerField()
    hit_points = models.IntegerField()
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()
    xp = models.IntegerField()
    damage_vulnerabilities = models.ManyToManyField(
        DamageType, related_name='vulnerable_species', blank=True)
    damage_resistances = models.ManyToManyField(
        DamageType, related_name="resistant_species", blank=True)
    damage_immunities = models.ManyToManyField(
        DamageType, related_name="immune_species", blank=True)
    condition_immunities = models.ManyToManyField(
        ConditionType, related_name="immune_species", blank=True)
    attack_methods = models.ManyToManyField(
        AttackMethod, related_name="attack_methods", blank=True)
    special_abilities = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    details = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Participant(models.Model):
    statblock = models.ForeignKey(Statblock, on_delete=models.CASCADE, related_name="members" , null = True, blank = True)
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE, related_name="members" , null = True, blank = True)
    name = models.CharField(max_length=200)
    initiative=models.IntegerField()
    
    health = models.IntegerField()
    armour = models.IntegerField()
    boons =  models.ManyToManyField(Boon, related_name='booned', blank=True)
    afflictions = models.ManyToManyField(Affliction, related_name='afflictied', blank=True)
    hpchange = models.IntegerField()
    def __str__(self):
        return self.name

class Battle(models.Model):
    name = models.CharField(max_length=200)
    participants = models.ManyToManyField(Participant, related_name="battles")
    def __str__(self):
        return self.name

# dt = DamageType.objects.get(name='Fire')
# dt.statblocks_vulnerable.all()

# species = Species.objects.get(name='Bob')
# species.damage_vulnerabilities.all()
# pick a Battle
# all speciess in faction in battle

# class Battle(models.Model):
#     battle_name = models.charField(max_length=100)
#     description = models.TextField()


# stuff clipped from species model
 #  size=model.CharField(max_length=200)
    #  type=model.CharField(max_length=200)
    #  subtype=model.CharField(max_length=200)
    #  alignment=model.CharField(max_length=200)
    #  speed = models.IntegerField()
# senses = model.CharField(max_length=200)
#     languages = model.CharField(max_length=200)
# actions = models.ForeignKey(actions, on_delete=models.CASCADE)
#  proficiencies = models.ForeignKey(proficiencies, on_delete=models.CASCADE)
# special_abilities = model.CharField(max_length=200)
