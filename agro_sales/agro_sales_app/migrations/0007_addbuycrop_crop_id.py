# Generated by Django 3.0 on 2023-05-25 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agro_sales_app', '0006_auto_20230525_0725'),
    ]

    operations = [
        migrations.AddField(
            model_name='addbuycrop',
            name='crop_id',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
