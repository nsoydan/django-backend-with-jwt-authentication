from email.policy import default
from django.db import models

# Create your models here.


class Firma(models.Model):
    id=models.AutoField(primary_key=True)
    firmaAdi=models.CharField(max_length=200,null=True,blank=True)
    firmaNo=models.CharField(max_length=200,null=True,blank=True)
    firmaAdresi=models.CharField(max_length=500,null=True,blank=True)
    firmaTel=models.CharField(max_length=50,null=True,blank=True)
    firmaYetkilisi=models.CharField(max_length=50,null=True,blank=True)
    firmaEnlem=models.FloatField(null=True,blank=True)
    firmaBoylam=models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.firmaAdi


class Bakim_List(models.Model):
    id=models.AutoField(primary_key=True)
    bakimKayitTarihSaat=models.DateTimeField(auto_now_add=True)
    ilkfoto=models.ImageField(null=True,blank=True, upload_to='bakimOnarim/ilkfoto/%Y/%m/%d/')
    sonFoto=models.ImageField(null=True,blank=True, upload_to='bakimOnarim/sonFoto/%Y/%m/%d/')
    talepAciklama=models.CharField(max_length=500,null=True,blank=True)
    isAciklama=models.CharField(max_length=500,null=True,blank=True)
    isBaslamaTarihi=models.DateField(null=True,blank=True)
    isBitisTarihi=models.DateField(null=True,blank=True)
    cikisKm=models.IntegerField(null=True,blank=True)
    gelisKm=models.IntegerField(null=True,blank=True)
    durum=models.BooleanField(default=False)
    kullanilanMalzemeler=models.CharField(max_length=250,null=True,blank=True)
    talepEden=models.CharField(max_length=50,null=True)
    isiYapan=models.CharField(max_length=50,null=True)
    sehir=models.CharField(max_length=50,null=True)
    tutanak=models.ImageField(null=True,blank=True, upload_to='bakimOnarim/tutanak/%Y/%m/%d/')
    firma=models.ForeignKey(Firma,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.firma.firmaAdi
