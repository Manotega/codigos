def incomodam(n):
    if type(n) != int or n <= 0:
        return "" 
   
    return "incomodam " +  incomodam(n-1)


def elefantes(n):
    if n < 1:
        return ""
    
    elif n == 1:
        return "Um elefante incomoda muita gente"
        elefantes(n-1)
        
    elif n == 2:
        return elefantes(n-1) + "\n2 elefantes incomodam incomodam muito mais"
            
    else:
        return elefantes(n-1) + f"\n{n-1} elefantes incomodam muita gente\n{n} elefantes {incomodam(n)}muito mais" 
               


        

