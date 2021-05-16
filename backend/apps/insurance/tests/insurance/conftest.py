import pytest
from pytest_factoryboy import register

from .factories import RiskFactory, RiskFieldFactory, FieldOptionFactory


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


register(RiskFactory, 'risk')
register(RiskFieldFactory, 'risk_field')
register(FieldOptionFactory, 'field_option')
