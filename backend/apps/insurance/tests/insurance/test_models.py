import pytest

from pytest_factoryboy import LazyFixture


@pytest.mark.django_db
def test_risk(risk):
    assert risk.name == 'Vehicle'


@pytest.mark.django_db
@pytest.mark.parametrize('risk_field__risk', [LazyFixture('risk')])
def test_risk_field(risk_field, risk):
    assert risk_field.risk.id == risk.id


@pytest.mark.django_db
@pytest.mark.parametrize('field_option__field', [LazyFixture('risk_field')])
def test_field_option(field_option, risk_field):
    assert field_option.field.id == risk_field.id
