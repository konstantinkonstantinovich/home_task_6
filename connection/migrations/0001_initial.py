# Generated by Django 3.1.4 on 2021-01-18 16:37
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False,
                                        verbose_name='ID')),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('first_name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['first_name'],
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('population', models.IntegerField(default=10)),
                ('name_of_country', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('country', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE,
                    primary_key=True,
                    serialize=False, to='connection.country')),
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
                    to='connection.Citizen', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='citizen',
            name='city',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='connection.city'),
        ),
    ]
