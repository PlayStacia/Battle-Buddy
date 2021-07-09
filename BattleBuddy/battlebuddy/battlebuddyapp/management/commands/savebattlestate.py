from django.core.management.base import BaseCommand
from battlebuddyapp.models import Battle, Participant, Species
import string


# when do we save?

#     -open a new battle
#     -pause battle
#     -win battle

# # what can change
# #     initive
# #     health
#     status





# select battle

# find battle by Name

# feed battle into save function

# overwrite old data 

class Command(BaseCommand):
    participants= Battle.objects.all()
    def handle(self, *args, **options):
            
    for partcipant in partcipants:
        initive.partcipant=int(new_initive)
        partcipant.save()