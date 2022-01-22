# Programa que simula o sorteio dos números de um bingo
from random import sample

print("================= \033[1mlET'S GO BINGO!\033[m =================")
print('Aperte \033[1menter\033[m para sortear uma pedra e \033[1m[S]\033[m para sair')
print('===================================================')
pedras = range(1,76)
globo = sample(pedras, len(pedras)) #embaralhar a range (pedras totais)
sorteadas = []
print("")
for pedra in globo:
    op = input('Sortear uma pedra?').upper().strip()
    if op == 'S':
        break
    print(f'Pedra: {pedra}')
    sorteadas += [pedra]
    print(f'Sorteadas até o momento: {sorted(sorteadas)}')
    print("")
print('\033[31m===== B-I-N-G-O!!!! =====\033[m')
