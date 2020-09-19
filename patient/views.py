from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Patient, Condition
from .forms import PatientForm, ConditionForm, PatientUpdateForm
# Create your views here.

class PatientListView(generic.ListView):
    model = Patient
    template_name = "patient/patient_list.html"
    context_object_name = 'all_patient'

class PatientCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "patient/create_patient.html"
    def get(self, request):
        form = PatientForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            form.save()
            patient_id = form.save().id
            patient_url = reverse('patient:patient_condition', kwargs={'pk': patient_id})
            return redirect(to=patient_url)
        else:
            return render(request, self.template_name, {'form': form})
    
class PatientDetailView(LoginRequiredMixin, generic.DetailView):
    queryset = Patient.objects.all()
    template_name = "patient/patient_detail.html"
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['condition'] = Condition.objects.get(owner=self.object.id)
        return ctx

class PatientUpdateView(LoginRequiredMixin, generic.UpdateView):
    form_class = PatientUpdateForm
    template_name = 'patient/patient_update.html'

    def get_queryset(self):
        return Patient.objects.all()

class ConditionCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = ConditionForm
    template_name = "patient/condition.html"
    success_url = reverse_lazy('patient:all_patient')

    def get_initial(self):
        full_url = self.request.path
        owner_split = full_url.split('/')[3:]
        for owner in owner_split:
            initial = super().get_initial()
            initial['owner'] = owner
            return initial

        