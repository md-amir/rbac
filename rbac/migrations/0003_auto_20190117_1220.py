# Generated by Django 2.1.5 on 2019-01-17 06:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rbac', '0002_auto_20190116_0218'),
    ]

    operations = [
        migrations.CreateModel(
            name='RolePermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='permission',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='permission',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='role',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='role',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userrole',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rbac.Role'),
        ),
        migrations.AddField(
            model_name='userrole',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rolepermission',
            name='permission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rbac.Permission'),
        ),
        migrations.AddField(
            model_name='rolepermission',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rbac.Role'),
        ),
        migrations.AddField(
            model_name='role',
            name='permissions',
            field=models.ManyToManyField(related_name='role', through='rbac.RolePermission', to='rbac.Permission'),
        ),
        migrations.AddField(
            model_name='role',
            name='users',
            field=models.ManyToManyField(through='rbac.UserRole', to=settings.AUTH_USER_MODEL),
        ),
    ]
