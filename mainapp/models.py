from django.db import models


# Create your models here.

# class Adres(models.Model):
#     class Meta:
#         verbose_name_plural = 'Adres'
#     miasto = models.CharField(max_length=30)
#     kod_pocztowy = models.CharField(max_length=5)
#     ulica = models.CharField(max_length=30)
#     lokal = models.IntegerField()
#     kraj = models.CharField(max_length=30)

class Klient(models.Model):
    class Meta:
        verbose_name_plural = 'Klient'

    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    data_urodzenia = models.DateField()
    email = models.CharField(max_length=30)
    telefon = models.IntegerField()
    login = models.CharField(max_length=30)
    haslo = models.CharField(max_length=30)
    # adres = models.ForeignKey(Adres, on_delete=models.CASCADE)
    miasto = models.CharField(max_length=30)
    kod_pocztowy = models.CharField(max_length=6)
    ulica = models.CharField(max_length=30)
    lokal = models.IntegerField()
    kraj = models.CharField(max_length=30)


class Pracownik(models.Model):
    class Meta:
        verbose_name_plural = 'Pracownik'

    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    telefon = models.IntegerField()
    data_urodzenia = models.DateField()
    data_zatrudnienia = models.DateField()
    placa = models.FloatField()
    # adres = models.ForeignKey(Adres, on_delete=models.CASCADE)
    miasto = models.CharField(max_length=30)
    kod_pocztowy = models.CharField(max_length=6)
    ulica = models.CharField(max_length=30)
    lokal = models.IntegerField()
    kraj = models.CharField(max_length=30)


class Produkt(models.Model):
    class Meta:
        verbose_name_plural = "Produkt"

    DOSTEPNY = 'dostępny'
    NIEDOSTEPNY = 'niedostępny'
    ROCK = 'Rock'
    POP = 'POP'
    CLASSIC = 'Klasyka'
    RAP = 'Rap'
    JAZZ = 'Jazz'

    GATUNEK = [
        (ROCK, ('Rock')),
        (POP, ('Pop')),
        (CLASSIC, ('Muzyka Klasyczna')),
        (RAP, ('Rap')),
        (JAZZ, ('Jazz')),
    ]

    DOST = [
        (DOSTEPNY, ('Produkt dostępny')),
        (NIEDOSTEPNY, ('Produkt niedostępny')),
    ]

    nazwa_produktu = models.CharField(max_length=80)
    gatunek = models.CharField(max_length=30, choices=GATUNEK)
    opis_produktu = models.CharField(max_length=200)
    dostepnosc = models.CharField(max_length=30, choices=DOST)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    zdjecie = models.ImageField()
    isRecommended = models.BooleanField(default=False)


class Magazyn(models.Model):
    class Meta:
        verbose_name_plural = 'Magazyn'

    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE)
    ilosc = models.IntegerField()
    miejsce = models.CharField(max_length=50, blank=True)


class Zamowienie(models.Model):
    class Meta:
        verbose_name_plural = 'Zamówienie'

    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    pracownik = models.ForeignKey(Pracownik, on_delete=models.CASCADE)
    data_przyjecia = models.DateField()
    status = models.CharField(max_length=30)


class Zamowiony_Przedmiot(models.Model):
    class Meta:
        verbose_name_plural = 'Zamówiony przedmiot'

    zamowienie = models.ForeignKey(Zamowienie, on_delete=models.CASCADE)
    produkty = models.ForeignKey(Produkt, on_delete=models.CASCADE)
    ilosc = models.IntegerField()
    cena = models.FloatField()
    data_realizacji = models.DateField()


class Faktura(models.Model):
    class Meta:
        verbose_name_plural = 'Faktura'

    zamowienie = models.ForeignKey(Zamowienie, on_delete=models.CASCADE)
    data = models.DateField()


class Platnosc(models.Model):
    class Meta:
        verbose_name_plural = 'Płatność'

    UKONCZONA = 'ukończona'
    OCZEKUJE = 'oczekuje'
    STAT = [
        (UKONCZONA, ('Płatność zrealizowana')),
        (OCZEKUJE, ('Płatność oczekuje')),
    ]
    faktura = models.ForeignKey(Faktura, on_delete=models.CASCADE)
    sposobPlatnosci = models.CharField(max_length=30)
    status = models.CharField(max_length=30, choices=STAT)
    data = models.DateField()


class Dostawa(models.Model):
    class Meta:
        verbose_name_plural = 'Dostawa'

    zamowienie = models.ForeignKey(Zamowienie, on_delete=models.CASCADE)
    rodzaj = models.CharField(max_length=30)
    tracking_number = models.IntegerField()
    data = models.DateField()


class Reklamacja(models.Model):
    class Meta:
        verbose_name_plural = 'Reklamacja'

    zamowienie = models.ForeignKey(Zamowienie, on_delete=models.CASCADE)
    data = models.DateField()
    powod = models.CharField(max_length=30)
