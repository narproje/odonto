# Generated by Django 2.0.13 on 2019-11-28 17:56
from django.db import migrations
from django.db import transaction

fields_to_values = {
    "assessment_and_review": "Assessment & review",
    "assess_and_refuse_treatment": "Assess & refuse treatment",
    "assess_and_appliance_fitted": "Assess & appliance fitted"
}


@transaction.atomic
def forwards(apps, schema_editor):
    Assessment = apps.get_model('odonto', "OrthodonticAssessment")
    for assessment in Assessment.objects.all():
        values = []
        for field, value in fields_to_values.items():
            field_value = getattr(assessment, field)
            if field_value:
                values.append(value)

        if len(values) > 1:
            raise ValueError(
                f'Unable to translate episode {assessment.episode_id}'
            )
        if len(values):
            assessment.assessment = values[0]
            assessment.save()


def backwards(apps, schema_editor):
    Assessment = apps.get_model('odonto', "OrthodonticAssessment")
    values_to_fields = {v: i for i, v in fields_to_values.items()}

    for assessment in Assessment.objects.all():
        if assessment.assessment:
            setattr(assessment, values_to_fields[assessment.assessment], True)
            assessment.save()


class Migration(migrations.Migration):
    dependencies = [
        ('odonto', '0025_orthodonticassessment_assessment'),
    ]

    operations = [
        migrations.RunPython(
            forwards, backwards
        )
    ]
