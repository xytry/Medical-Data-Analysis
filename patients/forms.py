from django import forms

from .models import PatientsInfo
from .validators import validate_gender

class PatientsCreateForm(forms.Form):
    name = forms.CharField()
    gender = forms.CharField(required=False)
    category = forms.CharField(required=False)

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "Hello":
            raise forms.ValidationError("Note a valid name")
        return name

class PatientsInfoCreateForm(forms.ModelForm):
    #gender = forms.CharField(required=False,validators=[validate_gender])
    class Meta:
        model = PatientsInfo
        fields = [
            'name',
            'age',
            'gender',
            'initial_shift',
            'initial_primary_doctor',
            'initial_secondary_doctor',
            'initial_admitted',
            'initial_admitted_to_edtu',
            'initial_discharged',
            'follow_up_initial_visit',
            'initial_at_own_risk_discharges',
            'activities_of_daily_living',
            'mobility',
            'caregiver',
            'diabetes_mellitus',
            'diabetes_mellitus_end_organ_damage',
            'peripheral_vascular_disease',
            'congestive_heart_failure',
            'chronic_obstructive_pulmonary_disease',
            'acute_myocardial_infarction',
            'transient_ischemic_attack',
            'renal_disease',
            'nonmetastatic_cancer',
            'metastatic_cancer',
            'abdominal_pain',
            'trauma',
            'fever',
            'upper_respiratory_tract_infections',
            'renal_colic',
            'giddiness',
            'low_back_pain',
            'cerebral_palsy',
            'asthma',
            'nausea_vomiting',
            'diarrhea',
            'sob',
            'musculoskeletal_pain',
            'constipation',
            'initial_vital_signs',
            'initial_pain_score',
            'initial_pac',
            'initial_pac_vs3',
            'return_shift',
            'return_primary_doctor',
            'return_secondary_doctor',
            'persist_pain',
            'worsen_symptoms_except_pain',
            'extend_mc',
            'return_vital_signs',
            'return_pain_score',
            'return_pac',
            'return_pac_vs3',
            'slug',
            #'category'
        ]

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "Hello":
            raise forms.ValidationError("Note a valid name")
        return name