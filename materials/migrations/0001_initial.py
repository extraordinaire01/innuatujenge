# Generated by Django 2.2.10 on 2020-03-03 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_id', models.IntegerField()),
                ('item_name', models.CharField(max_length=200)),
                ('date_received', models.DateTimeField()),
                ('quantity', models.IntegerField()),
                ('item_unit', models.CharField(choices=[('kgs', 'Kilograms'), ('g', 'Grams'), ('bags', 'Bags'), ('lt', 'Liters')], default='kgs', max_length=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
