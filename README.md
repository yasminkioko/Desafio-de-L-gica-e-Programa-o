# Desafio-de-Logica-e-Programacao
Escreva um programa onde, dado um determinado horário, ele seja capaz de calcular o ângulo entre os 2 ponteiros do relógio. 

Premissas:
1. Considere:
• 00:00h possui um ângulo de 0º.
• 00:15h possui um ângulo de 90º.
• 00:30 h possui um ângulo de 180º
2. Assinatura do método:
int retornaAnguloRelogio (int hora, int minuto);
3. O desafio deve ser resolvido escrito em Java ou linguagem natural.
4. Caso tenhas alguma dúvida, tome a decisão que julgar ser a melhor.
Resposta:
Public int retornaAnguloRelogio (int hora, int minuto) { // Implementar o restante do método
abaixo

"""
P Horas:
30 graus - 1 hora
x graus - h horas

x = 30h

P Minutos:
30 graus - 5 min
y graus - m min

y = 6m 

Como o ponteiro das horas anda z graus junto com o dos minutos:

30 graus - 60 min
z graus - m min

z = m/2

angulo = |y-(x+z)|
angulo = |(11m-60h)/2|
"""
