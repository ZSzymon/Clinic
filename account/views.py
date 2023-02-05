from django.shortcuts import render, redirect
from django.contrib import messages
from account.models import Note
from account.forms import UserCreationForm, NoteForm
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.utils.translation import gettext_lazy as _
from Clinic.settings import LOGIN_URL
from main_app.models import Appointment
from account.models import Account

# Create your views here.

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'account/register.html'
    success_url = '/profile.html/'


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {email} You can log in now')
            return redirect('account-login')
        else:
            messages.error(request, 'Account not created.')

    else:
        form = UserCreationForm()
    return render(request, 'account/register.html', {'form': form})


@login_required(login_url=LOGIN_URL)
def profile(request):
    is_patient = request.user.type == Account.Types.PATIENT
    is_doctor = request.user.type == Account.Types.DOCTOR
    if is_patient:
        appointments = Appointment.objects.all().filter(patient=request.user)
    elif is_doctor:
        appointments = Appointment.objects.all().filter(doctor=request.user)
    else:
        appointments = Appointment.objects.all()

    context = {
        'appointments' : appointments,
        'any_appoitments' : True if appointments else False,
        'is_doctor' : is_doctor,
        'is_patient': is_patient,
    }
    return render(request, 'account/profile.html',context=context)


@login_required(login_url=LOGIN_URL)
def notebook(request):
    notes = Note.objects.all().filter(user=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            messages.success(request, f'Note created.')
            return redirect('account-notebook')
        else:
            messages.error(request, 'Note not created.')

    else:
        form = NoteForm()

    context = {"form": form,
               'notes': notes,
               }
    return render(request, 'account/notes.html', context)

@login_required(login_url=LOGIN_URL)
def update_note(request, pk):
    note = Note.objects.get(id=pk)
    form = NoteForm(instance=note)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, _(f'Updated note'))
            return redirect('account-notebook')
        else:
            messages.error(request, _('An error occurred while attempting to update note.'))
    context = {
        'form': form,
        'note': note,
    }
    return render(request, "account/update_note.html", context)

@login_required(login_url=LOGIN_URL)
def delete_note(request, pk):
    note = Note.objects.get(id=pk)

    if request.method == 'POST':
        name = note.note
        note.delete()
        messages.success(request, _(f'deleted note:{name}'))
        return redirect('account-notebook')
    return render(request, 'account/delete_note.html', {'note': note})



