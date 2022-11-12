import requests
from pytest_voluptuous import S
from requests import Response

from test_api_reqres.schemas.tests_with_schema import *
from utils.base_user import reqres_session


def test_create_user():
    name = 'Margo'
    job = 'QA'

    result: Response = reqres_session().post(url='/api/users',
                                             json={"name": name, "job": job})

    assert result.status_code == 201
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert isinstance(result.json()['id'], str)
    assert result.json() == S(create_user_schema)


def test_update_user():
    name = 'Margo'
    job = 'Doctor'

    result: Response = reqres_session().put(url='/api/users/2',
                                            json={"name": name, "job": job})

    assert result.status_code == 200
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert result.json() == S(update_user_schema)


def test_list_user():
    result: Response = reqres_session().get(url='/api/users?page=2',
                                            params={"page": 2})

    assert result.status_code == 200
    assert result.json()['page'] == 2
    assert len(result.json()['data']) != 0
    assert result.json() == S(list_user_schema)


def test_update_user_patch():
    name = "ivan"
    job = "qa"

    result: Response = reqres_session().patch(
        url="/api/users/",
        params={"id": 3},
        json={"name": name, "job": job}
    )

    assert result.status_code == 200
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert result.json() == S(update_user_patch_schema)


def test_delete_user():
    result = reqres_session().delete(url='/api/users/2')

    assert result.status_code == 204


def test_single_user():
    result: Response = reqres_session().get(url='/api/users/2')
    assert result.status_code == 200
    assert result.json()["data"]
    assert result.json()["data"]["id"] == 2
    assert result.json() == S(single_user_schema)