from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import (
    StatementOfIncome,
    StatementOfFinancialPosition,
    StatementOfChangesInEquity,
    StatementOfCashflow,
)

def financial_statements_landing(request):
    context = {
        "incomes": StatementOfIncome.objects.all(),
        "positions": StatementOfFinancialPosition.objects.all(),
        "equitys": StatementOfChangesInEquity.objects.all(),
        "cashflows": StatementOfCashflow.objects.all(),
    }
    return render(request, "landing.html", context)
