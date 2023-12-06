# Parte 1
# Lista para armazenar as listas de dígitos de cada linha
digits = []

with open('day_1_input.txt') as file:
    # Lê o arquivo e separa as linhas em uma lista
    data = file.read().splitlines()
    # Itera por cada linha do arquivo
    for i in data:
        # Lista para armazenar os dígitos da linha atual
        digit_line = []
        # Itera por cada string da linha
        for j in i:
            # Verifica se é um digito ou uma letra
            if j.isdigit():
                # Se for um dígito adiciona na lista de digitos já convertido para inteiro
                digit_line.append(int(j))
        # Vê se lista tem pelo menos 2 digitos
        if len(digit_line) >= 1:
            # Pego o primeiro e o último digito dessa lista
            combined_number = int(str(digit_line[0]) + str(digit_line[-1]))
            # Adiciona os valores combinados na lista de digitos
            digits.append(combined_number)

print(digits)
print(sum(digits))
