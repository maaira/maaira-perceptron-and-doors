import random
import matplotlib.pyplot as plt
import numpy as np 

x1 = [0,1,0,1] 
x2 = [0,0,1,1]
y  = [0,0,0,1]
#w  = [random.randint(-1, 1),random.randint(-1, 1),random.randint(-1, 1)]
w = [0.5, 0.6, -0.3]
adjust = 0.1

def Correct(yn : list):
    if yn[0] == y[0] and yn [1] == y[1] and yn [2] == y[2] and yn [3] == y[3]:
        return True
    else : return False
    
def AcertSet(x1,x2, result,index):
    if y[index] == 1 and result == 0:
        if x1 > x2 :
            w[0] = w[0] + adjust
            w[2] = w[2] + adjust
        else : 
            w[1] = w[1] + adjust
            w[2] = w[2] + adjust
    else: 
        if x1 > x2 :
            w[0] = w[0] - adjust
            w[2] = w[2] - adjust
        else : 
            w[1] = w[1] - adjust
            w[2] = w[2] - adjust
        

listofresults = []

for x in range(50):

    print('-----Epoca ' + str(x) + '-----')
    listofresults.clear()

    for i in range(4):
        print ('__________________________________________')
        print ('Set ' + str((i+1)))
        print ('__________________________________________')

        print('Pesos: w1: '+ str(w[0]) + 'w2: '+ str(w[1]) + 'w3: '+ str(w[2]))
        print('X1',x1[0],x1[1],x1[2], x1[3])
        print('X2',x2[0],x2[1],x2[2], x2[3])
        

        result = x1[i]*w[0] + x2[i]*w[1] + w[2]
        if result > 0:
            yresult = 1            
        else :
            yresult = 0
            

        listofresults.append(yresult)
        if result != y[i]:
            AcertSet(x1[i],x2[i], yresult,i)
        
        print('Result :' + str(result) + '   Y: '+ str(yresult))
        print('Pesos: w1: '+ str(w[0]) + 'w2: '+ str(w[1]) + 'w3: '+ str(w[2]))
    if Correct(listofresults):
        print('-----Correct Epoca-----')
        break
    else :
        print('-----Incorrect Epoca-----')


#PLOTAR GRAFICO

for t in range(4):
    plt.scatter(x1[t], x2[t])

xp1 = ((-1) * w[2]) / w[0]
xp2 = ((-1) * w[2]) / w[1]
print(str(xp1) + "," + str(xp2))

pontos = [[0, xp1], [xp2, 0]]

z = np.polyfit(pontos[0], pontos[1], 1)
p = np.poly1d(z)
print("equação: ", p)

print('Pesos: w1: '+ str(w[0]) + 'w2: '+ str(w[1]) + 'w3: '+ str(w[2]))
# Generates plot
plt.plot(pontos, p(pontos), '-')

# plt.axis([0, 2, 0, 2])
plt.show()
print("Finalizado")





