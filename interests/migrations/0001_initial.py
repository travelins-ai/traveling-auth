# Generated by Django 4.2.5 on 2023-09-28 01:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountInterests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest_type_key', models.CharField(choices=[('DESTINATION_TYPE', 'DESTINATION_TYPE'), ('TRAVEL_RHYTHM', 'TRAVEL_RHYTHM'), ('COMFORT_OR_BUDGET', 'COMFORT_OR_BUDGET'), ('RESTRICTION', 'RESTRICTION'), ('FOOD_PREFERENCE', 'FOOD_PREFERENCE'), ('REQUIREMENTS', 'REQUIREMENTS')], max_length=100)),
                ('interest_type_value', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'interests',
            },
        ),
    ]