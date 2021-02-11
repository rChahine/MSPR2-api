from fastapi import Header, Depends, HTTPException
from sqlalchemy.orm.session import Session

from api.authentication.security import decode_auth_token
from api.authentication.models import User
from api.database import get_session


def get_user(
    authorization: str = Header(...),
    session: Session = Depends(get_session)
) -> User:

    """ Return user if token is valid """
    
    payload = decode_auth_token(authorization)
    user = session.query(User).filter_by(
        id=payload["id"]
    ).one_or_none()

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User must be connected to access this route"
        )
    else:
        return user
