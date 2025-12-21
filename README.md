# ProjetoComIAGloboEsporte
Extração das rodadas e dos jogos da Tabela Brasileirão Série A ou B com ChatGPT

Há algum tempo penso em montar uma tabela do Brasileirão, no estilo do Globo Esporte, e no decorrer das rodadas, à medida que os jogos vão acontecendo e os gols marcados, vou inputando os gols e a tabela de classificação atualiza.

Para enriquecer o estudo em Python, resolvi desenvolver um programa em Python para extrair do site do Globo Esporte a tabela de jogos do Brasileirão da Série A de 2026 e do Brasileirão da Série B de 2025.

Preparei literalmente a definição de um programa para extrair os dados, ou seja, uma das tarefas do analista de sistemas: após definidos os processos, define-se o que cada programa irá fazer.

A definição do programa de extração arbodou:
- Parametros de entrada
- Qual site do Globo Esporte (url)
- Como é a lógica para obter os conteúdos de cada tag do site
- Como navegar de uma rodada para outra, realizando o clique automático na seta de navegação
- Se vou percorrer as rodadas na ordem crescente ou decrecente a partir da rodada default que é carregada automaticamente
- E por fim, a saída, defini um JSON dos jogos e outro JSON com o endereço para download dos escudos dos times
A definição do programa foi submetida ao ChatGPT, solicitando a criação de um programa Python utilizando a biblioteca Selenium. Tal biblioteca é utilizada para acessar sites para extração de dados.

 Utilizei o VSCode para executar o programa Python gerado pelo ChatGPT. A lógica do programa foi gerada conforme a minha análise.

Na primeira execução,  o programa cancelou por não encontrar a tag. Fiz a correção do programa porque a leitura de duas das tags estava errada. O ChatGPT considerou a minha análise. 

Após a correção do erro de cancelamento, iniciei os testes, mais uma das tarefas do analista de sistemas que deve ser feita após a entrega do programa pelo programador ChatGPT. Fui realizando testes e acertos no programa. Primeiro, testei com a tabela da Série A de 2026, e algumas informações ainda não existem, como o local do jogo, o horário e o placar. Depois, realizei um segundo teste com a tabela da Série B de 2025, que contém as 38 rodadas com seus placares, horários e locais dos jogos. O resultado do teste foi 100% correto na primeira execução.
