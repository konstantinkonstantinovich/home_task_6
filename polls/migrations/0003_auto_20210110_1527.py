# Generated by Django 3.1.4 on 2021-01-10 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_myperson'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=250)),
                ('method', models.CharField(max_length=250)),
                ('timestamps', models.DateTimeField(auto_now_add=False)),
            ],
        ),
    ]
