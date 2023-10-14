import socket
import base64
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto import Random

def encryptMessage(a_message, publicKey):
    cipher_rsa = PKCS1_OAEP.new(publicKey)
    b_message = bytes(a_message, 'utf-8')
    encrypted = cipher_rsa.encrypt(b_message)
    encoded_msg = base64.b64encode(encrypted)
    return encoded_msg

def decryptMessage(encoded_encrypt_msg, privateKey):
    cipher_rsa = PKCS1_OAEP.new(privateKey)
    decoded_msg = base64.b64decode(encoded_encrypt_msg)
    msg = cipher_rsa.decrypt(decoded_msg)
    utf_8_msg = msg.decode('utf-8')
    return utf_8_msg

def main():
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect(('localhost', 12345))
    print("Conectado ao servidor!")

    # Receber chave pública do servidor
    chave_publica_pem = cliente_socket.recv(4096)
    chave_publica = RSA.import_key(chave_publica_pem)

    # Receber chave privada do servidor
    chave_privada_pem = cliente_socket.recv(4096)
    chave_privada = RSA.import_key(chave_privada_pem)

    # Enviar e receber mensagens em loop
    while True:
        # Ler mensagem do usuário
        mensagem = input("Clinte diz: ")

        # Criptografar mensagem com chave pública do servidor
        mensagem_cifrada = encryptMessage(mensagem, chave_publica)

        # Enviar mensagem criptografada para o servidor
        cliente_socket.sendall(mensagem_cifrada)

        # Receber resposta do servidor
        mensagem_cifrada = cliente_socket.recv(4096).decode()
        mensagem_descriptografada = decryptMessage(mensagem_cifrada, chave_privada)
        print("Servidor diz: " + mensagem_descriptografada)

        # Encerrar a conexão se a mensagem for "sair"
        if mensagem.lower() == "sair":
            break

    cliente_socket.close()

if __name__ == "__main__":
    main()
