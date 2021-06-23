def solution(w, h):
    white = w + h - gcd(max(w, h), min(w, h))

    gray = w * h - white

    return gray


def gcd(n1, n2):
    if n1 % n2 == 0:
        return n2

    return gcd(n2, n1 % n2)
