import re

def test_nim_ada():
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()
    # Ganti 210411100XXX dengan NIM kamu
    assert re.search(r"210411100XXX", html), "NIM tidak ditemukan di halaman"
