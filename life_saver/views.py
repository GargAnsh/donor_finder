from django.shortcuts import render, redirect
from .models import DonorInfo
from .forms import donorInfoForm,donorfinderForm
from django.utils import timezone
from datetime import timedelta
from django.contrib import messages
from django.http import HttpResponse


def donor_info_list(request):
    donors = DonorInfo.objects.all()
    return render(request, 'life_saver/Donor_info_list.html', {'donors': donors})

def add_donor(request):
    if request.method == 'POST':
        form = donorInfoForm(request.POST)
        if form.is_valid():
            form.save()
            # Add a success message
            messages.success(request, 'Registration done successfully.')
            return redirect('donor_finder')
        else:
            # Handle form validation errors
            # You can add code here to display form errors to the user
            # For example, you can pass form.errors to the template
            return render(request, 'life_saver/donor_add_form.html', {'form': form, 'errors': form.errors})
    else:
        form = donorInfoForm()
    return render(request, 'life_saver/donor_add_form.html', {'form': form})

def update_donor(request, pk):
    donor = DonorInfo.objects.get(pk=pk)
    if request.method == 'POST':
        form = donorInfoForm(request.POST, instance=donor)
        if form.is_valid():
            form.save()
            return redirect('donor_list')
        else:
            # Handle form validation errors
            # You can add code here to display form errors to the user
            # For example, you can pass form.errors to the template
            return render(request, 'life_saver/donor_form.html', {'form': form, 'donor': donor, 'errors': form.errors})
    else:
        form = donorInfoForm(instance=donor)
    return render(request, 'life_saver/donor_form.html', {'form': form, 'donor': donor})

def delete_donor(request, pk):
    donor = DonorInfo.objects.get(pk=pk)
    donor.delete()
    return redirect('donor_list')




def donor_finder(request):
    # Create an instance of the donorfinderForm
    form = donorfinderForm()

    if request.method == 'GET':
        blood_group = request.GET.get('blood_group', '')  # Get the selected blood group from the form

        # Calculate the date 50 days ago from the current date
        fifty_days_ago = timezone.now() - timedelta(days=50)

        # Add validation to check if blood_group is not empty
        if blood_group:
            donors = DonorInfo.objects.filter(blood_group=blood_group , donation_date__lte=fifty_days_ago)
        else:
            donors = DonorInfo.objects.none()
    else:
        donors = DonorInfo.objects.none()

    return render(request, 'life_saver/donor_finder.html', {'form': form, 'donors': donors})
