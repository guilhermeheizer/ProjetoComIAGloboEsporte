# gerador_html.py

def gerar_tabela_html(tabela_brasileirao, time_escudo):
    """
    Gera um HTML formatado que exibe os jogos da tabela do Brasileirão,
    incluindo escudos dos times.
    
    Args:
        tabela_brasileirao (dict): Estrutura de dados do Brasileirão.
        time_escudo (dict): Links de escudo dos times.

    Returns:
        str: HTML gerado.
    """
    html_tabela = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tabela do Brasileirão</title>
        <style>
            body {
                font-family: Arial, sans-serif;
            }
            .container {
                width: 80%;
                margin: 0 auto;
                text-align: center;
            }
            .rodada {
                margin-top: 20px;
                margin-bottom: 20px;
            }
            .jogo {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin: 10px 0;
                border-bottom: 1px solid #ccc;
                padding-bottom: 10px;
            }
            .escudo {
                width: 30px;
                height: 30px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Tabela do Brasileirão</h1>
    """

    for rodada, jogos in tabela_brasileirao.items():
        html_tabela += f'<div class="rodada"><h2>{rodada}ª Rodada</h2>'
        
        for jogo in jogos:
            mandante_escudo = time_escudo.get(jogo["time_mandante_sigla"], "")
            visitante_escudo = time_escudo.get(jogo["time_visitante_sigla"], "")

            html_tabela += f"""
            <div class="jogo">
                <div>
                    <img src="{mandante_escudo}" class="escudo" alt="{jogo['time_mandante_sigla']}">
                    <span>{jogo['time_mandante_nome']}</span>
                </div>
                <div>
                    <strong>{jogo['placar_time_mandante']} x {jogo['placar_time_visitante']}</strong>
                </div>
                <div>
                    <img src="{visitante_escudo}" class="escudo" alt="{jogo['time_visitante_sigla']}">
                    <span>{jogo['time_visitante_nome']}</span>
                </div>
            </div>
            """

        html_tabela += "</div>"

    html_tabela += """
        </div>
    </body>
    </html>
    """
    return html_tabela