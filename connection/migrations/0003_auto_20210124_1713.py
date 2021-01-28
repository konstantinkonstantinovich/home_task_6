# Generated by Django 3.1.4 on 2021-01-24 17:13
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connection', '0002_auto_20210124_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('email', models.EmailField(
                    max_length=200, unique=True)),
                ('first_name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['first_name'],
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('country', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE,
                    primary_key=True, serialize=False,
                    to='connection.country')),
                ('city_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('citizen', models.ManyToManyField(
                    to='connection.Citizen')),
            ],
        ),
        migrations.RemoveField(
            model_name='quote',
            name='author',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Quote',
        ),
        migrations.AddField(
            model_name='citizen',
            name='city',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='connection.city'),
        ),
    ]
