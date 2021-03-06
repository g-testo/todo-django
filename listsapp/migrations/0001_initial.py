# Generated by Django 3.2.8 on 2021-10-22 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('due_date', models.DateTimeField(verbose_name='due date')),
                ('is_complete', models.BooleanField()),
                ('list_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='listsapp.list')),
            ],
        ),
    ]
