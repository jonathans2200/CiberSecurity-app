import json
import os
import requests
from jose import jwt
from fastapi import Depends, HTTPException, Header
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose.exceptions import JWTError, ExpiredSignatureError
from urllib.request import urlopen
# Variables de entorno
AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")  # ej: dev-abc123.us.auth0.com
API_AUDIENCE = os.getenv("AUTH0_CLIENT_ID")  # ej: https://miapi.com
ALGORITHMS = ["RS256"]
class AuthError(Exception):
    def __init__(self, error: str, status_code: int = 401):
        self.error = error
        self.status_code = status_code

def get_jwk():
    jwks_url = f"https://{AUTH0_DOMAIN}/.well-known/jwks.json"
    with urlopen(jwks_url) as response:
        return json.load(response)

def verify_id_token(token: str):
    try:
        jwks = get_jwk()
        unverified_header = jwt.get_unverified_header(token)

        print("🔍 Unverified JWT Header:", unverified_header)
        print("🔑 Available JWKS keys:", [key["kid"] for key in jwks["keys"]])

        if "kid" not in unverified_header:
            raise AuthError("Token inválido: falta 'kid'")

        rsa_key = next(
            (key for key in jwks["keys"] if key["kid"] == unverified_header["kid"]),
            None
        )

        if rsa_key:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer=f"https://{AUTH0_DOMAIN}/"
            )
            return payload

        raise AuthError("No se pudo encontrar la clave adecuada")

    except JWTError as e:
        raise AuthError(f"Error al decodificar el token: {str(e)}")
security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        user_payload = verify_id_token(token)
        return user_payload
    except AuthError as e:
        raise HTTPException(status_code=e.status_code, detail=e.error)
