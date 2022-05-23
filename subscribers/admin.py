from .models import Subscribers

from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register
)

class SubscriberAdmin(ModelAdmin):

    model = Subscribers
    menu_label = "Subscriptores"
    menu_icon = "user"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("email", "full_name")
    search_fields = ("email", "full_name")

modeladmin_register(SubscriberAdmin)