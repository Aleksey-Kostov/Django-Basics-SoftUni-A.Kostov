# Generated by Django 5.1.2 on 2024-10-22 16:59

import django.core.validators
import django.db.models.deletion
import regular_exam_2024_feb.car.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profile_car', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Rally', 'Rally'), ('Open-wheel', 'Open-wheel'), ('Kart', 'Kart'), ('Drag', 'Drag'), ('Other', 'Other')], max_length=10)),
                ('model', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(1)])),
                ('year', models.IntegerField(validators=[regular_exam_2024_feb.car.validators.YearValidator()])),
                ('image_url', models.URLField(error_messages={'unique': 'This image URL is already in use! Provide a new one.'}, help_text='https://...', unique=True)),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(1.0)])),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='profile_car.profile')),
            ],
        ),
    ]
