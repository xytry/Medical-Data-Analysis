from django.conf import settings
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse

from .utils import unique_slug_generator
from .validators import validate_gender

User =settings.AUTH_USER_MODEL

# Create your models here.

class PatientsInfoQuerySet(models.query.QuerySet):
    def search(self,query): #PatientsInfo.objects.all().search(query)
        #if query:
            return self.filter(
                Q(name__icontains=query)|
                Q(age__icontains=query)|
                Q(gender__icontains=query)|
                Q(initial_shift__icontains=query)|
                Q(initial_primary_doctor__icontains=query)|
                Q(initial_secondary_doctor__icontains=query) |
                Q(initial_admitted__icontains=query) |
                Q(initial_admitted_to_edtu__icontains=query) |
                Q(initial_discharged__icontains=query) |
                Q(follow_up_initial_visit__icontains=query) |
                Q(initial_at_own_risk_discharges__icontains=query) |
                Q(activities_of_daily_living__icontains=query) |
                Q(mobility__icontains=query) |
                Q(caregiver__icontains=query) |
                Q(diabetes_mellitus__icontains=query) |
                Q(diabetes_mellitus_end_organ_damage__icontains=query) |
                Q(peripheral_vascular_disease__icontains=query) |
                Q(congestive_heart_failure__icontains=query) |
                Q(chronic_obstructive_pulmonary_disease__icontains=query) |
                Q(acute_myocardial_infarction__icontains=query) |
                Q(transient_ischemic_attack__icontains=query) |
                Q(renal_disease__icontains=query) |
                Q(nonmetastatic_cancer__icontains=query) |
                Q(metastatic_cancer__icontains=query) |
                Q(abdominal_pain__icontains=query) |
                Q(trauma__icontains=query) |
                Q(fever__icontains=query) |
                Q(upper_respiratory_tract_infections__icontains=query) |
                Q(renal_colic__icontains=query) |
                Q(giddiness__icontains=query) |
                Q(low_back_pain__icontains=query) |
                Q(cerebral_palsy__icontains=query) |
                Q(asthma__icontains=query) |
                Q(nausea_vomiting__icontains=query) |
                Q(diarrhea__icontains=query) |
                Q(sob__icontains=query) |
                Q(musculoskeletal_pain__icontains=query) |
                Q(constipation__icontains=query) |
                Q(initial_vital_signs__icontains=query) |
                Q(initial_pac__icontains=query) |
                Q(return_shift__icontains=query) |
                Q(return_primary_doctor__icontains=query) |
                Q(return_secondary_doctor__icontains=query) |
                Q(persist_pain__icontains=query) |
                Q(worsen_symptoms_except_pain__icontains=query) |
                Q(extend_mc__icontains=query) |
                Q(return_vital_signs__icontains=query) |
                Q(return_pac__icontains=query) |
                Q(item__name__icontains=query)
            ).distinct()
        #return self

class PatientsInfoManager(models.Manager):
    def get_queryset(self):
        return PatientsInfoQuerySet(self.model,using=self._db)

    def search(self,query):  #PatientsInfo.objetcs.search()
        return self.get_queryset().search(query)

