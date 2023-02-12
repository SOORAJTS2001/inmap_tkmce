# Generated by Django 4.0.3 on 2022-06-16 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('From', models.CharField(choices=[('Hall', 'Hall'), ('Bedroom 1', 'Bedroom 1'), ('Bedroom 2', 'Bedroom 2'), ('Bedroom 3', 'Bedroom 3'), ('Master Bedroom', 'Master Bedroom'), ('Bath', 'Bath'), ('Sitting area', 'Sitting area'), ('W.I.C', 'W.I.C')], default='Hall', max_length=600)),
                ('To', models.CharField(choices=[('Hall', 'Hall'), ('Bedroom 1', 'Bedroom 1'), ('Bedroom 2', 'Bedroom 2'), ('Bedroom 3', 'Bedroom 3'), ('Master Bedroom', 'Master Bedroom'), ('Bath', 'Bath'), ('Sitting area', 'Sitting area'), ('W.I.C', 'W.I.C')], default='Hall', max_length=600)),
            ],
        ),
    ]