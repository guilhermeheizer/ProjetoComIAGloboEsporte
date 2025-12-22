# Projeto com IA Globo Esporte
Extração das rodadas e dos jogos da Tabela Brasileirão Série A ou B com ChatGPT

Para enriquecer o estudo em Python, resolvi criar um programa Python para extrair do site do Globo Esporte a tabela de jogos do Brasileirão da Série A de 2026 e do Brasileirão da Série B de 2025.

Preparei a análise de um programa para extrair dos dados, como explicações detalhadas. Veja o **"instrucao_extracao_selenium.txt"** anexo no repositório do GitHub.
Esta análise foi a base do **prompt para o ChatGPT gerar o programa Python**, 

A análise do programa de extração abordou:
- A dinâmica do funcionamento site
- Quais as tags terão os contéudos capturados (
- Parametros de entrada
- Qual site do Globo Esporte (url)
- Como é a lógica para obter os conteúdos de cada tag do site
- Como navegar de uma rodada para outra, realizando o clique automático na seta de navegação
- Se vou percorrer as rodadas na ordem crescente ou decrecente a partir da rodada default que é carregada automaticamente
- A saída, defini dois dicionários: um JSON das rodadas com os jogos e outro JSON com o endereço para download dos escudos dos times

Solicitei ao ChatGPT a geração de outro programa:
- Uma página html para listar as rodadas e os jogos. Semelhante ao site do Globo Esporte, e que utilizasse o print screen do site: "ExemploTabela.png",
  os dois diconários da rodadas e dos escudos foram a base da listagem.

A análise do programa foi submetida ao ChatGPT, solicitando a criação do programa Python utilizando a biblioteca Selenium. 
Tal biblioteca é utilizada para acessar sites para extração de dados. A lógica do programa foi gerada conforme a minha análise.

Utilizei o VSCode para o projeto "ProjetoComIAGloboEsporte", com ambiente vitual para executar o programa Python gerado pelo ChatGPT.
Obs: acesse "instrucao_criacao_ambiente_virtual.txt" 

Na primeira execução, o programa cancelou por não encontrar a tag, a minha análise estava com explicação errada. 
Fiz a correção do programa, a leitura de duas das tags estava errada. O ChatGPT considerou a minha análise. 

Após a correção do erro de cancelamento, realizei uma série de testes e pequenos ajuste no programa. 
Primeiro, testei com a tabela da Série A de 2026 e algumas informações ainda não existem, como o local do jogo, o horário e o placar. 
Depois, realizei um segundo teste com a tabela da Série B de 2025, que contém as 38 rodadas com seus placares, horários e locais dos jogos. 

Conclusão:

Achei que o resultado do **Programador ChatGPT** com o Copilot foi supreende, gerou o programa main.py bem feito e com as funções separadas.

O mais importante de tudo foi a realização de testes com as tabelas do Brasileirão da Série A e Série B e conferência dos resultados.


