from django.shortcuts import render
from .models import Category, Category1, Category2, Category3
from django.http import HttpResponse

def page_one(request):
    if request.method == 'POST':
        category_name = request.POST.get('state_wise')
        category, created = Category.objects.get_or_create(name=category_name)

        if category_name == 'Uttar_Pradesh':
            StateData1.objects.create(
                category=category,
                field1=request.POST.get('first_name'),
                field2=request.POST.get('marks')
            )
        elif category_name == 'Bihar':
            StateData2.objects.create(
                category=category,
                field1=request.POST.get('last_name'),
                field2=request.POST.get('marks_in_percentage')
            )
        elif category_name == 'Karnataka':
            StateData3.objects.create(
                category=category,
                field1=request.POST.get('email'),
                field2=request.POST.get('date')
            )
        elif category_name == 'Madhya_Pradesh':
            StateData3.objects.create(
                category=category,
                field1=request.POST.get('email'),
                field2=request.POST.get('date')
            )

        return HttpResponse('Data saved successfully!')
    return render(request, "index.html")


