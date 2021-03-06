# Generated by Django 2.2.6 on 2020-04-05 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MorseCombination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=1)),
                ('combination', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='ReceiveSentence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentence', models.CharField(max_length=100)),
                ('receive_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