class PatientsInfo(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=100, blank=False)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=6, null=True,blank=True, default='Male', validators=[validate_gender],help_text='Male / Female')

    initial_shift = models.CharField(max_length=6,null=True,blank=True, default='AM', help_text='AM / PM / Night')
    initial_primary_doctor = models.CharField(max_length=20,null=True,blank=True, default='HO&MO', help_text='HO&MO / Locum&GP / Registrar')
    initial_secondary_doctor = models.CharField(max_length=30, null=True, blank=True,default='No Supervised Secondary Doctor',help_text='No Supervised Secondary Dcotor / Supervised by Secondary Doctor')
    initial_admitted = models.CharField(max_length=50, null=True, blank=True, default='No',help_text='Admitted/ No')
    initial_admitted_to_edtu = models.CharField(max_length=50,null=True,blank=True, default='No', help_text='Admitted to EDTU / No')
    initial_discharged = models.CharField(max_length=50,null=True,blank=True, default='No', help_text='Discharged / No')
    follow_up_initial_visit = models.CharField(max_length=50,null=True,blank=True, default='No', help_text='Follow up Initial Visit / No')
    initial_at_own_risk_discharges = models.CharField(max_length=50,null=True,blank=True, default='No', help_text='At Own Risk Discharges / No')
    activities_of_daily_living = models.CharField(max_length=20,null=True,blank=True, default='Independent', help_text='Independent / Assisted / Dependent')
    mobility = models.CharField(max_length=20,null=True,blank=True, default='Independet', help_text='Independent/Ambulant with Assistance / Wheelchair / Bedbound')
    caregiver = models.CharField(max_length=20,null=True,blank=True, default='Do not have', help_text='Do not have / Have')
    diabetes_mellitus = models.CharField(max_length=50,null=True,blank=True, default='No', help_text='Diabetes Mellitus / No')
    diabetes_mellitus_end_organ_damage = models.CharField(max_length=50,null=True,blank=True, default='No', help_text='Diabetes Mellitus End Organ Damage / No')
    peripheral_vascular_disease = models.CharField(max_length=50,null=True,blank=True, default='No', help_text='Peripheral Vascular Disease / No')
    congestive_heart_failure = models.CharField(max_length=50,null=True,blank=True, default='No', help_text='Congestive Heart Failure / No')
    chronic_obstructive_pulmonary_disease = models.CharField(max_length=50,null=True,blank=True, default='No', help_text='Chronic Obstructive Pulmonary Disease / No')
    acute_myocardial_infarction = models.CharField(max_length=50,null=True,blank=True, default='No', help_text='Acute Myocardial Infarction / No')
    transient_ischemic_attack = models.CharField(max_length=50,null=True,blank=True, default='No', help_text='Transient Ischemic Attack / No')
    renal_disease = models.CharField(max_length=50,null=True,blank=True, default='No', help_text='Renal Disease / No')
    nonmetastatic_cancer = models.CharField(max_length=50,null=True,blank=True, default='No', help_text='Nonmetastatic Cancer / No')
    metastatic_cancer = models.CharField(max_length=50,null=True,blank=True, default='No', help_text='Metastatic Cancer / No')
    abdominal_pain = models.CharField(max_length=50,null=True,blank=True, default='No', help_text='Abdominal Pain / No')
    trauma = models.CharField(max_length=30,null=True,blank=True, default='No', help_text='Trauma/No')
    fever = models.CharField(max_length=30,null=True,blank=True, default='No', help_text='Fever / No')
    upper_respiratory_tract_infections = models.CharField(max_length=30,null=True,blank=True, default='No', help_text='Upper Respiratory Tract Infections / No')
    renal_colic = models.CharField(max_length=30,null=True,blank=True, default='No', help_text='Renal Colic / No')
    giddiness = models.CharField(max_length=30,null=True,blank=True, default='No', help_text='Giddiness / No')
    low_back_pain = models.CharField(max_length=30,null=True,blank=True, default='No', help_text='Low Back Pain / No')
    cerebral_palsy = models.CharField(max_length=30,null=True,blank=True, default='No', help_text='Cerebral Palsy / No')
    asthma = models.CharField(max_length=30,null=True,blank=True, default='No', help_text='Asthma / No')
    nausea_vomiting = models.CharField(max_length=30,null=True,blank=True, default='No', help_text='Nausea Vomiting / No')
    diarrhea = models.CharField(max_length=30,null=True,blank=True, default='No', help_text='Diarrhea / No')
    sob = models.CharField(max_length=30,null=True,blank=True, default='No', help_text='Sob / No')
    musculoskeletal_pain = models.CharField(max_length=30,null=True,blank=True, default='No', help_text='Musculoskeletal Pain / No')
    constipation = models.CharField(max_length=30,null=True,blank=True, default='No', help_text='Constipation / No')
    initial_vital_signs = models.CharField(max_length=30,null=True,blank=True, default='Normal', help_text='Normal / Abnormal')
    initial_pain_score = models.IntegerField(null=True,blank=True, default='0', help_text='0-10')
    initial_pac = models.CharField(max_length=30,null=True,blank=True, default='P1', help_text='P1 / P2 / P3')
    initial_pac_vs3 = models.IntegerField(null=True,blank=True, default='0', help_text='0=P1&P2, 1=P3')
    return_shift = models.CharField(max_length=30,null=True,blank=True, default='AM', help_text='AM / PM / Night')
    return_primary_doctor = models.CharField(max_length=30,null=True,blank=True, default='HO&MO', help_text='HO&MO / Locum&GP / Registrar')
    return_secondary_doctor = models.CharField(max_length=30,null=True,blank=True, default='No Supervised Secondary Doctor', help_text='No Supervised Secondary Dcotor / Supervised by Secondary Doctor')
    persist_pain = models.CharField(max_length=30,null=True,blank=True, default='No', help_text='Persist Pain / No')
    worsen_symptoms_except_pain = models.CharField(max_length=30,null=True,blank=True, default='No', help_text='Worsen Symptoms Except Pain / No')
    extend_mc = models.CharField(max_length=30,null=True,blank=True, default='No', help_text='Extend MC / No')
    return_vital_signs = models.CharField(max_length=30,null=True,blank=True, default='Normal', help_text='Normal / Abnormal')
    return_pain_score = models.IntegerField(null=True,blank=True, default='0', help_text='0-10')
    return_pac = models.CharField(max_length=30,null=True,blank=True, default='P1', help_text='P1 / P2 / P3')
    return_pac_vs3 = models.IntegerField(null=True,blank=True, default='0', help_text='0=P1&P2, 1=P3')

    #category = models.CharField(max_length=10,null=True,blank=True, default='')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True,blank=True)

    objects = PatientsInfoManager()  #add Model.objects.all()
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return f"/patients/{self.slug}"
        return reverse('patients:detail', kwargs={'slug': self.slug})

    @property
    def title(self):
        return self.name

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    #print('saving..')
    #print(instance.timestamp)
    #instance.gender = instance.gender.capitalize()
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

#def rl_post_save_receiver(sender, instance, created, *args, **kwargs):
#    print('saved..')
#    print(instance.timestamp)
#    if not instance.slug:
#        instance.slug = unique_slug_generator(instance)
#        instance.save()

pre_save.connect(rl_pre_save_receiver, sender=PatientsInfo)

#post_save.connect(rl_post_save_receiver, sender=PatientsInfo)
