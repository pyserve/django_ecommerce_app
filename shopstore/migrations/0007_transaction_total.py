# Generated by Django 2.1.7 on 2019-02-26 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopstore', '0006_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='total',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]