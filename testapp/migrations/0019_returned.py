# Generated by Django 4.2.1 on 2023-07-24 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0018_remove_home_ccheck_remove_home_cproposed_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Returned',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cName', models.CharField(blank=True, max_length=20)),
                ('cIllustrate', models.TextField(blank=True)),
                ('returnTo', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='details', to='testapp.home')),
            ],
        ),
    ]
