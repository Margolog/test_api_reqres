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

update_user_schema = Schema(
    {
        "name": str,
        "job": str,
        "updatedAt": str
    },
    required=True,
    extra=PREVENT_EXTRA
)

update_user_patch_schema = Schema(
    {
        "name": str,
        "job": str,
        "updatedAt": str,
    },
    required=True
)

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

List_User = Schema(
    {
        "id": int,
        "email": str,
        "first_name": str,
        "last_name": str,
        "avatar": str
    })
Support_User = Schema(
    {
        "url": str,
        "text": str
    }
)

list_user_schema = Schema({
    "page": 2,
    "per_page": 6,
    "total": 12,
    "total_pages": 2,
    "data": [List_User],
    "support": Support_User
},
    required=True,
    extra=PREVENT_EXTRA)
