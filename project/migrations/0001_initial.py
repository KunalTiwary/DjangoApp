# Generated by Django 2.0.7 on 2023-03-17 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articleTitle', models.CharField(max_length=100)),
                ('targetLanguage', models.CharField(max_length=100)),
            ],
        ),
    ]