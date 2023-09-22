# Generated by Django 4.2.5 on 2023-09-22 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('offer', models.FloatField()),
                ('funko', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.funko')),
            ],
            options={
                'ordering': ['offer'],
            },
        ),
    ]