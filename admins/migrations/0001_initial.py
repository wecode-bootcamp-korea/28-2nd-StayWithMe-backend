# Generated by Django 3.2.5 on 2022-01-11 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=30)),
                ('admin_id', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'admins',
            },
        ),
    ]