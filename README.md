# 🔐 Secure Login System (Flask + JWT + Rate Limiting)

A secure authentication system built using **Flask**, demonstrating real-world cybersecurity concepts like password hashing, JWT authentication, rate limiting, and attack protection mechanisms.

This project simulates how real backend systems protect user login APIs from brute force and abuse.


<img width="1214" height="439" alt="SECURE LOGIN SYSTEM " src="https://github.com/user-attachments/assets/31925e7e-2e68-4099-b8c8-16dfd1e480fc" />

<img width="1214" height="439" alt="SECURE LOGIN SYSTEM " src="https://github.com/user-attachments/assets/a2934f6a-f776-4395-a106-65c4441390c1" />

<img width="1214" height="439" alt="SECURE LOGIN SYSTEM " src="https://github.com/user-attachments/assets/9733a59b-968e-45ad-8a34-694b1aa6203a" />

<img width="1214" height="439" alt="SECURE LOGIN SYSTEM " src="https://github.com/user-attachments/assets/78b6ed45-709b-409f-ae18-e9b463b833cb" />




---

# 🚀 Features

- 🔐 Secure password hashing (Werkzeug)
- 🔑 JWT-based authentication
- 🛡️ Rate limiting (anti brute-force protection)
- 🚫 IP blocking system
- 📊 Login attempt logging
- 🔒 Protected dashboard route
- ⏳ Token expiration system

---

# 🧠 Security Concepts Implemented

- Authentication & Authorization
- Brute force attack prevention
- Time-based rate limiting (sliding window)
- JSON Web Token (JWT) security
- Password hashing (no plain text storage)
- Basic intrusion detection (logging system)
- IP-based blocking

---

# 📁 Project Structure

secure-login-lab/
│
├── app.py              # Main Flask backend
├── brute.py            # Attack simulation script
├── security.log        # Auto-generated logs
├── requirements.txt    # Dependencies
├── README.md           # Documentation

---

# ⚙️ Installation

git clone https://github.com/your-username/secure-login-lab.git

cd secure-login-lab

pip install flask werkzeug pyjwt

---

# ▶️ Run Project

python app.py

Server runs at:
http://127.0.0.1:5000/

---

# 🔐 API Endpoints

## Home
GET /

Response:
Secure Login System Running

---

## Login
POST /login

Body:
{
  "username": "admin",
  "password": "your_password"
}

Response:
{
  "message": "Login successful",
  "token": "JWT_TOKEN"
}

---

## Dashboard (Protected)
GET /dashboard

Headers:
token: YOUR_JWT_TOKEN

Response:
{
  "message": "Welcome admin to secure dashboard"
}

---

# 💣 Attack Simulation

python brute.py

Simulates:
- brute force attacks
- password guessing
- API abuse

---

# 🛡️ Security Features

## Rate Limiting
- 5 requests per minute per IP
- prevents brute force attacks

## IP Blocking
- blocks abusive IP for 5 minutes

## Password Security
- hashed passwords only

## JWT Authentication
- secure token-based login system

## Logging System
- tracks all login attempts

---

# 🧠 Learning Outcome

- How login systems work internally
- How hackers perform brute force attacks
- How APIs are secured in real systems
- Backend security architecture basics

---

# 🚀 Future Improvements

- MongoDB integration
- Refresh token system
- OTP / 2FA authentication
- Redis-based rate limiting
- Admin security dashboard

---

# 👨‍💻 Author

Sumit Kumar  
Cybersecurity & AI Enthusiast  

---

# ⚠️ Disclaimer

For educational purposes only. Do not use for illegal activities.
