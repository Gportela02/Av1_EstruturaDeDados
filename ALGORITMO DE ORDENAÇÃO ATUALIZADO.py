import random
aleatorio = random.sample(range(1,500),100)
contadorb = 0
trocasb = 0
contadors = 0
trocass = 0
contadorm = 0
trocasm = 0
#Código Bubble Sort
list1 = list.copy(aleatorio)
def shortBubbleSort(bubblelist):
    global contadorb
    global trocasb
    for i in range (len(bubblelist)):
        for j in range (len(bubblelist)-i-1):
            contadorb +=1
            if (bubblelist[j] > bubblelist[j+1]):
                bubblelist[j],bubblelist[j+1] = bubblelist[j+1], bubblelist[j]
                trocasb +=1
    return bubblelist

#Código Selection Sort
list2 = list.copy(aleatorio)

def insertion_sort(lista2):
    global contadors
    global trocass
    for i in range(1, len(lista2)):
        chave = lista2[i]
        j = i - 1
        while j >= 0 and lista2[j] > chave:
            contadors+=1
            lista2[j + 1] = lista2[j]
            j -= 1
        lista2[j + 1] = chave
        trocass+=1
    return lista2

#Código Merge Sort
list3 = list.copy(aleatorio)
def mergesort(lista3, inicio=0, fim=None):
    if fim is None:
        fim = len(lista3)
    if(fim-inicio > 1):
        meio = (fim + inicio)//2
        mergesort(lista3, inicio, meio)
        mergesort(lista3, meio, fim)
        merge(lista3, inicio, meio, fim)

def merge(lista3, inicio, meio, fim):
    global contadorm
    global trocasm
    left = lista3[inicio:meio]
    right = lista3 [meio:fim]
    i, j = 0, 0
    for k in range(inicio, fim):
        if i >= len(left):
            lista3[k] = right[j]
            j = j + 1
            trocasm += 1
            
        elif j >= len(right):
            lista3[k] = left[i]
            i = i + 1
            trocasm += 1
            
        elif left[i] < right[j]: 
            lista3[k] = left [i]
            i = i + 1
            trocasm += 1
            
        else:
            lista3[k] = right[j]
            j = j + 1
            trocasm += 1
        
        contadorm +=1        

contador = 0
while (contador < 3):
    a = input ("Você deseja ordenar por qual organizador? \n 1-Bubble Sort \n 2- Selection Sort \n 3- Merge Sort \n")
    resposta = bool (a)
    if resposta == int (1):
        list1=shortBubbleSort(list1)
        print ("LISTA NÃO ORGANIZADA: \n")
        print (list.copy(aleatorio))
        print ("\n LISTA ORGANIZADA:\n")
        print (list1)
        print ("\n A quantida de trocas utilizadas nesse algoritmo foi de ", trocasb)
        print ("\n A quantida de comparações utilizadas nesse algoritmo foi de ", contadorb)
        contador +=1
    if resposta == int (2):
        list2=insertion_sort(list2)
        print ("LISTA NÃO ORGANIZADA: \n")
        print (list.copy(aleatorio))
        print ("\n LISTA ORGANIZADA:\n")
        print (list2)
        print ("\n A quantida de trocas utilizadas nesse algoritmo foi de ", trocass)
        print ("\n A quantida de comparações utilizadas nesse algoritmo foi de ", contadors)
        contador +=1
    if resposta == int (3):
        list3 = merge
        print ("LISTA NÃO ORGANIZADA: \n")
        print (list.copy(aleatorio))
        print ("\n LISTA ORGANIZADA:\n")
        print (list3)
        print ("\n A quantida de trocas utilizadas nesse algoritmo foi de ", trocasm)
        print ("\n A quantida de comparações utilizadas nesse algoritmo foi de ", contadorm)
        contador +=1
    
    if contador == (1): 
        print ("\n Você tem mais 2 algoritmos de ordenação para testar!!\n")
    if contador == (2):
        print ("\n Você tem apenas 1 algoritmo restante para testar.\n")
    if contador == (3):
        print ("\n Parabéns você testou todos os algoritmos de ordenação!")
