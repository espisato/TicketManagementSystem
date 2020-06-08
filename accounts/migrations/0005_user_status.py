# Generated by Django 2.2.10 on 2020-06-06 13:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('V', 'Verified'), ('U', 'Unverified')], default=django.utils.timezone.now, max_length=1),
            preserve_default=False,
        ),
    ]