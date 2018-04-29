# Generated by Django 2.0.4 on 2018-04-24 04:42

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IOSApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=56)),
                ('platform', models.CharField(max_length=10)),
                ('minimum_os_version', models.CharField(max_length=4)),
                ('store_id', models.IntegerField(unique=True)),
                ('currency', models.CharField(max_length=4)),
                ('content_advistory_rating', models.CharField(max_length=4)),
                ('category_ids', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('category_names', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=24), size=None)),
                ('supported_devices', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=36), size=None)),
                ('language_codes', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=4), size=None)),
                ('icon_100', models.ImageField(height_field=100, upload_to='', width_field=100)),
                ('icon_512', models.ImageField(height_field=512, upload_to='', width_field=512)),
                ('bundle_id', models.CharField(max_length=120)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='IOSAppObservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
                ('overall_average_rating', models.FloatField()),
                ('current_version_average_rating', models.FloatField()),
                ('current_version_release_date', models.DateField()),
                ('release_notes', models.TextField()),
                ('results', models.IntegerField()),
                ('ranking', models.IntegerField()),
                ('screenshot_urls', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), size=None)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ios_app_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scrapers.IOSApp')),
            ],
        ),
        migrations.CreateModel(
            name='IOSCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('app_store_id', models.IntegerField(unique=True)),
                ('parent_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scrapers.IOSCategory')),
            ],
        ),
        migrations.CreateModel(
            name='IOSDeveloper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_store_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=250)),
                ('store_url', models.CharField(max_length=250)),
                ('site_url', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='IOSKeywordObservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('popularity', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=250, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='ioskeywordobservation',
            name='keyword_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scrapers.Keyword'),
        ),
        migrations.AddField(
            model_name='iosappobservation',
            name='keyword_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scrapers.Keyword'),
        ),
        migrations.AddField(
            model_name='iosapp',
            name='developer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scrapers.IOSDeveloper'),
        ),
        migrations.AlterUniqueTogether(
            name='iosappobservation',
            unique_together={('created', 'ios_app_id')},
        ),
    ]
