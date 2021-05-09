from django.db import models
from django.core.validators import FileExtensionValidator


class Inventory(models.Model):

    serial_number = models.CharField(max_length=20, unique=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.serial_number


class UploadFile(models.Model):

    name = models.CharField(max_length=40, help_text = "Please enter a file name")
    date = models.DateTimeField(auto_now=True)
    file_path = models.FileField(upload_to='upload/', validators=[FileExtensionValidator(allowed_extensions=('xlsb',))])
    summary = models.CharField(max_length=120)

    def __str__(self):
        return self.file_path