from django.contrib import admin
from .models import CommandsModel

@admin.register(CommandsModel)
class CommandsModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'wbmode', 'saturation', 'sensor_id', 'exposuretime', 'gain', 'ispdigitalgain', 'tnr_mode', 'ee_mode', 'aeantibanding', 'exposurecompensation', 'aelock', 'awblock')
    list_filter = ('wbmode', 'tnr_mode', 'ee_mode', 'aeantibanding')
    search_fields = ('wbmode', 'sensor_id')
    list_per_page = 20  # Number of items displayed per page in the admin list view

# You can optionally customize the admin site header and title
admin.site.site_header = 'Custom Admin Panel Header'
admin.site.site_title = 'Custom Admin Panel Title'

# Optionally, you can also unregister the default Group and User models
# from the admin panel if you want to provide a more specific admin interface.
# For example:
# from django.contrib.auth.models import User, Group
# admin.site.unregister(User)
# admin.site.unregister(Group)
