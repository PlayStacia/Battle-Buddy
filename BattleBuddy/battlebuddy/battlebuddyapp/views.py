import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from battlebuddyapp.models import Statblock, Participant, Battle, Boon, Affliction
# from.forms import ParticipantForm


def battlebuddyapp(request):

    context = {}
    return render(request, 'battlebuddyapp/index.html', context)


def getbattles(request):

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
        battle_data = {'id': battle.id,
            'name': battle.name, 'participants': []}

        for participant in battle.participants.all():
            # print(participant.name)
            # print(participant.statblock.name)
            participant_data = {
                "id": participant.id,
                "hpchange": participant.hpchange,
                "name": participant.name,
                "faction": participant.faction.name,
                "initiative": participant.initiative,

                "health": participant.health,
                "boons": [boons.name for boons in participant.boons.all()],
                "afflictions": [aft.name for aft in participant.afflictions.all()],

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
    # print(json.dumps(battle_data, indent=4))
    battle = Battle.objects.get(id=battle_data['id'])
    # battle.name = battle_data['name']
    participants_data = battle_data['participants']  # list of dictionaries
    for participant_data in participants_data:  # dictionary
        participant = Participant.objects.get(id=participant_data['id'])
        participant.health = participant_data['health']
        participant.initiative = participant_data['initiative']

        # Remove all boons from the participant
        participant.boons.clear()
        # Iterate over the data received from the front end (list of strings)
        for boon_name in participant_data["boons"]:
        #    find the boon with given name
            boon = Boon.objects.get(name=boon_name)
            participant.boons.add(boon)
        #    add the boon to the participant's list of boons
      # Remove all boons from the participant
        participant.boons.clear()
        # Iterate over the data received from the front end (list of strings)
        for affliction_name in participant_data["afflictions"]:
        #    find the boon with given name
            affliction = Affliction.objects.get(name=affliction_name)
            participant.afflictions.add(affliction)
        #    add the boon to the participant's list of boons 
        participant.save()
    
    battle.save()
    return HttpResponse('ok')
   
