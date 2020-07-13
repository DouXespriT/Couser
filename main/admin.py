from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.course)
admin.site.register(models.course_level)
admin.site.register(models.popular_course)
admin.site.register(models.transaction_table)
admin.site.register(models.email_subscribe)
admin.site.register(models.contact_message)