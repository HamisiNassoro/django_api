# Generated by Django 3.2.7 on 2022-01-25 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_remove_customuser_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]