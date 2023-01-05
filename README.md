# basic_login_system

## Atividade de programação web 05-01-23

A tarefa consiste em fazer um sistema básico de login,porém, implementei algumas funcionalidades a mais.<br>
Além disso, ao invés de utilizar Java Script, optei por utilizar o microframework web Python, chamado Flask: https://flask.palletsprojects.com/en/2.2.x/


### Login route ( /login )

![image](https://user-images.githubusercontent.com/88283829/210840573-3d27d1f2-4caf-4b1e-9642-aecc1d351aab.png)


### Signup route  ( /signup )

![image](https://user-images.githubusercontent.com/88283829/210840082-08d0c486-8773-42ff-a138-0bc16e5cb829.png)


### Invalid route 

![image](https://user-images.githubusercontent.com/88283829/210835842-5e2898f4-aa69-41d9-a6d8-67943c773382.png)


### Login success ( /profile )

![image](https://user-images.githubusercontent.com/88283829/210840334-d380b595-1f62-4d36-8a64-1957781c4a4f.png)


### Possíveis status code tratados, no backend, do protocolo HTTP:

✔️ [Status 200] Success<br>
👌  [Status 201] Update<br>
🚗 [Status 302] Redirect<br>
❌ [Status 404] Not found<br>

### database utilizado:

🗳️ SQLite3


### Tecnologias Frontend:

5️⃣ HTML5 <br>
🖌️ CSS3 <br>

### Tecnologias Backend:

🐍 Python3.10.5

### Testado no Browser:

🦊 Firefox

### Sistema Operacional:

🐉  Debian (Linux)

### Dependências e versões disponíveis no arquivo requirements.txt, que se encontra neste diretório.

Para instalar:

    pip install -r requirements.txt
    
 Feito isso, as dependências necessárias serão baixadas.Contudo, é importante ter algum gerenciador de pacotes, no caso, utilizo o pip3.


### Criar o banco de dados, se desejar:

![image](https://user-images.githubusercontent.com/88283829/210887065-b399a0a7-d2d7-4508-af2b-d25ab6e06fc9.png)


### Como executar localmente:

Apontar a variável de ambiente para o arquivo main.py

    $env:FLASK_APP="main.py"
    
Executar:

     flask run --reload
     
### Patterns utilizado: 

<b>Factory</b> <br>

O Factory Method é um padrão criacional de projeto que fornece uma interface para criar objetos em uma superclasse, mas permite que as subclasses alterem o tipo de objetos que serão criados


### Diagrama do Database:

![image](https://user-images.githubusercontent.com/88283829/210848832-463e8988-6994-4e44-8adb-dae146835db2.png)



