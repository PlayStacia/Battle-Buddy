# from battlebuddy.battlebuddyapp.models import Battle, Participant
# from django.forms import ModelForm
# from django.forms import inlineformset_factory


# # class BattleForm(forms.ModelForm):
# #     class Meta:
# #         model = Battle
# #         fields = '__all__'

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = (initiative,health,armour,boons,afflictions)