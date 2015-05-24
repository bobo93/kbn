# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Another',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Bucket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('buyerUsername', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tel', models.IntegerField()),
                ('numberOfRoomsMin', models.IntegerField()),
                ('numberOfRoomsMax', models.IntegerField()),
                ('city', models.CharField(max_length=200)),
                ('propertyDescription', models.CharField(max_length=2000)),
                ('numberOfBathrooms', models.IntegerField()),
                ('priceMax', models.IntegerField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('elevator', models.BooleanField()),
                ('balcony', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gardenSize', models.IntegerField()),
                ('numberOfBalcony', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LocalMy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=200)),
                ('numberOfRooms', models.IntegerField()),
                ('size', models.IntegerField()),
                ('equipment', models.CharField(max_length=200)),
                ('propertyDescription', models.CharField(max_length=2000)),
                ('parking', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('avaible', models.CharField(max_length=200)),
                ('offerStatus', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('local', models.ForeignKey(to='polls.LocalMy')),
                ('seller', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('elevator', models.BooleanField()),
                ('security', models.CharField(max_length=2000)),
                ('local', models.ForeignKey(to='polls.LocalMy')),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tel', models.IntegerField()),
                ('dateOfBirth', models.DateTimeField()),
                ('address', models.CharField(max_length=200)),
                ('accountNumber', models.IntegerField()),
                ('PESEL', models.IntegerField()),
                ('education', models.CharField(max_length=2000)),
                ('role', models.CharField(max_length=200)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.AddField(
            model_name='home',
            name='local',
            field=models.ForeignKey(to='polls.LocalMy'),
        ),
        migrations.AddField(
            model_name='flat',
            name='local',
            field=models.ForeignKey(to='polls.LocalMy'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='polls.Question'),
        ),
        migrations.AddField(
            model_name='bucket',
            name='offer',
            field=models.ForeignKey(to='polls.Offer'),
        ),
        migrations.AddField(
            model_name='another',
            name='local',
            field=models.ForeignKey(to='polls.LocalMy'),
        ),
    ]
