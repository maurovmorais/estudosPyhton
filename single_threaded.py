import time
from threading import Thread

COUNT = 50_000_000

def countdown(n):
    while n > 0:
         n-= 1
         
t1 = Thread(target=countdown, args=(COUNT, ) )
t2 = Thread(target=countdown, args=(COUNT, ) )
         
start = time.time()

t1.start()
t2.start()

t1.join()
t2.join()

#countdown(COUNT)
end = time.time()

print("Tempo de execucao: ", end - start)         

