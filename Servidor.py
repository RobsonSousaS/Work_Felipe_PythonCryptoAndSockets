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

def generateKeys():
    tamanho = 256*4  #1024 bits
    privateKey = RSA.generate(tamanho, Random.new().read)
    publicKey = privateKey.publickey()
    return privateKey, publicKey

def main():
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind(('localhost', 12345))
    servidor_socket.listen(1)
    print("Servidor esperando por conexões...")

    privateKey, publicKey = generateKeys()

    while True:
        cliente_socket, addr = servidor_socket.accept()
        print("Cliente conectado!")

        # Enviar chave pública para o cliente
        chave_publica = publicKey.export_key()
        cliente_socket.sendall(chave_publica)

        # Enviar chave privada para o cliente
        chave_privada = privateKey.export_key()
        cliente_socket.sendall(chave_privada)

        # Receber a primeira mensagem do cliente
        mensagem_cifrada = cliente_socket.recv(4096).decode()
        mensagem_descriptografada = decryptMessage(mensagem_cifrada, privateKey)
        print("Cliente diz: " + mensagem_descriptografada)

        while True:
            # Ler mensagem do servidor
            mensagem_resposta = input("Digite uma mensagem para enviar ao cliente: ")

            # Criptografar mensagem com chave pública do cliente
            mensagem_resposta_cifrada = encryptMessage(mensagem_resposta, publicKey)

            # Enviar mensagem criptografada para o cliente
            cliente_socket.sendall(mensagem_resposta_cifrada)

            # Receber mensagem cifrada do cliente
            mensagem_cifrada = cliente_socket.recv(4096).decode()

            # Descriptografar mensagem com chave privada do servidor
            mensagem_descriptografada = decryptMessage(mensagem_cifrada, privateKey)
            print("Cliente diz: " + mensagem_descriptografada)

            # Encerrar a conexão se a mensagem for "sair"
            if mensagem_resposta.lower() == "sair" or mensagem_descriptografada.lower() == "sair":
                break

        cliente_socket.close()

if __name__ == "__main__":
    main()
