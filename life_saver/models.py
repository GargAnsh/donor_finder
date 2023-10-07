from django.db import models

class BloodGroup(models.Model):
    blood_group_type = models.CharField(max_length=3)

    def __str__(self):
        return self.blood_group_type

    class Meta:
        db_table = 'db_blood_group'
        verbose_name = 'db_blood_group'  # Set the verbose name for the model

class DonorInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    dob = models.DateField()
    mobile_number = models.CharField(max_length=20)
    email = models.EmailField()
    blood_group = models.ForeignKey('life_saver.BloodGroup', on_delete=models.CASCADE)
    blood_group_donated = models.BooleanField(default=False)
    geo_location = models.CharField(max_length=100)
    donation_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'db_donor_info'
        verbose_name = 'db_donor_info'  # Set the verbose name for the model
