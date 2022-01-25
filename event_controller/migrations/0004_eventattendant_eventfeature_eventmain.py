# Generated by Django 3.2.7 on 2022-01-25 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_alter_customuser_mobile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event_controller', '0003_auto_20220125_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('max_seat', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('address_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_address', to='user.addressglobal')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_events', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_name', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('eventmain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_features', to='event_controller.eventmain')),
            ],
        ),
        migrations.CreateModel(
            name='EventAttendant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('eventmain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_attenders', to='event_controller.eventmain')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_attendant', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
