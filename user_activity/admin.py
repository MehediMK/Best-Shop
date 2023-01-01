from django.contrib import admin
from user_activity.models import EmailSubscription, Newsletter, FAQ, TermsCondition, StoreInfo

admin.site.register(EmailSubscription)
admin.site.register(Newsletter)
admin.site.register(StoreInfo)


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'status']
    search_fields = ('title', 'description', 'status')
    list_editable = ['status']
    list_display_links = ['pk', 'title']


@admin.register(TermsCondition)
class TermsConditionAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'status']
    search_fields = ('title', 'description', 'status')
    list_editable = ['status']
    list_display_links = ['pk', 'title']
