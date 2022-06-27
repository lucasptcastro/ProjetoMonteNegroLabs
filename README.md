# Montenegro Labs - Teste Python 

Este projeto foi desenvolvido com o intúito de consumir dados do site <a href="https://www.contabeis.com.br/conteudo/">contabeis</a> à fim de ser avaliado e selecionado para a vaga de Desenvolvedor Python Júnior.

Foi idealizado dois projetos: um criado por mim, utilizando algumas bibliotecas nativas e externas do python e outro usando o framework scrapy que é ideal para este tipo de uso. 

## USAR O PROJETO EM SI:
 - 1° alternativa: executar o arquivo "program.exe" localizado em ProjetoMonteNegroLabs/dist/program.exe
 
<div align="center">
 <img align="center" src='https://github.com/lucasptcastro/ProjetoMonteNegroLabs/blob/main/images/local%20do%20program.exe.png'>
</div>
 
 <br>
 
 - 2° alternativa: abrir o arquivo "program.py" em um editor de código/IDE e executar o projeto.
 
<div align="center">
 <img align="center" src='https://github.com/lucasptcastro/ProjetoMonteNegroLabs/blob/main/images/executar%20programa.py.png'>
</div>

<br>

 - Ambas as situações irá retornar o arquivo "data.json" na pasta raíz do projeto.
 
<div align="center">
 <img align="center" src='https://github.com/lucasptcastro/ProjetoMonteNegroLabs/blob/main/images/local%20do%20data.json.png'>
</div>
 

## USAR FRAMEWORK SCRAPY:
 - 1° passo: acessar algum terminal (recomendo o anaconda prompt) e, em sequência, executar os seguintes comandos dentro da pasta raíz do programa:
 
<div align="center">
 <img align="center" src='https://github.com/lucasptcastro/ProjetoMonteNegroLabs/blob/main/images/comandos%20framework%20scrapy.png'>
</div>

 - O primeiro comando é para ir até a pasta em que o scrapy foi instalado.
 - O segundo é para transformar o scrapy em um arquivo .json.

## NECESSÁRIO
 - Python 3.10.5 ou superior instalado


## RECOMENDAÇÕES SEGUIDAS

- [x] Use Python >= 3.7
- [x] Use o Playwright
- [x] Use a PEP-8 como referência
- [x] Use Git
- [x] Escreva mensagens claras no Git
- [x] Escreva testes unitários!
- [x] Modele os dados com cautela e procure representar as entidades corretamente
- [x] Siga a documentação do Python e Playwright
- [x] Documente sua aplicação:
  - Descreva sua aplicação e os problemas que ela resolve
  - Dê instruções de como executar os testes e a sua aplicação

## Observações:

 - A formatação do arquivo data.json não ficou idêntica ao que foi proposto, tendo em vista que os dados ficaram dispostos um abaixo do outro e não todos em uma linha só.
 - Notei que a página que foi usada carrega mais assuntos ao chegar ao final dela, porém foi levado em consideração apenas a página principal que é carregada, tentei carregar as demais utilizando a busca pela tag 'p' que tinha o seguinte texto: "O Portal Contábeis se isenta de quaisquer responsabilidades civis sobre eventuais discussões dos usuários ou visitantes deste site, nos termos da lei no 5.250/67 e artigos 927 e 931 ambos do novo código civil brasileiro." da classe "rodapeFinal", que carregava os demais assuntos até o ano de 2007, porém não obtive êxito.
 - No mais, o programa cumpre totalmente o que foi proposto e está documentado utilizando as a padronização PEP 257, proposto no guia PEP 8.

