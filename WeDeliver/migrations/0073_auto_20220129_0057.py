# Generated by Django 3.2.4 on 2022-01-28 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeDeliver', '0072_auto_20220128_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email_verification',
            field=models.CharField(choices=[('V', 'Verified'), ('NV', 'Not Verified')], default='NV', max_length=2),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_no_verification',
            field=models.CharField(choices=[('V', 'Verified'), ('NV', 'Not Verified')], default='NV', max_length=2),
        ),
    ]
