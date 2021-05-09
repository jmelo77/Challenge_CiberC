from django import forms
from django.db.utils import IntegrityError
from inventory.models import Inventory, UploadFile
from datetime import datetime
from pyxlsb import open_workbook

class UploadFileForm(forms.ModelForm):

    class Meta:
        model = UploadFile
        fields = ('name', 'file_path',)

    def summary_json(self):
        totprice = 0
        elem = 0
        counter = 0
        work_book = open_workbook(self.cleaned_data['file_path'].file)
        with work_book.get_sheet(1) as leaf:

            for row in leaf.rows():
                if (isinstance(row[0].v, str) and isinstance(row[1].v, (float, int)) and isinstance(row[2].v, (float, int))):
                    serial_number = row[0].v
                    quantity = int(row[1].v)
                    price = row[2].v
                    try:
                        Inventory.objects.create(serial_number=serial_number, quantity=quantity, price=price)
                        totprice += price
                        elem += quantity
                        counter += 1
                    except IntegrityError:
                        Inventory.objects.filter(serial_number=serial_number).update(quantity=quantity, price=price)
                        totprice += price
                        elem += quantity
                        counter += 1
                    except Exception as e:
                        print('ERROR', str(e))

        return {'elements': elem, 'averagePrice': totprice / counter}