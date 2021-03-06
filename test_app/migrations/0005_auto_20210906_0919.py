# Generated by Django 3.2.6 on 2021-09-06 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0004_auto_20210903_0850'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testmodel',
            options={'ordering': ('-created_at',), 'verbose_name_plural': 'Test Model'},
        ),
        migrations.CreateModel(
            name='ModelX',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mileage', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('test_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_content', to='test_app.testmodel')),
            ],
            options={
                'verbose_name_plural': 'ModelX',
                'ordering': ('-created_at',),
            },
        ),
    ]
