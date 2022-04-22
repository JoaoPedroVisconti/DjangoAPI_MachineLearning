from django.contrib import admin
from .models import Candidature

# Register your models here.


class CandidatureAdmin(admin.ModelAdmin):
  list_display = ('Gender', 'Married')


admin.site.register(Candidature, CandidatureAdmin)
