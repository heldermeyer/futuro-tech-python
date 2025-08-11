"""
5. Verificação de Elegibilidade para um Empréstimo
Um banco só concede empréstimo se o cliente:
Tem renda mensal acima de R$ 2.000,

E não está negativado ou possui um fiador com nome limpo.

Peça ao usuário:
A renda mensal,

Se está negativado (S ou N),

Se possui fiador com nome limpo (S ou N).

Use os operadores lógicos adequados para decidir se o empréstimo será "Aprovado" ou "Negado".
"""

renda = float(input("Informe a sua renda: "))

while True:
    esta_negativado = str(input("Você está negativado (S/N)? ")).lower()
    if esta_negativado not in ["s","n"]:
        print("Apenas S (Sim) ou N (Não)!")
        continue
    possui_fiador = str(input("Você possui fiador (S/N)? ")).lower()
    if possui_fiador not in ["s","n"]:
        print("Apenas S (Sim) ou N (Não)!")
        continue
    break

esta_negativado = True if esta_negativado == "s" else False
possui_fiador = True if possui_fiador == "s" else False

possui_renda_minima = renda >= 2000.00

if possui_renda_minima and (not esta_negativado or possui_fiador):
    print("Empréstimo liberado!")
else:
    print("Empréstimo negado!")
