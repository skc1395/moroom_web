from django import forms

from .models import Room, RoomType, RoomAgree, Option

class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ('title', 'text', 'deposit_ori', 'rentfee_ori', 'deposit_new', 'rentfee_new', 'manage_fee', 'date_start', 'date_end', 'room_type', 'room_agree', 'contact', 'room_option',)
