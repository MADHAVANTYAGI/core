# Generated by Django 3.2.5 on 2021-07-29 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_alter_quesmcq_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quesmcq',
            name='answer',
            field=models.CharField(choices=[('option_1', 'option 1'), ('option_2', 'option 2'), ('option_3', 'option 3'), ('option_4', 'option 4')], max_length=50),
        ),
    ]