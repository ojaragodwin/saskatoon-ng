# Generated by Django 3.2.5 on 2021-07-26 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20210601_0342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='neighborhood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.neighborhood', verbose_name='Neighborhood'),
        ),
    ]