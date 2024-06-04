# Generated by Django 5.0.6 on 2024-05-09 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cbtUser',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.CharField(default='', max_length=255, unique=True)),
                ('phone', models.CharField(default='', max_length=255, unique=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'cbt_user',
            },
        ),
    ]
