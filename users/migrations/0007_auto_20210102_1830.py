# Generated by Django 2.2.5 on 2021-01-02 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210102_1818'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email_verify',
            new_name='email_verified',
        ),
    ]
