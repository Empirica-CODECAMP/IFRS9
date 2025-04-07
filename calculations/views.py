from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import ModelRun
from .forms import ModelRunForm

def calculations_dashboard(request):
    if request.method == 'POST':
        form = ModelRunForm(request.POST)
        if form.is_valid():
            model_run = form.save(commit=False)
            model_run.model_name = "Default IFRS9 Model"
            model_run.status = "pending"
            model_run.input_parameters = "{}"  # Placeholder
            model_run.save()
            return redirect('calculations')  # Replace if you want to go to a 'success' view
    else:
        form = ModelRunForm()

    return render(request, 'calculations/dashboard.html', {'form': form})
