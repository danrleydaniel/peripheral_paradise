#Plano de Testes de Software

## Introdução
Serve para destacar como pretendemos realizar os testes de software do projeto Peripheral Paradise.

## Tipos de Testes
A princípio, os seguintes testes serão realizados:

1. Testes de Unidade
2. TDD

## Critérios de Aceitação
Os critérios de aceitação para cada tipo de teste são os seguintes:

- Testes de Unidade: Alcançar 80% de cobertura no SonarQube.
- Testes de Integração: Manter os 80% de cobertura no SonarQube.

## Plano de Testes
### Testes de Unidade
#### Caso de Teste 1
- Descrição: Testes feitos para testar unitariamente funções do Peripheral Paradise.
- Passos de Execução: Serão criados CRUDs e, em seguida, desenvolver testes de unidade para cada operação dos CRUDs. 
- Resultado Esperado: Manter os 80% de cobertura no SonarQube.

### TDD
#### Caso de Teste 2
- Descrição: Funções feitas utilizando Desenvolvimento Orientado a Testes.
- Passos de Execução: Primeiro, os testes serão escritos e rodados para, então, ser desenvolvido o código de produção. O teste será rodado novamente para checar se está funcionando corretamente com o código escrito. Caso não esteja, o código será reescrito. Esse processo será feito para cada ação do CRUD.
- Resultado Esperado: Manter os 80% de cobertura no SonarQube.
