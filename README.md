# Script de Backup Docker

Script criado com o propósito de realizar backups de containers em ambiente de teste ou desenvolvimento. Para utilizar a documentação será necessario instalar o [Sphinx](https://www.sphinx-doc.org/), por esse motivo execulte o seguinte comando.

```
pip3 install -r requirements.txt
```

## Gerar documentação

Para gera a documentação, entre o diretorio doc e execulte o seguinte comando:

```
sphinx-apidoc -f -o ./source .. && make html
```
