# F14_help

def help(is_login,role):
  # Ketika belum login role sebarang
  # Ketika sudah login role terdefinisi sebagai admin atau user
  print("============ HELP ============")
  print("help - panduan penggunaan aplikasi")
  if is_login:
    if role == "admin":
      print("1. login - Untuk melakukan login ke dalam sistem")
      print("2. register - Untuk melakukan registrasi user baru")
      print("3. tambah_game - Untuk menambah game baru pada toko")
      print("4. ubah_game - Untuk mengubah informasi sebuah game pada toko")
      print("5. ubah_stok - Untuk mengubah stok sebuah game pada toko")
      print("6. list_game_toko - Untuk melihat list game yang dijual pada toko")
      print("7. search_game_at_store - Untuk mencari game pada toko")
      print("8. top_up - Untuk menambahkan saldo pengguna")
      print("9. save - Untuk penyimpanan data")
      print("10. exit - keluar dari aplikasi binomo")

    elif role == "user":
      print("1. login - Untuk melakukan login ke dalam sistem")
      print("2. list_game_toko - Untuk melihat list game yang dijual pada toko")
      print("3. buy_game - Untuk membeli game pada toko")
      print("4. list_game - Untuk melihat daftar game anda")
      print("5. search_my_game - Untuk mencari game dari daftar game anda")
      print("6. search_game_at_store - Untuk mencari game pada toko")
      print("7. riwayat - Untuk melihat riwayat pembelian game anda")
      print("8. save - Untuk penyimpanan data")
      print("9. exit - keluar dari aplikasi binomo")
      
  else:
    print("Anda belum login!")
    print("login - Untuk melakukan login ke dalam sistem")
