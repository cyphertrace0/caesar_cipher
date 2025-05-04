def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# İstifadəçi ilə qarşılıqlı
print("Sezar Şifrələmə Aləti 🔐")
choice = input("1. Şifrələ\n2. Şifrəni aç\nSeçim: ")
message = input("Mətni daxil et: ")
shift = int(input("Neçə hərf dəyişsin? (məs: 3): "))

if choice == "1":
    encrypted = caesar_encrypt(message, shift)
    print("🔒 Şifrələnmiş mətn:", encrypted)
elif choice == "2":
    decrypted = caesar_decrypt(message, shift)
    print("🔓 Şifrəsi açılmış mətn:", decrypted)
else:
    print("Yanlış seçim etdin.")
