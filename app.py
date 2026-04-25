from flask import Flask, request, jsonify
from auth import login_user
from config import MODE

app = Flask(__name__)

# =========================
# CHANGE MODE
# =========================
@app.route('/mode', methods=['POST'])
def change_mode():
    global MODE
    data = request.json

    MODE = data.get("mode", "NORMAL").upper()

    return jsonify({"message": f"Mode set to {MODE}"})


# =========================
# HOME
# =========================
@app.route('/')
def home():
    return jsonify({
        "message": "Cybersecurity Lab Running",
        "mode": MODE
    })


# =========================
# LOGIN API
# =========================
@app.route('/login', methods=['POST'])
def login():

    ip = request.remote_addr
    data = request.json

    username = data.get("username")
    password = data.get("password")

    result = login_user(ip, username, password, MODE)

    return jsonify(result)


# =========================
# DASHBOARD
# =========================
@app.route('/dashboard')
def dashboard():

    token = request.headers.get("token")

    if not token:
        return jsonify({"message": "Token missing"}), 401

    try:
        import jwt
        from config import SECRET_KEY

        data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

        return jsonify({
            "message": f"Welcome {data['user']}",
            "mode": MODE
        })

    except:
        return jsonify({"message": "Invalid token"}), 403


# =========================
# RUN SERVER
# =========================
if __name__ == "__main__":
    app.run(debug=True)