from django.shortcuts import render
from .models import StateData

def page_one(request):
    if request.method == 'POST':
        # Assuming your form fields match the model fields
        name = request.POST.get('name')
        percentage = request.POST.get('percentage')

        # Save data to StateData model
        state_data = StateData.objects.create(
            name=name,
            percentage=percentage
        )
        # Redirect to a success page after form submission
        return redirect('success_page')
    else:
        # Retrieve StateData objects and sort by percentage in ascending order
        state_data_list = StateData.objects.all().order_by('percentage')
        return render(request, "index.html", {'state_data_list': state_data_list})
