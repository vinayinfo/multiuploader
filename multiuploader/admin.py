from django.contrib import admin
from multiuploader.models import MultiuploaderFile


class MultiuploaderAdmin(admin.ModelAdmin):
    search_fields = ["filename", "key_data"]
    list_display = ["filename", "upload_date", "file"]


admin.site.register(MultiuploaderFile, MultiuploaderAdmin)
