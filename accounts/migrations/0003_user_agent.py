# Generated by Django 2.2.10 on 2020-06-05 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Agent',
            field=models.BooleanField(default=False),
        ),
    ]