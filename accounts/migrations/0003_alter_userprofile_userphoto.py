# Generated by Django 3.2.6 on 2021-08-11 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_userprofile_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='userphoto',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile'),
        ),
    ]