# test_validasi.py

from validasi import get_identity

def test_identity_nim():
    data = get_identity()
    # Pastikan NIM tidak kosong
    assert data["nim"] != ""

def test_identity_nama():
    data = get_identity()
    # Pastikan nama sesuai
    assert data["nama"] == "Dellon Ismu Enyunanda"
