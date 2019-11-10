from django.contrib import admin

from . models import *

class AgentAdmin(admin.ModelAdmin):
    list_display = ("user","avatar","organisation")
    list_filter = ("user","organisation")
    ordering = ("user","organisation")
    search_field = ("user","organisation")

class AssuranceAdmin(admin.ModelAdmin):
    list_display = ("no_police","montant","debut", "materiel", "fin","client")
    list_filter = ("no_police","montant","debut", "materiel", "fin","client")
    ordering = ("no_police","montant","debut", "materiel", "fin","client")
    search_field = ("no_police","montant","debut", "materiel", "fin","client")

class MaterielRoulantAdmin(admin.ModelAdmin):
    list_display = ("nom","plaque","chassis", 'roues')
    list_filter = ("nom","plaque","chassis", 'roues')
    ordering = ("nom","plaque","chassis", 'roues')
    search_field = ("nom","plaque","chassis", 'roues')

class OrganisationAdmin(admin.ModelAdmin):
    list_display = ("titre", "sigle")
    list_filter = ("titre", "sigle")
    ordering = ("titre", "sigle")
    search_field = ("titre", "sigle")

class ClientAdmin(admin.ModelAdmin):
    list_display = ("nom", "prenom", "CNI", "tel", "email", "depuis")
    list_filter = ("nom", "prenom", "CNI", "depuis")
    ordering = ("nom", "prenom", "CNI", "depuis")
    search_field = ("nom", "prenom", "CNI", "depuis")

admin.site.register(Agent, AgentAdmin)
admin.site.register(Assurance, AssuranceAdmin)
admin.site.register(MaterielRoulant, MaterielRoulantAdmin)
admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(Client, ClientAdmin)