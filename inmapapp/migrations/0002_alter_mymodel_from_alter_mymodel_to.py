# Generated by Django 4.0.3 on 2022-12-10 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmapapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='From',
            field=models.CharField(choices=[('bedroom1-2nd floor', 'bedroom1-2nd floor'), ('familyroom-2nd floor', 'familyroom-2nd floor'), ('bath-2nd floor', 'bath-2nd floor'), ('stairentry-2nd floor', 'stairentry-2nd floor'), ('empty-2nd floor', 'empty-2nd floor'), ('stairexit-2nd floor', 'stairexit-2nd floor'), ('bedroom3-2nd floor', 'bedroom3-2nd floor'), ('bedroom2-2nd floor', 'bedroom2-2nd floor'), ('bathroom-2nd floor', 'bathroom-2nd floor'), ('kitchen-1st floor', 'kitchen-1st floor'), ('bedroom1-1st floor', 'bedroom1-1st floor'), ('empty-1st floor', 'empty-1st floor'), ('bath-1st floor', 'bath-1st floor'), ('stairentry-1st floor', 'stairentry-1st floor'), ('bath2-1st floor', 'bath2-1st floor'), ('room-1st floor', 'room-1st floor'), ('stairexit-1st floor', 'stairexit-1st floor'), ('formaldinnning-1st floor', 'formaldinnning-1st floor'), ('office-1st floor', 'office-1st floor'), ('familyroom-1st floor', 'familyroom-1st floor'), ('exit-1st floor', 'exit-1st floor')], default='Hall', max_length=600),
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='To',
            field=models.CharField(choices=[('bedroom1-2nd floor', 'bedroom1-2nd floor'), ('familyroom-2nd floor', 'familyroom-2nd floor'), ('bath-2nd floor', 'bath-2nd floor'), ('stairentry-2nd floor', 'stairentry-2nd floor'), ('empty-2nd floor', 'empty-2nd floor'), ('stairexit-2nd floor', 'stairexit-2nd floor'), ('bedroom3-2nd floor', 'bedroom3-2nd floor'), ('bedroom2-2nd floor', 'bedroom2-2nd floor'), ('bathroom-2nd floor', 'bathroom-2nd floor'), ('kitchen-1st floor', 'kitchen-1st floor'), ('bedroom1-1st floor', 'bedroom1-1st floor'), ('empty-1st floor', 'empty-1st floor'), ('bath-1st floor', 'bath-1st floor'), ('stairentry-1st floor', 'stairentry-1st floor'), ('bath2-1st floor', 'bath2-1st floor'), ('room-1st floor', 'room-1st floor'), ('stairexit-1st floor', 'stairexit-1st floor'), ('formaldinnning-1st floor', 'formaldinnning-1st floor'), ('office-1st floor', 'office-1st floor'), ('familyroom-1st floor', 'familyroom-1st floor'), ('exit-1st floor', 'exit-1st floor')], default='Hall', max_length=600),
        ),
    ]
