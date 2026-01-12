from fastapi import Depends, HTTPException, status
from core.dependencies import get_current_user
from core.roles import Role


def require_role(*allowed_roles: Role):
    def checker(user=Depends(get_current_user)):
        if user["role"] not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions",
            )
        return user

    return checker
