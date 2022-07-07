from No import *

def sort(vetor):
    #temp=Nos(None,None,None)
    for i in range(0,len(vetor)):
      menor_indice=i
      for k in range(i+1,len(vetor)):
        if(vetor[k].valor<vetor[menor_indice].valor):
            temp=vetor[i]
            vetor[i]=vetor[k]
            vetor[k]=temp
