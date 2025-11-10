import re
from ci_projectppl_dellon.validasi import get_identity

def test_nim():
    with open("ci_projectppl_dellon/index.html", "r", encoding="utf-8") as f:
        html = f.read()
    assert re.search(r"230411100111", html), "NIM tidak ditemukan di halaman"

def test_nama():
    with open("ci_projectppl_dellon/index.html", "r", encoding="utf-8") as f:
        html = f.read()
    assert re.search(r"Dellon Enyunanda", html), "Nama salah atau tidak ditemukan di halaman HTML"

def test_prodi():
    with open("ci_projectppl_dellon/index.html", "r", encoding="utf-8") as f:
        html = f.read()
    assert re.search(r"Teknika Informatika", html), "Nama prodi salah atau tidak ditemukan di halaman HTML"

def test_fakultas():
    with open("ci_projectppl_dellon/index.html", "r", encoding="utf-8") as f:
        html = f.read()
    assert re.search(r"Teknika", html), "Nama fakultas salah atau tidak ditemukan di halaman HTML"

def test_universitas():
    with open("ci_projectppl_dellon/index.html", "r", encoding="utf-8") as f:
        html = f.read()
    assert re.search(r"Universitas Trunojoyo Maduraa", html), "Nama univ salah atau tidak ditemukan di halaman HTML"