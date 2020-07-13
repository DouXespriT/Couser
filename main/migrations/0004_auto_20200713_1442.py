# Generated by Django 3.0.7 on 2020-07-13 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_auto_20200713_1431'),
    ]

    operations = [
        migrations.RenameField(
            model_name='popular_course',
            old_name='course_id',
            new_name='course',
        ),
        migrations.AddField(
            model_name='transaction',
            name='course',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.course'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='user',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]