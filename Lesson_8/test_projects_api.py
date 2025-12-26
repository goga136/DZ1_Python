import pytest
import requests

base_url = "https://yougile.com/api-v2/projects"
token = "ВВедите сюда свой токен"
HEADERS = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

def test_create_project_positive():
    payload = {
        "title": "ГосУслуги"
    }
    response = requests.post(
        base_url,
        json=payload,
        headers=HEADERS
    )
    assert response.status_code == 201
    assert "id" in response.json()


def test_create_project_negative():
    payload = {}
    response = requests.post(
        base_url,
        json=payload,
        headers=HEADERS
    )
    assert response.status_code == 400


def test_update_project_positive():
    payload = {
        "title": "ГосУслуги"
    }
    response = requests.post(
        base_url,
        json=payload,
        headers=HEADERS
    )
    project_id = response.json()["id"]

    update_payload = {
        "title": "ГосУслуги_2"
    }
    response = requests.put(
        f'{base_url}/{project_id}/',
        json=update_payload,
        headers=HEADERS
    )
    assert response.status_code == 200
    assert "id" in response.json()


def test_update_project_negative():
    payload = {
        "title": "ГосУслуги_2"
    }
    response = requests.post(
        base_url,
        json=payload,
        headers=HEADERS
    )
    project_id = response.json()["id"]

    update_payload = {
        "title": ""
    }
    response = requests.put(
        f'{base_url}/{project_id}/',
        json=update_payload,
        headers=HEADERS
    )
    assert response.status_code == 400


def test_get_project_positive():
    response = requests.get(
        f'{base_url}/7ca569b8-17e3-4fe2-8da6-e3135e2166c1',
        headers=HEADERS
    )
    assert response.status_code == 200
    assert "id" in response.json()


def test_get_project_negative():
    response = requests.get(
        f'{base_url}/slkdurhygurghjhfv935763764',
        headers=HEADERS
    )
    assert response.status_code == 404





