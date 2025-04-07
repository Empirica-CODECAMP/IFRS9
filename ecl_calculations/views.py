# ecl_calculations/views.py
from django.shortcuts import render
from .models import ECLReport, StageAllocationReport, LossAllowance, CreditRiskExposure

def ecl_landing(request):
    context = {
        "ecl_reports": ECLReport.objects.all(),
        "stage_allocations": StageAllocationReport.objects.all(),
        "loss_allowances": LossAllowance.objects.all(),
        "credit_exposures": CreditRiskExposure.objects.all(),
    }
    return render(request, "ecl.html", context)

def ecl_report_list(request):
    return render(request, "ecl_calculations/ecl_report_list.html", {"ecl_reports": ECLReport.objects.all()})

def stage_allocation_list(request):
    return render(request, "ecl_calculations/stage_allocation_list.html", {"stage_allocations": StageAllocationReport.objects.all()})

def loss_allowance_list(request):
    return render(request, "ecl_calculations/loss_allowance_list.html", {"loss_allowances": LossAllowance.objects.all()})

def credit_risk_exposure_list(request):
    return render(request, "ecl_calculations/credit_risk_exposure_list.html", {"credit_exposures": CreditRiskExposure.objects.all()})
