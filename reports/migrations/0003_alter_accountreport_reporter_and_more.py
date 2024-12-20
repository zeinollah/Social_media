# Generated by Django 4.2 on 2024-11-28 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reports', '0002_alter_accountreport_options_alter_postreport_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountreport',
            name='reporter',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='reporter_reports', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='postreport',
            name='reporter',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='author_reports', to=settings.AUTH_USER_MODEL),
        ),
    ]
