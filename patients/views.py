from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
import random
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView,ListView, DetailView, CreateView, UpdateView

from .forms import PatientsCreateForm, PatientsInfoCreateForm
from .models import PatientsInfo

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import svm
from sklearn import cross_validation, metrics
from sklearn.grid_search import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
import pickle
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score,roc_auc_score
from sklearn.externals import joblib

# Create your views here.

class HomeView(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView,self).get_context_data(*args, **kwargs)

        #model built
        data = pd.read_csv("EMD_URV_2014(9).csv")
        df_x = data.iloc[:, 1:]
        df_y = data.iloc[:, 0]
        x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.2, random_state=4)
        clf2 = svm.SVC(C=0.21, gamma=0.08, kernel='poly')
        clf2.fit(x_train, y_train)
        accuracy = clf2.score(x_test, y_test)

        #user input
        queryset = PatientsInfo.objects.latest('pk')
        qs_age=(queryset.age-16)/(101-16)
        if(queryset.gender=='Male'):
            qs_gender = 0
        else:
            qs_gender = 1

        if(queryset.initial_shift=='AM'):
            qs_initial_shift = 0
        elif(queryset.initial_shift=='PM'):
            qs_initial_shift = 0.5
        else:
            qs_initial_shift = 1

        if(queryset.initial_primary_doctor=='HO&MO'):
            qs_initial_primary_doctor = 0
        elif(queryset.initial_primary_doctor=='Locum&GP'):
            qs_initial_primary_doctor = 0.5
        else:
            qs_initial_primary_doctor = 1

        if (queryset.initial_secondary_doctor == 'No Supervised Secondary Doctor'):
            qs_initial_secondary_doctor = 0
        else:
            qs_initial_secondary_doctor = 1

        if (queryset.initial_admitted == 'No'):
            qs_initial_admitted = 0
        else:
            qs_initial_admitted = 1

        if (queryset.initial_admitted_to_edtu == 'No'):
            qs_initial_admitted_to_edtu = 0
        else:
            qs_initial_admitted_to_edtu = 1

        if (queryset.initial_discharged == 'No'):
            qs_initial_discharged = 0
        else:
            qs_initial_discharged = 1

        if (queryset.follow_up_initial_visit == 'No'):
            qs_follow_up_initial_visit = 0
        else:
            qs_follow_up_initial_visit = 1

        if (queryset.initial_at_own_risk_discharges == 'No'):
            qs_initial_at_own_risk_discharges = 0
        else:
            qs_initial_at_own_risk_discharges = 1

        if (queryset.activities_of_daily_living == 'Independent'):
            qs_activities_of_daily_living = 0
        elif (queryset.activities_of_daily_living == 'Assisted'):
            qs_activities_of_daily_living = 0.5
        else:
            qs_activities_of_daily_living = 1

        if (queryset.mobility == 'Independent'):
            qs_mobility = 0
        elif (queryset.mobility == 'Ambulant with Assistance'):
            qs_mobility = 1/3
        elif (queryset.mobility == 'Wheelchair'):
            qs_mobility = 2/3
        else:
            qs_mobility = 1

        if (queryset.caregiver == 'Do not have'):
            qs_caregiver = 0
        else:
            qs_caregiver = 1

        if (queryset.diabetes_mellitus == 'No'):
            qs_diabetes_mellitus = 0
        else:
            qs_diabetes_mellitus = 1

        if (queryset.diabetes_mellitus_end_organ_damage == 'No'):
            qs_diabetes_mellitus_end_organ_damage = 0
        else:
            qs_diabetes_mellitus_end_organ_damage = 1

        if (queryset.peripheral_vascular_disease == 'No'):
            qs_peripheral_vascular_disease = 0
        else:
            qs_peripheral_vascular_disease = 1

        if (queryset.congestive_heart_failure == 'No'):
            qs_congestive_heart_failure = 0
        else:
            qs_congestive_heart_failure = 1

        if (queryset.chronic_obstructive_pulmonary_disease == 'No'):
            qs_chronic_obstructive_pulmonary_disease = 0
        else:
            qs_chronic_obstructive_pulmonary_disease = 1

        if (queryset.acute_myocardial_infarction == 'No'):
            qs_acute_myocardial_infarction = 0
        else:
            qs_acute_myocardial_infarction = 1

        if (queryset.transient_ischemic_attack == 'No'):
            qs_transient_ischemic_attack = 0
        else:
            qs_transient_ischemic_attack = 1

        if (queryset.renal_disease == 'No'):
            qs_renal_disease = 0
        else:
            qs_renal_disease = 1

        if (queryset.nonmetastatic_cancer == 'No'):
            qs_nonmetastatic_cancer = 0
        else:
            qs_nonmetastatic_cancer = 1

        if (queryset.metastatic_cancer == 'No'):
            qs_metastatic_cancer = 0
        else:
            qs_metastatic_cancer = 1

        if (queryset.abdominal_pain == 'No'):
            qs_abdominal_pain = 0
        else:
            qs_abdominal_pain = 1

        if (queryset.trauma == 'No'):
            qs_trauma = 0
            message1 = 0
        else:
            qs_trauma = 1
            message1 = 1

        if (queryset.fever == 'No'):
            qs_fever = 0
        else:
            qs_fever = 1

        if (queryset.upper_respiratory_tract_infections == 'No'):
            qs_upper_respiratory_tract_infections = 0
        else:
            qs_upper_respiratory_tract_infections = 1

        if (queryset.renal_colic == 'No'):
            qs_renal_colic = 0
        else:
            qs_renal_colic = 1

        if (queryset.giddiness == 'No'):
            qs_giddiness = 0
        else:
            qs_giddiness = 1

        if (queryset.low_back_pain == 'No'):
            qs_low_back_pain = 0
        else:
            qs_low_back_pain = 1

        if (queryset.cerebral_palsy == 'No'):
            qs_cerebral_palsy = 0
        else:
            qs_cerebral_palsy = 1

        if (queryset.asthma == 'No'):
            qs_asthma = 0
        else:
            qs_asthma = 1

        if (queryset.nausea_vomiting == 'No'):
            qs_nausea_vomiting = 0
        else:
            qs_nausea_vomiting = 1

        if (queryset.diarrhea == 'No'):
            qs_diarrhea = 0
        else:
            qs_diarrhea = 1

        if (queryset.sob == 'No'):
            qs_sob = 0
        else:
            qs_sob = 1

        if (queryset.musculoskeletal_pain == 'No'):
            qs_musculoskeletal_pain = 0
        else:
            qs_musculoskeletal_pain = 1

        if (queryset.constipation == 'No'):
            qs_constipation = 0
        else:
            qs_constipation = 1

        if (queryset.initial_vital_signs == 'Normal'):
            qs_initial_vital_signs = 0
        else:
            qs_initial_vital_signs = 1

        qs_initial_pain_score=queryset.initial_pain_score/10

        if (queryset.initial_pac == 'P1'):
            qs_initial_pac = 0
        elif (queryset.initial_pac == 'P2'):
            qs_initial_pac = 0.5
        else:
            qs_initial_pac = 1

        qs_initial_pac_vs3 = queryset.initial_pac_vs3

        if (queryset.return_shift == 'AM'):
            qs_return_shift = 0
        elif (queryset.return_shift == 'PM'):
            qs_return_shift = 0.5
        else:
            qs_return_shift = 1

        if (queryset.return_primary_doctor == 'HO&MO'):
            qs_return_primary_doctor = 0
        elif (queryset.initial_primary_doctor == 'Locum&GP'):
            qs_return_primary_doctor = 0.5
        else:
            qs_return_primary_doctor = 1

        if (queryset.return_secondary_doctor == 'No Supervised Secondary Doctor'):
            qs_return_secondary_doctor = 0
        else:
            qs_return_secondary_doctor = 1

        if (queryset.persist_pain == 'No'):
            qs_persist_pain = 0
            message2 = 0
        else:
            qs_persist_pain = 1
            message2 = 1

        if (queryset.worsen_symptoms_except_pain == 'No'):
            qs_worsen_symptoms_except_pain = 0
        else:
            qs_worsen_symptoms_except_pain = 1

        if (queryset.extend_mc == 'No'):
            qs_extend_mc = 0
        else:
            qs_extend_mc = 1

        if (queryset.return_vital_signs == 'Normal'):
            qs_return_vital_signs = 0
        else:
            qs_return_vital_signs = 1

        qs_return_pain_score=queryset.return_pain_score/10

        if (queryset.return_pac == 'P1'):
            qs_return_pac = 0
        elif (queryset.return_pac == 'P2'):
            qs_return_pac = 0.5
        else:
            qs_return_pac = 1

        qs_return_pac_vs3 = queryset.return_pac_vs3

        testdata = [[qs_age,qs_gender,qs_initial_shift,qs_initial_primary_doctor,qs_initial_secondary_doctor,qs_initial_admitted,qs_initial_admitted_to_edtu,qs_initial_discharged,qs_follow_up_initial_visit,qs_initial_at_own_risk_discharges,qs_activities_of_daily_living,qs_mobility,qs_caregiver,qs_diabetes_mellitus,qs_diabetes_mellitus_end_organ_damage,qs_peripheral_vascular_disease,qs_congestive_heart_failure,qs_chronic_obstructive_pulmonary_disease,qs_acute_myocardial_infarction,qs_transient_ischemic_attack,qs_renal_disease,qs_nonmetastatic_cancer,qs_metastatic_cancer,qs_abdominal_pain,qs_trauma,qs_fever,qs_upper_respiratory_tract_infections,qs_renal_colic,qs_giddiness,qs_low_back_pain,qs_cerebral_palsy,qs_asthma,qs_nausea_vomiting,qs_diarrhea,qs_sob,qs_musculoskeletal_pain,qs_constipation,qs_initial_vital_signs,qs_initial_pain_score,qs_initial_pac,qs_initial_pac_vs3,qs_return_shift,qs_return_primary_doctor,qs_return_secondary_doctor,qs_persist_pain,qs_worsen_symptoms_except_pain,qs_extend_mc,qs_return_vital_signs,qs_return_pain_score,qs_return_pac,qs_return_pac_vs3]]
        pred = clf2.predict(testdata)
        if (pred == 1):
            output = "Pay Attention is Required"
        else:
            output = "Pay Attention is not Reuqired"
        #output = "pay attention = %d" % (pred)

        #if qs_trauma == 1:
            #message = "Patient May Suffer from Laceration"
        #if persistpain == 1:
            #message1 = "Patient's condition may worsen and recommend to have a caregiver"
            #tkinter.messagebox.showinfo("Suggestions", message1)

        #num = random.randint(0, 1000)
        #some_list = [num, random.randint(0, 1000), random.randint(0, 1000)]
        context = {
            #"bool_item": False,
            #"num": num,
            #"some_list": some_list,
            #"accuracy": accuracy,
            "queryset":queryset,
            "qs_age":qs_age,
            "qs_gender": qs_gender,
            "qs_initial_shift": qs_initial_shift,
            "qs_initial_primary_doctor": qs_initial_primary_doctor,
            "qs_initial_secondary_doctor": qs_initial_secondary_doctor,
            "qs_initial_admitted": qs_initial_admitted,
            "qs_initial_admitted_to_edtu": qs_initial_admitted_to_edtu,
            "qs_initial_discharged": qs_initial_discharged,
            "qs_follow_up_initial_visit": qs_follow_up_initial_visit,
            "qs_initial_at_own_risk_discharges": qs_initial_at_own_risk_discharges,
            "qs_activities_of_daily_living": qs_activities_of_daily_living,
            "qs_mobility":qs_mobility,
            "qs_caregiver": qs_caregiver,
            "qs_diabetes_mellitus": qs_diabetes_mellitus,
            "qs_diabetes_mellitus_end_organ_damage": qs_diabetes_mellitus_end_organ_damage,
            "qs_peripheral_vascular_disease": qs_peripheral_vascular_disease,
            "qs_congestive_heart_failure": qs_congestive_heart_failure,
            "qs_chronic_obstructive_pulmonary_disease": qs_chronic_obstructive_pulmonary_disease,
            "qs_acute_myocardial_infarction": qs_acute_myocardial_infarction,
            "qs_transient_ischemic_attack": qs_transient_ischemic_attack,
            "qs_renal_disease": qs_renal_disease,
            "qs_nonmetastatic_cancer": qs_nonmetastatic_cancer,
            "qs_metastatic_cancer": qs_metastatic_cancer,
            "qs_abdominal_pain": qs_abdominal_pain,
            "qs_trauma": qs_trauma,
            "qs_fever": qs_fever,
            "qs_upper_respiratory_tract_infections": qs_upper_respiratory_tract_infections,
            "qs_renal_colic": qs_renal_colic,
            "qs_giddiness":qs_giddiness,
            "qs_low_back_pain": qs_low_back_pain,
            "qs_cerebral_palsy": qs_cerebral_palsy,
            "qs_asthma":qs_asthma,
            "qs_nausea_vomiting": qs_nausea_vomiting,
            "qs_diarrhea": qs_diarrhea,
            "qs_sob": qs_sob,
            "qs_musculoskeletal_pain": qs_musculoskeletal_pain,
            "qs_constipation": qs_constipation,
            "qs_initial_vital_signs": qs_initial_vital_signs,
            "qs_initial_pain_score": qs_initial_pain_score,
            "qs_initial_pac": qs_initial_pac,
            "qs_initial_pac_vs3": qs_initial_pac_vs3,
            "qs_return_shift": qs_return_shift,
            "qs_return_primary_doctor": qs_return_primary_doctor,
            "qs_return_secondary_doctor": qs_return_secondary_doctor,
            "qs_persist_pain": qs_persist_pain,
            "qs_worsen_symptoms_except_pain": qs_worsen_symptoms_except_pain,
            "qs_extend_mc": qs_extend_mc,
            "qs_return_vital_signs": qs_return_vital_signs,
            "qs_return_pain_score": qs_return_pain_score,
            "qs_return_pac": qs_return_pac,
            "qs_return_pac_vs3": qs_return_pac_vs3,
            "output": output,
            "message1": message1,
            "message2": message2
        }
        return context

