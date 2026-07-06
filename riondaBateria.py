# REQUISITOS DO PROGRAMA - Definição das 2 variáveis
# (Você pode alterar os valores abaixo para testar as diferentes condições)
bateria_atual = 10
bola_em_jogo = True

# Processamento das condições (If / Elif / Else) de forma ordenada
if bateria_atual < 15 and bola_em_jogo == True:
    # Condição 1: Bateria abaixo de 15% E bola em jogo
    print("ALERTA MÁXIMO: Bateria baixa! Substitua a bola na próxima paralisação.")

elif bateria_atual < 15 and bola_em_jogo == False:
    # Condição 2: Bateria abaixo de 15%, mas bola NÃO está em jogo
    print("Aviso: Bateria baixa. Aproveite a bola parada para trocá-la.")

else:
    # Condição 3 (Caso Geral): Bateria igual ou acima de 15%
    print("Sistema Trionda operando normalmente. Bateria ok.")
