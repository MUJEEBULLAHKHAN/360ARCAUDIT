# Generated by Django 4.1.7 on 2023-02-27 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_uploadedimage_remove_arcinfo_title_arcinfo_wi2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arcinfo',
            name='wi6',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]