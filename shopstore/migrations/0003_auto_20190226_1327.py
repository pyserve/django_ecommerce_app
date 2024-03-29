# Generated by Django 2.1.7 on 2019-02-26 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopstore', '0002_item_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(blank=True, default=0)),
                ('datetime', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='transaction',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopstore.Item'),
        ),
    ]
