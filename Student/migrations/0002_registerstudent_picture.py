# Generated by Django 3.0.6 on 2020-07-03 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registerstudent',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/pictures'),
        ),
    ]