from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, request
from flaskr.exceptions import HttpException
from regex import regex
from flaskr.utils import encode_jwt, decode_jwt
from functools import wraps

password_strength_regex = regex.compile(r"^(?=.*[A-Z].*[A-Z])(?=.*[!@#$&*])(?=.*[0-9].*[0-9])(?=.*[a-z].*[a-z].*[a-z]).{8}$")
email_regex = regex.compile(r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])""")
bp = Blueprint("auth", __name__, url_prefix="/api/auth")

users = [
    {
        "user_id": 1,
        "email": "admin@admin.com",
        "password": generate_password_hash("admin")
    }
]

def token_required(fn):
    @wraps(fn)
    def token_wrap(**kwargs):
        global users
        auth: (str | None) = request.authorization.get()
        if auth == None:
            raise HttpException("Authorization token required", 401)
        if auth[0:6].lower() == "bearer":
            auth = auth[7:]
        result = decode_jwt(auth)
        if result == None:
            raise HttpException("Token expired or wrong signature", 401)
        email = result["email"]
        user_exits = [x for x in users if x["email"] == email]
        if len(user_exits) == 0:
            raise HttpException("The user does not exits", 401)
    return token_wrap
@bp.post("/signup")
def signup():
    global users
    
    body = request.json()
    if "password" not in body or "email" not in body:
        raise HttpException("Email and password fields are mandatory", 400)
    user_exits = [x for x in users if x["email"] == body["email"]]
    if len(user_exits) == 1:
        raise HttpException("There's an user with that email", 400)
    if email_regex.match(body["email"]) == None:
        raise HttpException("The email is not valid", 400)
    if password_strength_regex.match(body["passowrd"]) == None:
        raise HttpException("The password is weak", 400)
    password = generate_password_hash(body["password"])
    user_id = len(users) + 1
    users.append({
        "user_id": user_id,
        "email": body["email"],
        "password": password
    })
    jwt = encode_jwt(user_id, body["email"])
    return {
        "authType": "bearer",
        "authToken": jwt
    }


@bp.post("/signin")
def signin():
    global users
    body = request.json()
    if "password" not in body or "email" not in body:
        raise HttpException("Email and password fields are mandatory", 400)
    user_exits = [x for x in users if x["email"] == body["email"]]
    
    if len(user_exits) == 0:
        raise HttpException("There isn't an user with that email", 400)
    user = user_exits[0]
    result = check_password_hash(user["password"], body["password"])
    
    if result is False:
        raise HttpException("The password is wrong", 400)
    
    jwt = encode_jwt(user["user_id"], body["email"])
    return {
        "authType": "bearer",
        "authToken": jwt
    }