        # iterate over the speciess for the faction
    # return a dictionary that contains a list of battles
    # each battle is a dictionary that contains a list of factions

    # each faction is a dictionary that contains a list of speciess
    # each statblock is a dictionary that contains other stats (name, strength, etc)


import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from battlebuddyapp.models import Statblock, Participant, Battle, Boon, Affliction


def battlebuddyapp(request):
 
    context = {}
    return render(request, 'battlebuddyapp/index.html', context)


def getbattles(request):
    # if request.method=="POST";:

        
    search = request.GET.get('search', '')
    page = request.GET.get('page', '1')
    page = int(page) if page.isdigit() else 1
    limit = request.GET.get('limit', '3')
    limit = int(limit) if limit.isdigit() else 3

    battles = Battle.objects.all()

    paginator = Paginator(battles, limit)
    if page > paginator.num_pages:
        battles = []
    else:
        battles = paginator.page(page)
            
    battles_data = []
    for battle in battles:
        # iterate over your factions for the battle
        battle_data = {'id': battle.id, 'name': battle.name, 'participants': []}

        for participant in battle.participants.all():
            # print(participant.name)
            # print(participant.statblock.name)
            participant_data = {
                "id":participant.id,
                "hpchange": participant.hpchange,
                "name": participant.name,
                "faction": participant.faction.name,
                "initiative":participant.initiative,
                "health": participant.statblock.hit_points,
                "boons" :[bonus.name for bonus in participant.boons.all()],
                "afflictions" : [aft.name for aft in participant.afflictions.all()],

                "statblock": {
                    "name": participant.statblock.name,
                    "armor_class": participant.statblock.armor_class,
                    "hit_points": participant.statblock.hit_points,
                    "xp": participant.statblock.xp,
                    "initiative_bonus":  participant.statblock.initiative_bonus,
                    
                    'damage_vulnerabilities': [dt.name for dt in participant.statblock.damage_vulnerabilities.all()],
                    
                    'damage_resistances': [dt.name for dt in participant.statblock.damage_resistances.all()],
                     
                    'damage_immunities': [dt.name for dt in participant.statblock.damage_immunities.all()],
                    
                    'condition_immunities': [dt.name for dt in participant.statblock.condition_immunities.all()],
                   
                    'attack_methods': [attack.name for attack in participant.statblock.attack_methods.all()],
                   
                    'special_abilities': participant.statblock.special_abilities,
                 
                    "notes": participant.statblock.notes,
                    },
                    

            }

            battle_data['participants'].append(participant_data)

        battles_data.append(battle_data)




    return JsonResponse({'battles': battles_data, 'total_pages': paginator.num_pages})



def savebattle(request):
    battle_data = json.loads(request.body)
    print(battle_data)
    battle = Battle.objects.get(id=battle_data['id'])
    battle.name = battle_data['name']
    # ...
    battle.save()
    return HttpResponse('ok')
    # battle = Battle(name=data['name'], participants = data[participants])
    # battle.save()

