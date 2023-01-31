# Generated by Django 3.2.3 on 2021-05-31 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifier', '0002_alter_image_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='ans_class',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='image',
            name='score',
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]