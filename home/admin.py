from django.contrib import admin
from .models import News, VicePrincipal, Principal


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass

admin.site.register(VicePrincipal)
admin.site.register(Principal)
