import lorem as lr
import time

sentence = lr.sentence()

i=0
for i in range(500):       
    print(" " *i +  sentence)
    #print(" ")
    i=+1

    start_time = time.time()
    seconds = 0.3

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time > seconds:
            print("") #"""str(int(elapsed_time))  + " seconds""")
            break     
 

    
    
    
    

    
