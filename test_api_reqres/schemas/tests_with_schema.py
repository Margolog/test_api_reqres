import requests
from requests import Response
from voluptuous import Schema, PREVENT_EXTRA, Any, Optional
from pytest_voluptuous import S

from utils.base_user import reqres_session

create_user_schema = Schema(
    {
        "name": str,
        "job": str,
        "id": str,
        "createdAt": str
    },
    required=True,
    extra=PREVENT_EXTRA

)


def test_create_user_schema():
    name = 'Margo'
    job = 'QA'

    result: Response = reqres_session().post(url='/api/users',
                                             json={"name": name, "job": job})

    assert result.status_code == 201
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert isinstance(result.json()['id'], str)
    assert result.json() == S(create_user_schema)



update_user_schema = Schema(
    {
        "name": str,
        "job": str,
        "updatedAt": str
    },
    required=True,
    extra=PREVENT_EXTRA
)


def test_update_user_schema():
    name = 'Margo'
    job = 'Doctor'

    result: Response = reqres_session().put(url='/api/users/2',
                                            json={"name": name, "job": job})

    assert result.status_code == 200
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert result.json() == S(update_user_schema)

update_user_patch_schema = Schema(
        {
            "name": str,
            "job": str,
            "updatedAt": str,
        },
        required=True
    )


def test_update_user_patch():
    name = "Margo"
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


single_user_schema = Schema(
    {
        "data": {
            "id": int,
            "email": str,
            "first_name": str,
            "last_name": str,
            "avatar": str
        },
        "support": {
            "url": str,
            "text": str
        }
    },
    required=True,
    extra=PREVENT_EXTRA
)


def test_single_user_schema():
    result: Response = reqres_session().get(url='/api/users/2')
    assert result.status_code == 200
    assert result.json() == S(single_user_schema)