from django.shortcuts import render

from django.shortcuts import render
from home.forms import CalcForm
from home.helpers import calc_age, calc_glucose, calc_bmi, calc_heart_rate, calc_qtc


def home_page_view(request):
    form = CalcForm()

    if request.method == 'POST':
        form = CalcForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            context = {
                'form': form,
                'birth_date': cd['birth_date'],
                'weight': cd['weight'],
                'age': calc_age(cd['birth_date']),
                'glucose_calculated': calc_glucose(cd['glucose_val'], cd['glucose_unit']),
                'bmi': calc_bmi(cd['bmi'], cd['weight'], cd['height']),
                'heart_rate': calc_heart_rate(cd['rr'], cd['speed']),
                'qtc': calc_qtc(cd['rr'], cd['qt'], cd['speed'])
            }
            return render(request, 'home/home.html', context)

    context = {'form': form}
    return render(request, 'home/home.html', context)

