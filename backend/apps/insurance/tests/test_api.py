import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_risk_create_api(api_client):
    url = reverse('risk-list-create')
    data = {
        'name': 'Vehicle',
        'fields': [{
            'label': 'Manufacturer',
            'type': 'select',
            'options': [
                {'name': 'Tesla'},
                {'name': 'Audi'}
            ]
        }]
    }
    response = api_client.post(
        path=url,
        data=data,
        format='json'
    )
    assert response.status_code == 201


@pytest.fixture
def test_risk_list_api(api_client):
    url = reverse('risk-list-create')
    response = api_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_risk_detail_api(api_client, risk):
    url = reverse('risk-detail', kwargs={'pk': risk.pk})
    response = api_client.get(url)
    assert response.status_code == 200
