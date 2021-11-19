# python-clean-architecture
Python Clean Architecture Example

# Orientacoes
pylint (baseado no guia de estilo PEP 8) - verifica somente em tempo de desenvolvimento
  - pylint asgi.py weather

  - pylint --generate-rcfile > .pylintrc  
    max-line-lenght=120  
    min-public-methods=1  
    min-similarity-lines=10  

    Incluir logo no inicio depois do [MASTER]  
      disable=  
           C0114 # missing-module-docstring
    
    
black (formatador de codigo de acordo com a formatacao PEP 8)
  - black asgi.py


flake8 (realiza a mesma verificacao que o pylint so que durante o processo de commit do codigo
  - .flake8  
    [flake8]  
    ignore = E722, W503 # W503 so para ficar alinhado com o black que permite  
    max-line-lenght = 120  
    per-file-ignores =  
            __init__.py: F401


pre-commit (permite realizar verificacoes e rodar comandos antes do commit)
  - pre-commit install
  - .pre-commit-config.yaml  
    <https://github.com/programadorLhama/python_settings/blob/master/.pre-commit-config.yaml>

mypy (verifica typing)
  - mypy --disallow-untyped-defs .