import re
from validasi import get_identity

def test_nim():
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()
    assert re.search(r"230411100126", html), "NIM tidak ditemukan di halaman"

def test_nama():
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()
    assert re.search(r"Dellon Enyunanda", html), "Nama salah atau tidak ditemukan di halaman HTML"

def test_prodi():
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()
    assert re.search(r"Teknik Informatika", html), "Nama prodi salah atau tidak ditemukan di halaman HTML"

def test_fakultas():
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()
    assert re.search(r"Teknik", html), "Nama fakultas salah atau tidak ditemukan di halaman HTML"

def test_universitas():
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()
    assert re.search(r"Universitas Trunojoyo Madura", html), "Nama univ salah atau tidak ditemukan di halaman HTML"