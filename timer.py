#import módulo time
import time
#roberta
#Marcos >=)

seconds = int(input("Digite o tempo em segundos: "))

def countdown_timer(sec):
    while sec >=0:
        
        mins = sec // 60
        secs = sec % 60

        timer = f"{mins}:{secs}   "
        print(timer, end="\r")
        #diminuir os segundos somente apos 1 segundo
        time.sleep(1)
        sec -= 1
    print ("Tempo esgotado!!!")

countdown_timer(seconds)





































































































