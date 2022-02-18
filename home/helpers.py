import decimal
import math
from dateutil.relativedelta import *
from datetime import date


def calc_age(birth_date):
    if birth_date and birth_date < date.today():
        age = relativedelta(date.today(), birth_date)
        age = {"lata:": age.years,
               'miesiące:': age.months,
               'dni:': age.days}
        return age


def calc_glucose(glucose_val, glucose_unit):
    if glucose_val:
        glucose_calculated = (glucose_val, 'mmol/l', glucose_val * 18, 'mg/dl') \
            if glucose_unit == 'mmol/l' else \
            (glucose_val, 'mg/dl', round(glucose_val / 18, 2), 'mmol/l')
    else:
        glucose_calculated = None
    return glucose_calculated


def calc_bmi(bmi, weight, height):
    if bmi:
        if weight and height:
            calc_bmi = round(weight / ((height / 100) * (height / 100)), 1)
            if calc_bmi < 4 or calc_bmi > 110:
                calculated_bmi = f'{calc_bmi}  kg/m2  - wynik mało prawdopodobny, sprawdź poprawność wprowadzonych danych'
            else:
                calculated_bmi = f'{calc_bmi}  kg/m2'
        else:
            calculated_bmi = 'podaj wagę i wzrost '
        return calculated_bmi


def calc_heart_rate(rr, speed):
    if rr:
        return round(1500 / rr) if speed == '25' else round(3000 / rr)


def calc_qtc(rr, qt, speed):
    if rr:
        if qt:
            rr_s = round(rr * decimal.Decimal(0.04), 3) if speed == '25' else round(rr * decimal.Decimal(0.02), 3)
            qt_s = round(qt * decimal.Decimal(0.04), 3) if speed == '25' else round(qt * decimal.Decimal(0.02), 3)
            qtc_bazzet = round(qt_s / decimal.Decimal(math.sqrt(rr_s)), 3)
            qtc_frederic = round(qt_s / decimal.Decimal(math.pow(rr_s, 1 / 3)), 3)
            return [qtc_bazzet, qtc_frederic]
