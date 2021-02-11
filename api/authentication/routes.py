from os import stat
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.log import Identified
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import MultipleResultsFound

from api.database import get_session

from .models import User
from .schemas import NewUserSchema
from .security import (
    check_encryption,
    encrypt_password,
    generate_auth_token
)


router = APIRouter()


@router.post("/subscription")
async def subscribe(
    new_user: NewUserSchema,
    session: Session = Depends(get_session)
):
    user = session.query(User).filter_by(
        identifiant=new_user.identifiant
    ).one_or_none()

    if user is None:

        user_to_add = User(
            identifiant=new_user.identifiant,
            password=encrypt_password(new_user.password)
        )

        session.add(user_to_add)
        session.commit()

        return {'detail': 'User added'}
    else:
        raise HTTPException(
            status_code=409, 
            detail="identifiant already exist"
        )


@router.post("/authentication")
async def login(
    new_user: NewUserSchema,
    session: Session = Depends(get_session)
):
    try:
        user = session.query(User).filter_by(
            identifiant=new_user.identifiant
        ).one_or_none()

        if user is not None:

            if check_encryption(new_user.password, user.password):
                return {
                    'token': generate_auth_token({'id': user.id})
                }
            else:
                raise HTTPException(
                    status_code=404,
                    detail="User not found"
                )

        else:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

    except MultipleResultsFound:
        raise HTTPException(
            status_code=409,
            detail="Multiple users found"
        )
