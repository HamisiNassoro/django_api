# Generated by Django 3.2.7 on 2022-01-25 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_alter_customuser_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
