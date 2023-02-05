from cart.cart import Cart
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _

from Clinic.settings import LOGIN_URL
from pharmacy.forms import *
from pharmacy.models import *

# Create your views here.


def pharmacy_home(request):
    user = request.user
    prescriptions = Prescription.objects.all().filter(patient=user)
    context = {"prescriptions": prescriptions}
    return render(request, "pharmacy/home.html", context)


def drugs_doctor(request):
    form = DrugForm()
    drugs = Drug.objects.all()

    if request.method == "POST":
        form = DrugForm(request.POST)
        if form.is_valid():
            form.save()
            drug_name = form.cleaned_data.get("name")
            messages.success(request, _(f"Created drug:{drug_name}"))
            return redirect("drugs_path")
        else:
            messages.error(request, _("error in creating drug."))
            return redirect("drugs_path")

    context = {"form": form, "drugs": drugs}
    return render(request, "pharmacy/doctor_drugs_panel.html", context)


@login_required(login_url=LOGIN_URL)
def update_prescription(request, pk):
    prescription = Prescription.objects.get(id=pk)
    form = PrescriptionForm(instance=prescription)
    if request.method == "POST":
        form = PrescriptionForm(request.POST, instance=prescription)
        if form.is_valid():
            form.save()
            messages.success(request, _(f"Updated prescription"))
            return redirect("prescriptions_path")
        else:
            messages.error(
                request,
                _(
                    "An error occurred while attempting to update prescription."
                ),
            )
    context = {
        "form": form,
        "prescription": prescription,
    }
    return render(request, "pharmacy/update_prescription.html", context)


@login_required(login_url=LOGIN_URL)
def update_drug(request, pk):
    drug = Drug.objects.get(id=pk)
    form = DrugForm(instance=drug)
    if request.method == "POST":
        form = DrugForm(request.POST, instance=drug)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get("name")
            messages.success(request, _(f"Updated drug:{name}"))
            return redirect("drugs_path")
        else:
            messages.error(
                request,
                _("An error occurred while attempting to update drug."),
            )
    context = {
        "form": form,
        "drug": drug,
    }
    return render(request, "pharmacy/update_drug.html", context)


@login_required(login_url=LOGIN_URL)
def prescriptions_doctor(request):
    form = PrescriptionForm()
    prescriptions = Prescription.objects.all()

    if request.method == "POST":
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            print("was valid?")
            return redirect("prescriptions_path")

    context = {
        "prescriptions": prescriptions,
        "form": form,
    }
    return render(
        request, "pharmacy/doctor_prescriptions_panel.html", context=context
    )


@login_required(login_url=LOGIN_URL)
def delete_drug(request, pk):
    drug = Drug.objects.get(id=pk)

    if request.method == "POST":
        name = drug.name
        drug.delete()
        messages.success(request, _(f"deleted drug:{name}"))
        return redirect("drugs_path")
    return render(request, "pharmacy/delete_drug.html", {"drug": drug})


@login_required(login_url=LOGIN_URL)
def delete_prescription(request, pk):
    prescription = Prescription.objects.get(id=pk)

    if request.method == "POST":
        prescription.delete()
        messages.success(request, _(f"deleted drug"))
        return redirect("drugs_path")
    return render(
        request,
        "pharmacy/delete_prescription.html",
        {"prescription": prescription},
    )


@login_required(login_url=LOGIN_URL)
def store_view(request):
    drugs = Drug.objects.all()
    form = DrugForm()

    context = {"drugs": drugs, "form": form}

    return render(request, "pharmacy/store.html", context)


@login_required(login_url=LOGIN_URL)
def cart_add(request, id):
    cart = Cart(request)
    product = Drug.objects.get(id=id)
    cart.add(product=product)
    return redirect("store")


@login_required(login_url=LOGIN_URL)
def item_clear(request, id):
    cart = Cart(request)
    product = Drug.objects.get(id=id)
    cart.remove(product)
    return redirect(request.META.get("HTTP_REFERER"))


@login_required(login_url=LOGIN_URL)
def item_increment(request, id):
    cart = Cart(request)
    product = Drug.objects.get(id=id)
    cart.add(product=product)
    return redirect(request.META.get("HTTP_REFERER"))


@login_required(login_url=LOGIN_URL)
def item_decrement(request, id):
    cart = Cart(request)
    product = Drug.objects.get(id=id)
    cart.decrement(product=product)
    return redirect(request.META.get("HTTP_REFERER"))


@login_required(login_url=LOGIN_URL)
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect(request.META.get("HTTP_REFERER"))


@login_required(login_url=LOGIN_URL)
def cart_detail(request):
    return render(request, "pharmacy/cart_detail.html")


@login_required(login_url=LOGIN_URL)
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("pharmacy/cart_detail.html")
