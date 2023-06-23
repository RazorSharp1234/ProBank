from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from form.models import Form


def form(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone_number = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        district = request.POST['district']
        branch = request.POST['branch']
        account_type = request.POST['account-type']
        materials = request.POST.getlist('materials')

        application = Form(
            name=name,
            dob=dob,
            age=age,
            gender=gender,
            phone_number=phone_number,
            email=email,
            address=address,
            district=district,
            branch=branch,
            account_type=account_type,
            materials_provided=materials
        )
        application.save()

        # return render(request, 'form.html', {'message': 'Application Accepted'})
        # messages.success(request, 'Application Accepted')
        #return redirect('/')

        if form.is_valid():
            # Save the form data to the database
            form.save()

            # Add a success message
            messages.success(request, 'Form submitted successfully.')

            # Redirect to a success page
            return redirect('/')
        else:
            # Add an error message
            messages.error(request, 'Form submission failed.')

        # ...

    return render(request, 'form.html')
