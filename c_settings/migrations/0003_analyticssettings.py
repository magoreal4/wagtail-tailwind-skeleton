# Generated by Django 4.0.4 on 2022-05-22 16:13

import c_settings.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('c_settings', '0002_social'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalyticsSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ga_tracking_id', models.CharField(blank=True, help_text='Your Google "Universal Analytics" tracking ID (begins with "UA-")', max_length=255, verbose_name='UA Tracking ID')),
                ('ga_g_tracking_id', models.CharField(blank=True, help_text='Your Google Analytics 4 tracking ID (begins with "G-")', max_length=255, verbose_name='G Tracking ID')),
                ('ga_track_button_clicks', models.BooleanField(default=False, help_text='Track all button clicks using Google Analytics event tracking. Event tracking details can be specified in each button’s advanced settings options.', verbose_name='Track button clicks')),
                ('gtm_id', models.CharField(blank=True, help_text='Begins with "GTM-"', max_length=255, verbose_name='Google Tag Manager ID')),
                ('head_scripts', c_settings.fields.MonospaceField(blank=True, help_text='Add tracking scripts between the <head> tags.', null=True, verbose_name='<head> tracking scripts')),
                ('body_scripts', c_settings.fields.MonospaceField(blank=True, help_text='Add tracking scripts toward closing <body> tag.', null=True, verbose_name='<body> tracking scripts')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'verbose_name': 'Tracking',
            },
        ),
    ]
