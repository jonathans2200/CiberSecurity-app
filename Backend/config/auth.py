import json
import os

import requests

from fastapi import Depends, HTTPException, Header, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from urllib.request import urlopen

AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")  # ej: dev-abc123.us.auth0.com
API_AUDIENCE = os.getenv("AUTH0_CLIENT_ID")  # ej: https://miapi.com
ALGORITHMS = ["RS256"]

security = HTTPBearer()

def get_user_profile(access_token: str):
    """Obtiene el perfil del usuario desde /userinfo con el token"""
    url = f"https://{AUTH0_DOMAIN}/userinfo"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print("🔍 User Profile:", response.json())
        return response.json()
    raise HTTPException(status_code=401, detail="Token inválido o expirado")

def require_roles(*required_roles: str):
  
    async def role_checker(
        credentials: HTTPAuthorizationCredentials = Depends(security),
        request: Request = None
    ):
        token = credentials.credentials
        profile = get_user_profile(token)

     
        user_roles = profile.get("https://securityApp.com/roles", [])

        if not isinstance(user_roles, list):
            raise HTTPException(status_code=403, detail="Formato de roles inválido")

        if not any(role in user_roles for role in required_roles):
            raise HTTPException(status_code=403, detail="No tienes permisos para acceder a este recurso")


        request.state.user = profile
        return profile

    return Depends(role_checker)