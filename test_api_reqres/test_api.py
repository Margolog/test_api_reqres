from requests import Response

from test_api_reqres.schemas.tests_with_schema import *
from pytest_voluptuous import S


def test_create_user(reqres_session):
    name = 'Margo'
    job = 'QA'

    result: Response = reqres_session.post(url='/api/users',
                                           json={"name": name, "job": job})

    assert result.status_code == 201
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert isinstance(result.json()['id'], str)
    assert result.json() == S(create_user_schema)


def test_update_user(reqres_session):
    name = 'Margo'
    job = 'Doctor'

    result: Response = reqres_session.put(url='/api/users/2',
                                          json={"name": name, "job": job})

    assert result.status_code == 200
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert result.json() == S(update_user_schema)


def test_list_user(reqres_session):
    result: Response = reqres_session.get(url='/api/users?page=2',
                                          params={"page": 2})

    assert result.status_code == 200
    assert result.json()['page'] == 2
    assert len(result.json()['data']) != 0
    assert result.json() == S(list_user_schema)


def test_update_user_patch(reqres_session):
    name = "margo"
    job = "qa"

    result: Response = reqres_session.patch(
        url="/api/users/",
        params={"id": 3},
        json={"name": name, "job": job}
    )

    assert result.status_code == 200
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert result.json() == S(update_user_patch_schema)


def test_delete_user(reqres_session):
    result = reqres_session.delete(url='/api/users/2')

    assert result.status_code == 204


def test_single_user(reqres_session):
    result: Response = reqres_session.get(url='/api/users/2')
    assert result.status_code == 200
    assert result.json()["data"]
    assert result.json()["data"]["id"] == 2
    assert result.json() == S(single_user_schema)
