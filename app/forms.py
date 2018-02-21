from django import forms

from .models import Room, RoomType, RoomAgree, Option

class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ('title',
        'created_date',
        'published_date',
        'deposit_ori',
        'rentfee_ori',
        'deposit_new',
        'rentfee_new',
        'manage_fee',
        'address',
        'date_start',
        'date_end',
        'room_type',
        'room_agree',
        'contact',
        'room_option',
        'university',
        'text',)
