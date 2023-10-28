hora = 0
minuto = 0

def usuario():
    while True:
            try :
                    global hora
                    global minuto
                
                    print("Qual é o ângulo entre dois ponteiros de um relógio? \n")                                          
                    hora = int(input("Insira o ponteiro da hora (0 à 12): \n"))
                    minuto = int(input("Insira o ponteiro do minuto (0 à 60): \n"))
                                    
                    if hora <= 12 and minuto <=60:                        
                        print("\nHora escolhida:",hora,":",minuto)
                    else:
                        print("Valores fora do esperado, tente novamente \n")
                        continue
            
            except ValueError:
                    print("Valores fora do esperado, tente novamente \n")
  
            else:
                break

def angulo(hora, minuto):
    
    angulo = abs((11*minuto - 60*hora)/2)
    
    if angulo > 180:
        ang_menor = 360 - angulo
        print("Ângulo:", ang_menor, "°")
        
    else:
        print ("Ângulo:", angulo, "°")
    
        
if __name__ == "__main__":
    usuario()   
    angulo(hora, minuto)