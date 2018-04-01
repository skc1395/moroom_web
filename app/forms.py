from django import forms

from .models import Room, RoomType, RoomAgree, Option, RoomStatus


class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple' : True}))

class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ('title',
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
        'text',
        'room_status',)
        labels = {
        'title' : '제목',
        'deposit_ori' : '기존 보증금',
        'rentfee_ori' : '기존 월세',
        'deposit_new' : '보증금',
        'rentfee_new' : '월세',
        'manage_fee' : '관리비',
        'address' : '집주소',
        'date_start' : '계약시작일',
        'date_end' : '계약만기일',
        'room_type' : '방형태',
        'room_agree' : '집주인 동의',
        'contact' : '연락수단',
        'room_option' : '옵션',
        'university' : '학교',
        'text' : '기타 추가사항',
        'room_status' : '계약가능여부',
        }
        widgets = {
        'date_start' : forms.SelectDateWidget(years=('2018',)),
        'date_end' : forms.SelectDateWidget(years=('2018',)),
        }
