"""
Program Sederhana: Penghitung Total Hasil Panen
"""

def hitung_total_panen(daftar_berat):
    """
    Menghitung total hasil panen (dalam kg) dari daftar berat per petak/keranjang.
    """
    return sum(daftar_berat)


def hitung_harga_setelah_diskon(total_harga, persen_diskon):
    """
    Menghitung harga akhir setelah dikurangi diskon.
    persen_diskon dalam bentuk persen, misalnya 10 untuk 10%.
    """
    if not (0 <= persen_diskon <= 100):
        raise ValueError("Persen diskon harus di antara 0 dan 100")
    potongan = total_harga * (persen_diskon / 100)
    return total_harga - potongan


def main():
    daftar_berat = [120.5, 98.0, 150.25, 87.75]  # contoh data berat panen (kg)
    harga_per_kg = 5000  # contoh harga per kg (Rupiah)
    persen_diskon = 10   # contoh diskon untuk pembelian dalam jumlah besar

    total = hitung_total_panen(daftar_berat)
    total_harga = total * harga_per_kg
    harga_akhir = hitung_harga_setelah_diskon(total_harga, persen_diskon)

    print("=== Laporan Hasil Panen ===")
    for i, berat in enumerate(daftar_berat, start=1):
        print(f"Petak {i}: {berat} kg")
    print(f"Total Hasil Panen: {total} kg")
    print(f"Total Harga (sebelum diskon): Rp{total_harga:,.0f}")
    print(f"Diskon: {persen_diskon}%")
    print(f"Harga Akhir (setelah diskon): Rp{harga_akhir:,.0f}")


if __name__ == "__main__":
    main()
