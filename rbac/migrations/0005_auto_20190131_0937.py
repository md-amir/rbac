# Generated by Django 2.1.5 on 2019-01-31 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0004_userrole_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='name',
            field=models.CharField(default='', max_length=50, null=''),
        ),
    ]