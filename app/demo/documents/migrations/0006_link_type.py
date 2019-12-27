# Generated by Django 3.0 on 2019-12-27 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0005_link_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='type',
            field=models.CharField(choices=[('choice1', 'Choice1'), ('choice2', 'Choice2'), ('choice3', 'Choice3'), ('choice4', 'Choice4'), ('choice5', 'Choice5')], max_length=64, null=True, verbose_name='Type'),
        ),
    ]
