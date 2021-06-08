from django.contrib import admin
from mainapp.models import *

# Register your models here.
admin.site.register(Klient)
admin.site.register(Pracownik)
admin.site.register(Produkt)
admin.site.register(Magazyn)
admin.site.register(Zamowienie)
admin.site.register(Zamowiony_Przedmiot)
admin.site.register(Faktura)
admin.site.register(Platnosc)
admin.site.register(Dostawa)
admin.site.register(Reklamacja)
