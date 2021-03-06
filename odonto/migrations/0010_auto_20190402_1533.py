# Generated by Django 2.0.9 on 2019-04-02 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('odonto', '0009_auto_20190329_1101'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fp17exemptions',
            options={'verbose_name': 'Exemptions and remissions'},
        ),
        migrations.AlterModelOptions(
            name='fp17treatmentcategory',
            options={'verbose_name': 'Treatment category'},
        ),
        migrations.RemoveField(
            model_name='fp17treatmentcategory',
            name='treatment_category_band_1',
        ),
        migrations.RemoveField(
            model_name='fp17treatmentcategory',
            name='treatment_category_band_2',
        ),
        migrations.RemoveField(
            model_name='fp17treatmentcategory',
            name='treatment_category_band_3',
        ),
        migrations.AddField(
            model_name='fp17treatmentcategory',
            name='treatment_category',
            field=models.CharField(blank=True, choices=[('Band 1', 'Band 1'), ('Band 2', 'Band 2'), ('Band 3', 'Band 3')], max_length=255, null=True, verbose_name='Treatment category'),
        ),
        migrations.AlterField(
            model_name='fp17exemptions',
            name='aged_18_in_full_time_education',
            field=models.BooleanField(default=False, verbose_name='Aged 18 in full time education'),
        ),
        migrations.AlterField(
            model_name='fp17exemptions',
            name='evidence_of_exception_or_remission_seen',
            field=models.BooleanField(default=False, verbose_name='Evidence of exception or remission seen'),
        ),
        migrations.AlterField(
            model_name='fp17exemptions',
            name='expectant_mother',
            field=models.BooleanField(default=False, verbose_name='Expectant mother'),
        ),
        migrations.AlterField(
            model_name='fp17exemptions',
            name='full_remission_hc2_cert',
            field=models.BooleanField(default=False, verbose_name='Full remission - HC2 cert.'),
        ),
        migrations.AlterField(
            model_name='fp17exemptions',
            name='income_based_jobseekers_allowance',
            field=models.BooleanField(default=False, verbose_name='Income based jobseekers allowance'),
        ),
        migrations.AlterField(
            model_name='fp17exemptions',
            name='income_related_employment_and_support_allowance',
            field=models.BooleanField(default=False, verbose_name='Income related employment and support allowance'),
        ),
        migrations.AlterField(
            model_name='fp17exemptions',
            name='income_support',
            field=models.BooleanField(default=False, verbose_name='Income support'),
        ),
        migrations.AlterField(
            model_name='fp17exemptions',
            name='nhs_tax_credit_exemption',
            field=models.BooleanField(default=False, verbose_name='NHS tax credit exemption'),
        ),
        migrations.AlterField(
            model_name='fp17exemptions',
            name='nursing_mother',
            field=models.BooleanField(default=False, verbose_name='Nursing mother'),
        ),
        migrations.AlterField(
            model_name='fp17exemptions',
            name='partial_remission_hc3_cert',
            field=models.BooleanField(default=False, verbose_name='Partial remission - HC3 cert.'),
        ),
        migrations.AlterField(
            model_name='fp17exemptions',
            name='patient_charge_collected',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Patient charge collected'),
        ),
        migrations.AlterField(
            model_name='fp17exemptions',
            name='patient_under_18',
            field=models.BooleanField(default=False, verbose_name='Patient under 18'),
        ),
        migrations.AlterField(
            model_name='fp17exemptions',
            name='pension_credit_guarantee_credit',
            field=models.BooleanField(default=False, verbose_name='Pension credit guarantee credit'),
        ),
        migrations.AlterField(
            model_name='fp17exemptions',
            name='universal_credit',
            field=models.BooleanField(default=False, verbose_name='Universal credit'),
        ),
    ]
