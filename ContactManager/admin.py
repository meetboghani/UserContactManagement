from django.contrib import admin
from  .models import Profile,usersave,Contact,SaveContact
# Register your models here.

admin.site.register(Profile)
admin.site.register(usersave)
admin.site.register(SaveContact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'client_email', 'contact_date')
    list_display_links = ('id', 'client_name')
    search_feilds = ('client_name', 'client_email')
    list_per_page = 20


admin.site.register(Contact, ContactAdmin)
