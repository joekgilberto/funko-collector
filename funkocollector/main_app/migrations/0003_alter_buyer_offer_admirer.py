# Generated by Django 4.2.5 on 2023-09-22 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_buyer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='offer',
            field=models.FloatField(default=0.0),
        ),
        migrations.CreateModel(
            name='Admirer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('funkos', models.ManyToManyField(to='main_app.funko')),
            ],
        ),
    ]