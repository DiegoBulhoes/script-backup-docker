# Script de Backup Docker(Desenvolvendo)

Script criado com o propósito de realizar backups de containers em ambiente de teste ou desenvolvimento. Para utilizar a documentação será necessario instalar o [Sphinx](https://www.sphinx-doc.org/), por esse motivo execulte o seguinte comando.

```
pip3 install -r requirements.txt
```

## Gerar documentação

Para gera a documentação, entre o diretorio doc e execulte o seguinte comando:

```
sphinx-apidoc -f -o ./source .. && make html
```

## Backup full

Para realizar o backup de todos os containers, tanto que está no status _up_ ou _down_ basta executar:

```
python3 main.py -r full -p ./bk
```

## Backup de um container específico

Para realizar o backup de um container específico basta executar

```
python3 main.py -r backup -c <ID_CONTAINER>  -p './backup'
```

## Restaurar o backup de um container específico

Para realizar o backup de um container específico basta executar

```
python3 main.py -r retore -c <ID_CONTAINER>  -t container -p ./
```
