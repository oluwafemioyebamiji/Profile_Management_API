# Generated by Django 3.1.4 on 2020-12-28 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilestatus',
            name='status_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
