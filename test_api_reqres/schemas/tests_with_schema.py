from voluptuous import Schema, PREVENT_EXTRA, Any, Optional, All, Length

Support = Schema(
    {
        "url": str,
        "text": str
    }
)

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
Single_user = Schema(
    {
            "id": int,
            "email": str,
            "first_name": str,
            "last_name": str,
            "avatar": str
    })


single_user_schema = Schema(
    {
        "data": Single_user,
        "support": Support
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

list_user_schema = Schema(
    {
        "page": 2,
        "per_page": 6,
        "total": 12,
        "total_pages": 2,
        "data": All([List_User], Length(min=1)),
        "support": Support
    },
    required=True,
    extra=PREVENT_EXTRA)
