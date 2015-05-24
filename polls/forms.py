from django import forms

from .models import *

class OfferForm(forms.ModelForm):

    class Meta:
        model = Offer
        fields = ('name', 'price',)




class BuyerForm(forms.ModelForm):

    class Meta:
        model = Buyer
        fields = ('tel','numberOfRoomsMin', 'numberOfRoomsMax', 'city', 'propertyDescription','numberOfBathrooms','priceMax')





class ContactForm(forms.Form):
 subject = forms.CharField(max_length=100)
 message = forms.CharField()
 sender = forms.EmailField()
 cc_myself = forms.BooleanField(required=False)



class ArticleForm(forms.Form):

    city = forms.CharField(label='Miasto',max_length=100, required=False)
    sizeMin=forms.IntegerField(label='Minimalna ilosc metrow', required=False,initial=0 )
    sizeMax=forms.IntegerField(label='Maksymalna ilosc metrow', required=False,initial=0)
    minRooms=forms.IntegerField(label='Minimalna liczba pokoi', required=False,initial=0 )
    maxRooms=forms.IntegerField(label='Maksymalna liczba pokoi', required=False,initial=0)
    priceMin=forms.IntegerField(label='Minimalna cena', required=False,initial=0 )
    priceMax=forms.IntegerField(label='Maksymalna cena', required=False,initial=0)
    elevator=forms.BooleanField(label='Winda',required=False)
    balcony=forms.BooleanField(label='Balkon',required=False)
    gardenSizeMin=forms.IntegerField(label='Minimalna liczba metrow ogrodu', required=False,initial=0 )
    gardenSizeMax=forms.IntegerField(label='Maksymalna liczba metrow ogrodu', required=False,initial=0)

