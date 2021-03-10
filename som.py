import time
import winsound

def som(x, y):
    z = 0

    winsound.PlaySound('som.wav', winsound.SND_FILENAME)

    time.sleep(x)

    while z < y:
        z += 1
        winsound.PlaySound('som.wav', winsound.SND_FILENAME)
    
def main():
    x = int(input("Digite o intervalo de tempo entre o primeiro audio e os proximos: "))
    y = int(input("Informe o numero de vez que voce deseja que o audio se repita: "))
    
    som(x, y)
    
main()
    


