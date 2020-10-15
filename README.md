# Coletor Snap7 (Siemens) em python
- coleta dados referentes temperatura, pressão, energia, acionamentos, erros e etc
![alt text](https://github.com/AlexsanderSouza/historiador-sonda-python/blob/master/Screenshot_146.png?raw=true)
## Instalação python e mysql connector
- executar exe: python 2.7.16 32bits
- marque a opção para adicionar o python nas variaveis de ambiente do windows
- executar exe: mysql-connector...
## metodo online:
- copiar pasta "snap" para disco local e adicionar o caminho nas variaveis de ambientes do windows
- instalar snap7
```bash
pip install python-snap7
```
- influxdb
```bash
pip install influxdb
```
## metodo offline:
- copiar pasta "snap" para disco local e adicionar o caminho nas variaveis de ambientes do windows
- na pasta "python-snap7-master" executar o comando: 
```bash
python setup.py install
```
- instalar bibliotecas e influx db
- dentro da pasta influxdb execute no cmd:
```bash
pip install --no-index --find-links="./pkg" -r requirements.txt
python setup.py install
```
## Configuração Collector
- abra o arquivo Colletor.py e configure as seguintes linhas:
```bash
#Variaveis iniciais
errorSiemens = 3 #Quantidade de erros de conexao permitidos antes de reiniciar software
time_cicle = 1 #Tempo de ciclo da leitura em segundos
time_influx = 1 #Tempo maximo sem gravacao no influx em segundos 

# Configuracao do PLC
ipSiemens = '192.168.1.1'

# Configuracao Influx
ipInfludb ="192.168.0.200"
portInfluxdb = 8086
userInflux ="userExemple"
passwordInflux = "passwordExemple"
bdInflux ="nameDB"
```

## Adicionar collector como serviço
- extraia o arquivo do nssm (encontrado na pasta install)
- abra o terminal dentro da pasta onde esta o aplicativo nssm.exe e execute o comando:
```bash
nssm install flexCollector
```
- na janela que abriu escolha a pasta e selecione start_collector.cmd
- na guia details coloque o display name desejado.
- reinicie o windows ou inicie o serviço manualmente
