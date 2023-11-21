from django.contrib import admin
from allauth.account.models import EmailConfirmation

class EmailConfirmationAdmin(admin.ModelAdmin):
    list_display = ('email_address', 'created', 'sent', 'key_expired')
    search_fields = ('email_address__email',)
    
    def key_expired(self, obj):
        return obj.key_expired()

    key_expired.boolean = True
    key_expired.short_description = 'Key Expired'

admin.site.register(EmailConfirmation, EmailConfirmationAdmin)
