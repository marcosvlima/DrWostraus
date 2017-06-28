# DrWostraus

Um Chatterbot para tirar dúvidas sobre Inteligência Artificial

Este Chatterbot faz parte do trabalho de Inteligência Artificial do curso de
Ciência da Computação da Universidade Regional Integrada (URI) Campus Erechim.

Autor: Marcos Vinicius de Moura Lima

Orientador: Prof Marcos A. Lucas

Este chatterbot deverá ser executado em sistemas Linux com a versão do Python 2.7

## Faça Download do projeto

Olhe para o canto superior direito, aparecerá um botão para Download, você pode escolher
 
### Fazer donwload usando o git
Caso você tenha o git instalado basta digitar o seguinte comando:
 ```
 sudo git clone https://github.com/marcosvlima/DrWostraus.git
 ```
   
### Download .zip
Basta baixar o arquivo e extrair ele no seu computador

## Instalar Python versão 2.7

Primeiro você deve verificar se já possue o Python instalado, digite no seu terminal o seguinte comando:
```
python -V
```

Caso a resposta seja positiva, você pode passar para o próximo tópico.

### Dependencias python
```
sudo apt-get install build-essential checkinstall
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
```

### Baixe a versão 2.7.13

```
cd ~/Downloads/
wget https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tgz
```

- Extraia e vá para o diretório
```
tar -xvf Python-$version.tgz
cd Python-$version
```

- Instale o Python com estes comandos
```
./configure
make
sudo checkinstall
```

## Instalar dependencias do projeto
```
  sudo apt install python-pip
  sudo pip install flask
  sudo pip install aiml
```

## Para executar o chatterbot rode a seguinte linha de comando:
```
  sudo python main.py
```

Agora você deve ir para seu navegador e acessar o caminho que apareceu no web service. Provavelmente ser:
```
http://localhost:5000/
```

## Algumas sentenças mapeadas

- Definições de Inteligência Artificial
- As 4 abordagens da Inteligência Artificial
- A abordagem Agindo de Forma Humana
- A abordagem Agindo Racionalmente
- Quem foi Alan Turing
- O que é o Teste de Turing
- O que é um Agente Inteligênte
- Quais são as Aplicações de IA
- O que são Algoritmos Genéticos
- Redes Neurais
- Processos de aprendizagem
- Lógica Fuzzy
- Sistemas Multiagentes
- História da Inteligência Artificial
- Mineração de Dados
- Algoritmos de Busca
- E existem alguns easter eggs escondidos ;D"

OBS: Nesta lista não conta todas as sentenças mapeadas, mas sim as principais.

## Algumas considerações:

- Não digite as perguntas com ? (ponto de interrogação);


OBS: Este projeto é um protótipo, melhorias futuras podem ser implementadas,
qualquer sugestão ou crítica mande um email para marcoslima.xv@gmail.com
