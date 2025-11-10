import re

def test_nim_ada():
    with open("ci-projectppl-dellon/index.html", "r", encoding="utf-8") as f:
        html = f.read()
    # Ganti 210411100XXX dengan NIM kamu
    assert re.search(r"230411100126", html), "NIM tidak ditemukan di halaman"

def get_identity():
    """Memastikan data identitas sesuai dengan validasi.py"""
    data = validasi.get_identity()
    assert data["nama"] == "Dellon Ismu Enyunanda"
    assert data["nim"] == "230411100126"
    assert data["program studi"] == "Teknik Informatika"
    assert data["fakultas"] == "Teknik"
    assert data["Universitas"] == "Universitas Trunojoyo Madura"