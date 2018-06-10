from django import forms

from .models import Room, RoomType, RoomAgree, Option, RoomStatus


class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple' : True}))

class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ('title',
        'deposit',
        'rentfee',
        'fee_new',
        'manage_fee',
        'address',
        'date_start',
        'date_end',
        'room_type',
        'room_agree',
        'contact',
        'room_option',
        'door',
        'text',
        'room_status',)
        labels = {
        'title' : '제목',
        'deposit' : '보증금',
        'rentfee' : '월세',
        'fee_new' : '지원금',
        'manage_fee' : '관리비',
        'address' : '집주소',
        'date_start' : '계약시작일',
        'date_end' : '계약만기일',
        'room_type' : '방형태',
        'room_agree' : '집주인 동의',
        'contact' : '연락수단',
        'room_option' : '옵션',
        'door': '문',
        'text' : '기타 추가사항',
        'room_status' : '계약가능여부',
        }
        widgets = {
        'date_start' : forms.SelectDateWidget(years=('2018',)),
        'date_end' : forms.SelectDateWidget(years=('2018',)),
        }
