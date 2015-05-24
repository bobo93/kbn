from django.contrib import admin

from .models import *

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)


class OfferAdmin(admin.ModelAdmin):
    list_display=('name','local','seller','price','avaible')

admin.site.register(LocalMy)


admin.site.register(Personnel)
admin.site.register(Buyer)
admin.site.register(Bucket)
admin.site.register(Offer, OfferAdmin)

admin.site.register(Flat)
admin.site.register(Another)
admin.site.register(Office)
admin.site.register(Home)