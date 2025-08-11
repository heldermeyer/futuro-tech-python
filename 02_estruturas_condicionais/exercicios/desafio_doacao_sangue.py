"""
3. Triagem para Doação de Sangue

Uma pessoa só pode doar sangue se:

Tem entre 16 e 69 anos (inclusive),

Pesa mais de 50 kg,

E não estiver em jejum.

Receba a idade, o peso e se a pessoa está em jejum (S ou N), e informe se ela pode doar sangue ou não.
"""

idade = int(input("Informe a sua idade: ")) # Entre 16 e 69
peso = float(input("Informe o seu peso: ")) # Peso > 50 kg
while True:
    jejum = str(input("Informe se está em jejum (S ou N): ")).lower() # Não pode estar em jejum
    if jejum not in ["s","n"]:
        print("Apenas S (Sim) ou N (Não)!")
        continue
    break

idade_permitida = idade >= 16 and idade <= 69
peso_adequado = peso > 50
jejum = True if jejum == "s" else False

if idade_permitida and peso_adequado and not jejum:
    print("Você pode doar sangue!")
else:
    print("Você não pode doar sangue!")