#@login_required(login_url='/login/')
def patients_createview(request):
    form =PatientsInfoCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        if request.user.is_authenticated():
            isinstance=form.save(commit=False)
            isinstance.owner = request.user
            isinstance.save()
            return HttpResponseRedirect("/patients/")
        else:
            return HttpResponseRedirect("/login/")
        form.save()
    if form.errors:
        errors = form.errors

    template_name = 'patients/forms.html'
    context = {"form": form, "errors": errors}
    return render(request, template_name, context)

#useful code starts here

def patients_listview(request):
    template_name = 'patients/patientsinfo_list.html'
    queryset = PatientsInfo.objects.all()
    context = {
        "object_list":queryset
    }
    return  render(request,template_name, context)

def patients_detailview(request,slug):
    template_name = 'patients/patientsinfo_detail.html'
    obj = PatientsInfo.objects.get(slug=slug)
    context = {
        "object_list":obj
    }
    return  render(request,template_name, context)

#really used function starts here
class PatientsListView(LoginRequiredMixin,ListView):
    #queryset = PatientsInfo.objects.all()
    #template_name = 'patients/patientsinfo_list.html'

    def get_queryset(self):
        #print(self.kwargs)

        #slug = self.kwargs.get("slug")
        #if slug:
        #    queryset = PatientsInfo.objects.filter(
        #        Q(category__iexact=slug) |
        #       Q(category__icontains=slug)
        #       )
        #else:
        #   queryset = PatientsInfo.objects.all()
        #return queryset
        return PatientsInfo.objects.filter(owner=self.request.user)
class PatientsDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        return PatientsInfo.objects.filter(owner=self.request.user)
    #template_name = 'patients/patientsinfo_detail.html'

    #queryset = PatientsInfo.objects.all()


    #def get_context_data(self, *args, **kwargs):
        #print(self.kwargs)
        #context = super(PatientsDetailView, self).get_context_data(*args, **kwargs)
        #print(context)
        #return  context

    #def get_object(self, *args, **kwargs):
    #    patient_id = self.kwargs.get('patient_id')
    #    obj = get_object_or_404(PatientsInfo, id=patient_id) #pk=patient_id
    #    return  obj

class  PatientCreateView(LoginRequiredMixin, CreateView):
#class PatientCreateView(CreateView):
    form_class = PatientsInfoCreateForm
    login_url = '/login/'
    template_name = 'form.html'
    #success_url = "/patients/"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(PatientCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(PatientCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Patients'
        return context


class  PatientUpdateView(LoginRequiredMixin, UpdateView):
#class PatientCreateView(CreateView):
    form_class = PatientsInfoCreateForm
    login_url = '/login/'
    template_name = 'patients/detail-update.html'
    #template_name = 'form.html'
    #success_url = "/patients/"

    def get_context_data(self, *args, **kwargs):
        context = super(PatientUpdateView, self).get_context_data(*args, **kwargs)
        name =self.get_object().name
        context['title'] = f'Update URV Patients: { name }'
        return context

    def get_queryset(self):
        return PatientsInfo.objects.filter(owner=self.request.user)