Comandos base:

ruff check . && ruff format .                      #Para checar e formatar

fastapi dev fast_zero/app.py                       #Para rodar a aplicação

pytest --cov=fast_zero -vv                         #Teste

coverage html                                      #Cobertura (teste)

lint = 'ruff check . && ruff check . --diff'       #Mostra erro e onde alterar no código

format = 'ruff check . --fix && ruff format .'     #Corrige o código

Com Taskpy(Aliás)

task --list  #Mostra todos os comandos configurados

task run     #Para rodar o servidor

task test    #Para executar os testes

task lint

task format