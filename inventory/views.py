from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, ListView
from inventory.models import Inventory, UploadFile
from inventory.forms import UploadFileForm
import json


class InventoryListView(ListView):

    context_object_name = 'view_inventory'
    queryset = Inventory.objects.all()
    template_name = 'view_inventory.html'


class UploadFileListView(ListView):

    context_object_name = 'view_uploadfile'
    queryset = UploadFile.objects.all()
    template_name = 'view_uploadfile.html'


class UploadFileView(FormView):

    template_name = 'uploadfile.html'
    form_class = UploadFileForm
    success_url = '/uploadfile/'

    def form_valid(self, form):

        summary_format_json = form.summary_json()
        saved_instance = form.save()
        saved_instance.summary = json.dumps(summary_format_json)
        saved_instance.save()
        return super().form_valid(form)