# list semua barang yg tersedia
items = {
    "susu": 50000,
    "daging": 20000,
    "lampu": 15000,
    "masker": 25000,
    "apel": 30000,
}

# list barang promo
promotions = {"susu": 50000, "masker": 25000}

def display_menu():
    print("Selamat Datang di Supermarket!")
    print("Selamat Belanja")
    print("")
    print("Berikut merupakan beberapa barang promosi disini!")
    for item, harga in promotions.items():
        print(f"{item}: Rp. {harga:,.0f}".replace(',', '.'))

    print("")


def show_items():
    choice = input("Apakah Anda ingin melihat semua barang (A) atau hanya barang promosi (P)? ")
    if choice.lower() == "p":
        print("Berikut ini adalah barang kami yang sedang dalam promo:")
        for item, harga in promotions.items():
            print(f"{item}: Rp. {harga:,.0f}".replace(',', '.'))
    else:
        print("Berikut ini adalah semua barang yang tersedia disini:")
        for item, harga in items.items():
            print(f"{item}: Rp. {harga:,.0f}".replace(',', '.'))


def calculate_total(item_yang_dibeli):
    total = 0
    print("")
    print("Berikut adalah barang yang telah Anda pilih:")
    for item_with_quantity in item_yang_dibeli:
        jumlah_item, item_name = item_with_quantity.split(" ")
        if item_name in promotions:
            item_harga = promotions[item_name]
            print(
                f"{item_name} (PROMO!) Rp. {item_harga:,.0f} x {jumlah_item}: Rp. {item_harga * int(jumlah_item):,.0f}".replace(',', '.')
            )
            total += item_harga * int(jumlah_item)
        else:
            item_harga = items[item_name]
            print(
                f"{item_name} Rp. {item_harga:,.0f} x {jumlah_item}: Rp. {item_harga * int(jumlah_item):,.0f}".replace(',', '.')
            )
            total += item_harga * int(jumlah_item)
    print("")
    print(f"Total harga: Rp. {total:,.0f}".replace(',', '.'))


# menampilkan ucapan selamat datang dan barang promo
display_menu()

# menampilkan hasil barang yang diinginkan user
show_items()

# input pembelian user
print("")
print("Contoh input Pembelian: 3 daging, 4 apel, 3 susu, dst.")
item_yang_dibeli = input("Apa yang ingin Anda beli? (Pisahkan tiap barang dengan koma dan spasi) ").split(
    ", "
)

# function penghitungan total harga dan detail barang
calculate_total(item_yang_dibeli)
print("Terima kasih telah berbelanja disini!")
