from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import secrets
import base64

# 1. Geração de chaves RSA
def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# 2. Função para criptografar a mensagem usando AES-GCM e RSA
def encrypt_message(message, rsa_public_key):
    # Criação de uma chave AES-256 aleatória
    aes_key = get_random_bytes(32)
    print(f'\n Essa é a chave AES: \033[0;33;40m {aes_key} \033[0;37;40m')

    # Geração de um nonce (IV) aleatório de 12 bytes (recomendado para o método GCM)
    nonce = secrets.token_bytes(12)
    print(f'\n Este é o nonce (IV): \033[0;33;40m {nonce} \033[0;37;40m')

    # Criptografia da mensagem usando AES-GCM
    #O GCM fornece autenticação integrada. Em vez de apenas criptografar, usamos encrypt_and_digest() para obter o texto cifrado criptografado e uma tag de autenticação.
    cipher_aes = AES.new(aes_key, AES.MODE_GCM, nonce=nonce)
    ciphertext, tag = cipher_aes.encrypt_and_digest(message.encode())

    # Criptografia da chave AES usando RSA
    rsa_key = RSA.import_key(rsa_public_key)
    print(f'\n Essa é a chave RSA pública: \033[0;33;40m {rsa_public_key} \033[0;37;40m')
    cipher_rsa = PKCS1_OAEP.new(rsa_key)
    encrypted_aes_key = cipher_rsa.encrypt(aes_key)

    # Combinação do nonce, chave AES criptografada, ciphertext e tag
    encrypted_data = base64.b64encode(nonce + encrypted_aes_key + ciphertext + tag).decode()
    return encrypted_data

# 3. Função para descriptografar a mensagem
def decrypt_message(encrypted_data, rsa_private_key):
    encrypted_data = base64.b64decode(encrypted_data)

    # Extrai o nonce, chave AES criptografada, ciphertext e tag
    nonce = encrypted_data[:12]
    encrypted_aes_key = encrypted_data[12:12 + 256]  # 256 bytes fpara RSA-2048
    ciphertext = encrypted_data[12 + 256:-16]  # Tudo menos a tag
    tag = encrypted_data[-16:]  # Ultimos 16 bytes são a tag


    # Descriptografia da chave AES usando RSA
    rsa_key = RSA.import_key(rsa_private_key)
    cipher_rsa = PKCS1_OAEP.new(rsa_key)
    aes_key = cipher_rsa.decrypt(encrypted_aes_key)


    # Descriptografia da mensagem usando AES-GCM
    cipher_aes = AES.new(aes_key, AES.MODE_GCM, nonce=nonce)
    try:
       decrypted_message = cipher_aes.decrypt_and_verify(ciphertext, tag).decode()
       return decrypted_message
    except ValueError:
        return "\033[1;31;40m Invalid Tag."

# Exemplo de uso
private_key, public_key = generate_rsa_keys()
message = input("\033[0;37;40m Insira sua mensagem:" )

# Criptografia
encrypted_data = encrypt_message(message, public_key)
print(f"\n Mensagem Criptografada: \033[1;31;40m {encrypted_data} \033[0;37;40m \n ")

# Descriptografia
decrypted_message = decrypt_message(encrypted_data, private_key)
print(f"Mensagem Descriptografada: \033[1;32;40m {decrypted_message}")
