def vigenere_encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = key.replace(" ", "").upper()

    ciphertext = ""
    key_index = 0
    key_length = len(key)

    for char in plaintext:
        if char.isalpha():
            pi = ord(char) - ord('A')
            ki = ord(key[key_index % key_length]) - ord('A')
            ci = (pi + ki) % 26
            cipher_char = chr(ci + ord('A'))
            ciphertext += cipher_char
            key_index += 1
        else:
            ciphertext += char

    return ciphertext


# Plaintext dari soal
plaintext = """Di halaman sekolah, siswa-siswi berkumpul untuk mengikuti upacara bendera. Barisan mereka rapi, berdiri tegap sambil menyanyikan lagu kebangsaan dengan penuh semangat. Bendera merah putih perlahan naik ke puncak tiang, berkibar di bawah langit biru cerah. Seorang guru memberikan amanat, mengingatkan pentingnya disiplin dan tanggung jawab. Di sudut lapangan, beberapa siswa berbisik, sesekali tersenyum mendengar pidato yang disampaikan. Angin pagi bertiup sejuk, membawa aroma rumput basah setelah hujan semalam. Setelah upacara selesai, mereka bergegas masuk kelas, siap menerima pelajaran dengan antusiasme baru."""

# Kunci dari soal
key = "ALDIT SHEVA OSYANA"

# Enkripsi
ciphertext = vigenere_encrypt(plaintext, key)

# Cetak ke terminal
print("Ciphertext:\n", ciphertext)

# Simpan ke file
with open("ciphertext_output.txt", "w") as file:
    file.write(ciphertext)

print("\n✅ Ciphertext berhasil disimpan ke file 'ciphertext_output.txt'")
