from datetime import date

import pytest
from dateutil.relativedelta import relativedelta
from django.urls import reverse

from home.views import *


@pytest.fixture
def get_homepage_response(client):
    url = reverse('home:homepage')
    return client.get(url)


def test_homepage_status_code(client):
    url = reverse('home:homepage')
    return client.get(url)


def test_homepage_status_code_by_reverse(get_homepage_response):
    assert get_homepage_response.status_code == 200


def test_homepage_templates(get_homepage_response):
    assert 'home/home.html' in [t.name for t in get_homepage_response.templates]


def test_homepage_contains_correct_html(get_homepage_response):
    assert "Oblicz wiek" in get_homepage_response.content.decode('UTF-8')


def test_calc_age():
    age = relativedelta(date.today(), date(2019, 11, 11))
    assert calc_age(date(2019, 11, 11)) == ({"lata:": age.years,
            'miesiące:': age.months,
            'dni:': age.days
            }, date(2019, 11, 11))


def calc_glu():
    assert calc_glu(5, 'mmol/l') == (5, 'mmol/l', 90.00, 'mg/dl')
    assert calc_glu(180, 'mg/dl') == (180,  'mg/dl', 10, 'mmol/l')
    assert calc_glu(None, 'mg/dl') is None
    assert calc_glu(None, None) is None


def test_calc_bmi():
    assert calc_bmi(60, 170) == 20.8
    assert calc_bmi(60, None) is None
    assert calc_bmi(None, 180) is None
    assert calc_bmi(None, None) is None








