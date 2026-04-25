from time import time

request_log = {}
blocked_ips = {}
failed_attempts = {}


# =========================
# RATE LIMIT
# =========================
def is_rate_limited(ip):
    now = time()

    if ip not in request_log:
        request_log[ip] = []

    request_log[ip] = [t for t in request_log[ip] if now - t < 60]

    if len(request_log[ip]) >= 5:
        return True

    request_log[ip].append(now)
    return False


# =========================
# IP BLOCK CHECK
# =========================
def is_blocked(ip):
    if ip in blocked_ips:
        if time() < blocked_ips[ip]:
            return True
    return False


# =========================
# BLOCK IP
# =========================
def block_ip(ip, seconds=300):
    blocked_ips[ip] = time() + seconds