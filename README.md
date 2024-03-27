# Automatização de Cadastro de Produtos em Site
Este projeto consiste em uma automação para realizar o cadastro de produtos em um site específico. O objetivo é facilitar o processo de cadastro, eliminando a necessidade de inserção manual dos dados.

## Visão Geral do Projeto
O processo de cadastro de produtos é automatizado por meio de scripts Python utilizando a biblioteca PyAutoGUI para simular as ações do usuário. O fluxo de trabalho inclui os seguintes passos:

Acesso ao site no navegador Chrome. <br>
Realização do login no site. <br>
Importação da base de dados de produtos. <br>
Cadastro dos produtos em looping até que todos sejam cadastrados. <br>


## Funcionalidades Principais
- Automatização de Tarefas: O projeto automatiza tarefas repetitivas de cadastro de produtos, economizando tempo e esforço manual.
- Interatividade com o Navegador: Utiliza a biblioteca PyAutoGUI para interagir com elementos da interface do navegador, como campos de texto e botões.
- Importação de Dados: Os dados dos produtos são importados a partir de um arquivo CSV utilizando a biblioteca Pandas.
- Looping de Cadastro: Realiza o cadastro dos produtos em looping até que todos os itens da base de dados sejam cadastrados com sucesso.


## Como Utilizar
- Clone este repositório em sua máquina local.
- Certifique-se de ter Python instalado em seu ambiente.
- Instale as bibliotecas necessárias executando pip install pyautogui pandas.
- Certifique-se de ter o navegador Chrome instalado em sua máquina.
- Execute o script Python para iniciar o processo de automação de cadastro de produtos.
- Aguarde o término da execução do script e verifique se todos os produtos foram cadastrados corretamente no site.

# Aviso
Este projeto foi desenvolvido para fins de estudo e demonstração. Certifique-se de ter permissão para automatizar tarefas em sites específicos antes de usar este script em produção.
O funcionamento deste script pode depender de fatores como a resolução da tela e a posição dos elementos na interface do site. Ajustes podem ser necessários dependendo do ambiente de execução.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar um pull request com melhorias ou correções.
