# Generated by Django 3.2.4 on 2022-02-14 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeDeliver', '0073_auto_20220129_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_no',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
