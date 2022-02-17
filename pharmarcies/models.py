from django.db import models


# class PharmaciesMananger(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     whatsapp_contact = models.CharField(max_length=15)
#     phonenumbers = models.CharField(max_length=100)
#     class Meta:
#         verbose_name_plural  =  "Pharmacies Manangers" 

#     def __str__(self):
#         return self.first_name


class PharmaciesBranchDetails(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    whatsapp_contact = models.CharField(max_length=15)
    phonenumbers = models.CharField(max_length=100)
    #manager = models.ForeignKey(PharmaciesMananger,related_name="pharmacy_mananger",on_delete=models.CASCADE)

    class Meta: 
        verbose_name_plural  =  "Pharmacies Branch Details" 

    def __str__(self):
        return self.name