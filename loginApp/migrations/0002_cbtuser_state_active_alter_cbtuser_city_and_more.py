# Generated by Django 5.0.6 on 2024-05-09 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cbtuser',
            name='state_active',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='cbtuser',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='cbtuser',
            name='gender',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='cbtuser',
            name='password',
            field=models.CharField(max_length=255, null=True),
        ),
    ]