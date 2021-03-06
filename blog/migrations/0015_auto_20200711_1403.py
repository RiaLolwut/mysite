# Generated by Django 3.0.8 on 2020-07-11 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('blog', '0014_auto_20200711_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='hero_heading',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='hero_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
