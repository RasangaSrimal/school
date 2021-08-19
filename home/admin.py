from django.contrib import admin
from .models import News, VicePrincipal 


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass

admin.site.register(VicePrincipal)
