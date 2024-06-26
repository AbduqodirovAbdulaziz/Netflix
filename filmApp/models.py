from django.db import models


class Aktyor(models.Model):
    ism = models.CharField(max_length=100)
    t_sana = models.DateField(blank=True, null=True)
    davlat = models.CharField(max_length=50)
    jins = models.CharField(max_length=10)

    def __str__(self):
        return self.ism


class Kino(models.Model):
    nom = models.CharField(max_length=255)
    janr = models.CharField(max_length=50)
    yil = models.CharField(max_length=4)

    def __str__(self):
        return self.nom


class KinoAktyor(models.Model):
    kino = models.ForeignKey(Kino, on_delete=models.CASCADE)
    aktyor = models.ForeignKey(Aktyor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.kino.nom}:{self.aktyor}"


class Tarif(models.Model):
    nom = models.CharField(max_length=255)
    davomiyligi = models.CharField(max_length=20)
    narx = models.PositiveIntegerField()

    def __str__(self):
        return self.nom
