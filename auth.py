from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from config import SECRET_KEY
from security import failed_attempts, is_rate_limited, is_blocked, block_ip

users = {
    "admin": generate_password_hash("Sumitraj@1234")
}


# =========================
# LOGIN FUNCTION
# =========================
def login_user(ip, username, password, mode):

    # 💣 HACKING MODE
    if mode == "HACKING":
        return {
            "message": "HACKING MODE ACTIVE (Simulation Only)"
        }

    # 🛡️ DEFENCE MODE
    if mode == "DEFENCE":

        if is_blocked(ip):
            return {"message": "IP blocked"}, 403

        if is_rate_limited(ip):
            block_ip(ip)
            return {"message": "Too many requests"}, 429

    # ❌ USER CHECK
    if username not in users:
        return {"message": "Invalid username"}, 401

    # 🔐 PASSWORD CHECK
    if check_password_hash(users[username], password):

        failed_attempts[ip] = 0

        token = jwt.encode({
            "user": username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, SECRET_KEY, algorithm="HS256")

        return {
            "message": "Login successful",
            "token": token
        }

    # ❌ FAILED LOGIN
    failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

    if failed_attempts[ip] > 10:
        block_ip(ip)

    return {"message": "Invalid password"}, 401