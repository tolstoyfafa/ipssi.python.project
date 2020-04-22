from django.contrib import admin
from django.contrib.admin import StackedInline
from django.utils.translation import gettext_lazy as _
from .models import Ad, User, Category, Address
from datetime import *
from dateutil.relativedelta import relativedelta


class AdInline(StackedInline):
    model = Ad
    verbose_name_plural = _('Ads')
    show_change_link = True
    extra = 0


class AddressInline(StackedInline):
    model = Ad
    verbose_name_plural = _('Address')
    show_change_link = True
    extra = 0


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', '_calculate_age', '_name', '_fulladr',
                    'phone', 'updated', 'created')
    readonly_fields = ('created', 'updated')
    search_fields = ('email', )
    list_display_links = ['email']
    ordering = ('created',)
    inlines = [
        AdInline,
        AddressInline
    ]

    def _name(self, obj):
        output = ' {}. {}'.format(
            obj.first_name[1],
            obj.last_name,
        )
        return output

    from datetime import date

    def _calculate_age(self, obj):
        if obj.birth_date:
            myday = obj.birth_date
            diff = relativedelta(datetime.now(), myday)
            print(diff)
            return diff.years

    def _fulladr(self, obj):
        output = ' {}. {}'.format(
            obj.address
        )
        return output


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'type', 'status', 'updated', 'created')
    readonly_fields = ('created', 'updated')
    list_filter = ('user', 'category', 'type', 'status')
    search_fields = ('title', 'description')
    list_display_links = ['user', 'title']
    ordering = ('created',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('address1', 'address2', 'postal_code',
                    'city', 'country', 'latitude', 'longitude', 'user')
    readonly_fields = ('user',)
    list_filter = ('postal_code',)
    search_fields = ('postal_code',)
    list_display_links = ('user',)
    ordering = ('created',)


""" @admin.register(Ad)
class MissionAdmin(admin.ModelAdmin):
    list_display = ('customer', 'ad', 'created', 'updated')
    readonly_fields = ('created', 'updated', 'user')
    list_filter = ('postal_code', 'category', 'type', 'status')
    search_fields = ('postal_code',)
    list_display_links = ['user', 'title']
    ordering = ('created',) """


admin.site.register(Category)
