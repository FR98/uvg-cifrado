import time
from flask import Flask, request
import hmac

app = Flask(__name__)

SECRET_TOKEN = 'abmlw'


def strcmp(s1, s2):
    if len(s1) != len(s2):
        return False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            return False
        time.sleep(0.01)
    return True

def is_equal(s1, s2):
    if len(s1) != len(s2):
        return False

    result = 0
    for x, y in zip(s1, s2):
        x, y = ord(x), ord(y)
        result |= x ^ y
        time.sleep(0.01)
    return result == 0


@app.route("/")
def bad_protected():
    token = request.headers.get('X-TOKEN')

    if not token:
        return "Missing token", 401

    if strcmp(token, SECRET_TOKEN):
        return "Hello admin user! Here is your secret content"
    else:
        return "WHO ARE YOU? GET OUT!", 403

@app.route("/good-protection")
def protected():
    token = request.headers.get('X-TOKEN')

    if not token:
        return "Missing token", 401

    if hmac.compare_digest(token, SECRET_TOKEN):
        return "Hello admin user! Here is your secret content"
    else:
        return "WHO ARE YOU? GET OUT!", 403

@app.route("/good-protection-2")
def protected2():
    token = request.headers.get('X-TOKEN')

    if not token:
        return "Missing token", 401

    if is_equal(token, SECRET_TOKEN):
        return "Hello admin user! Here is your secret content"
    else:
        return "WHO ARE YOU? GET OUT!", 403


if __name__ == "__main__":
    app.run()
