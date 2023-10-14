# Chat Criptografado com Python e Sockets

Este é um exemplo de um chat criptografado em Python usando a biblioteca `Crypto` para criptografia assimétrica e sockets para comunicação entre cliente e servidor. O chat permite que dois usuários, identificados como **Robson Sousa da Silva** e **Rubens Abraão da Silva Sousa**, se comuniquem de forma segura usando criptografia RSA.

## Requisitos

- Python 3.x
- Biblioteca `cryptography` para criptografia simétrica: Você pode instalá-la usando o comando `pip install cryptography`.

## Como Funciona

O sistema consiste em dois scripts Python: `Cliente.py` e `Servidor.py`.

### Servidor

O arquivo `Servidor.py` é responsável por iniciar um servidor que espera por conexões de clientes. Quando um cliente se conecta, o servidor envia sua chave pública para o cliente. O servidor também recebe mensagens criptografadas do cliente, descriptografa-as usando sua chave privada e imprime o conteúdo das mensagens na tela.

### Cliente

O arquivo `Cliente.py` é responsável por se conectar ao servidor. Quando conectado, o cliente recebe a chave pública do servidor e a usa para criptografar suas mensagens antes de enviá-las. O cliente também descriptografa mensagens recebidas do servidor usando sua chave privada e imprime o conteúdo das mensagens na tela.

## Como Usar

1. **Clone o Repositório:**

   ```
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Execute o Servidor:**

   ```
   python Servidor.py
   ```

   O servidor será iniciado e ficará aguardando por conexões de clientes.

3. **Execute o Cliente:**

   ```
   python Cliente.py
   ```

   O cliente se conectará ao servidor. Após a conexão bem-sucedida, você pode digitar mensagens no cliente. As mensagens serão criptografadas e enviadas ao servidor, que as descriptografará e imprimirá na tela.

4. **Para Sair:**

   Para encerrar o chat, basta digitar "sair" em qualquer um dos lados (cliente ou servidor). O programa será encerrado tanto para o cliente quanto para o servidor.

## Criadores

- **Robson Sousa da Silva**
- **Rubens Abraão da Silva Sousa**

Sinta-se à vontade para explorar e modificar o código conforme suas necessidades! Se tiver alguma dúvida ou encontrar problemas, não hesite em entrar em contato com os criadores. Esperamos que este exemplo seja útil para você!
