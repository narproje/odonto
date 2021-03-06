# Generated by Django 2.0.13 on 2020-11-09 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('odonto', '0051_auto_20201109_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casemix',
            name='ability_to_communicate',
            field=models.CharField(choices=[('0', '0'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=256, null=True, verbose_name='Ability to communicate'),
        ),
        migrations.AlterField(
            model_name='casemix',
            name='ability_to_cooperate',
            field=models.CharField(choices=[('0', '0'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=256, null=True, verbose_name='Ability to co-operate'),
        ),
        migrations.AlterField(
            model_name='casemix',
            name='access_to_oral_care',
            field=models.CharField(choices=[('0', '0'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=256, null=True, verbose_name='Access to oral care'),
        ),
        migrations.AlterField(
            model_name='casemix',
            name='legal_and_ethical_barriers_to_care',
            field=models.CharField(choices=[('0', '0'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=256, null=True, verbose_name='Legal and ethical barriers to care'),
        ),
        migrations.AlterField(
            model_name='casemix',
            name='medical_status',
            field=models.CharField(choices=[('0', '0'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=256, null=True, verbose_name='Medical status'),
        ),
        migrations.AlterField(
            model_name='casemix',
            name='oral_risk_factors',
            field=models.CharField(choices=[('0', '0'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=256, null=True, verbose_name='Oral risk factors'),
        ),
    ]
