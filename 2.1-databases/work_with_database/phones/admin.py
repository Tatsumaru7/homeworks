from django.contrib import admin
from .models import Phone
from import_export import resources
from import_export.fields import Field
from import_export.admin import ImportExportModelAdmin

# класс обработки данных
class PhoneResource(resources.ModelResource):

    id = Field(attribute='id')
    name = Field(attribute='name')
    price = Field(attribute='price')
    image = Field(attribute='image')
    release_date = Field(attribute='release_date')
    lte_exists = Field(attribute='lte_exists')
    slug = Field(attribute='slug')

    class Meta:
        model = Phone

# вывод данных на странице
@admin.register(Phone)
class PhoneAdmin(ImportExportModelAdmin):
    resource_class = PhoneResource

# admin.site.register(Phone, PhoneAdmin)