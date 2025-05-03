import json
import os

import requests

from fastapi import Depends, HTTPException, Header, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from urllib.request import urlopen
# Variables de entorno
AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")  # ej: dev-abc123.us.auth0.com
API_AUDIENCE = os.getenv("AUTH0_CLIENT_ID")  # ej: https://miapi.com
ALGORITHMS = ["RS256"]
# class AuthError(Exception):
#     def __init__(self, error: str, status_code: int = 401):
#         self.error = error
#         self.status_code = status_code

# def get_jwk():
#     jwks_url = f"https://{AUTH0_DOMAIN}/.well-known/jwks.json"
#     with urlopen(jwks_url) as response:
#         return json.load(response)

# def verify_id_token(token: str):
#     try:
#         jwks = get_jwk()
#         unverified_header = jwt.get_unverified_header(token)

#         print("🔍 Unverified JWT Header:", unverified_header)
#         print("🔑 Available JWKS keys:", [key["kid"] for key in jwks["keys"]])

#         if "kid" not in unverified_header:
#             raise AuthError("Token inválido: falta 'kid'")

#         rsa_key = next(
#             (key for key in jwks["keys"] if key["kid"] == unverified_header["kid"]),
#             None
#         )

#         if rsa_key:
#             payload = jwt.decode(
#                 token,
#                 rsa_key,
#                 algorithms=ALGORITHMS,
#                 audience=API_AUDIENCE,
#                 issuer=f"https://{AUTH0_DOMAIN}/"
#             )
#             return payload

#         raise AuthError("No se pudo encontrar la clave adecuada")

#     except JWTError as e:
#         raise AuthError(f"Error al decodificar el token: {str(e)}")
# security = HTTPBearer()

# def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
#     token = credentials.credentials
#     try:
#         user_payload = verify_id_token(token)
#         return user_payload
#     except AuthError as e:
#         raise HTTPException(status_code=e.status_code, detail=e.error)

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
    """Dependencia reutilizable para validar si el usuario tiene uno de los roles requeridos"""
    async def role_checker(
        credentials: HTTPAuthorizationCredentials = Depends(security),
        request: Request = None
    ):
        token = credentials.credentials
        profile = get_user_profile(token)

        # Leer roles desde custom claim
        user_roles = profile.get("https://securityApp.com/roles", [])

        if not isinstance(user_roles, list):
            raise HTTPException(status_code=403, detail="Formato de roles inválido")

        if not any(role in user_roles for role in required_roles):
            raise HTTPException(status_code=403, detail="No tienes permisos para acceder a este recurso")

        # Puedes guardar el perfil si lo necesitas más adelante
        request.state.user = profile
        return profile

    return Depends(role_checker)