# Generated by Django 2.0.2 on 2018-02-07 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='email',
            field=models.EmailField(max_length=300, null=True),
        ),
    ]
