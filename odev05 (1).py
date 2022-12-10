import math
sepallength = [5.3, 5.1, 7.2, 5.4, 5.1, 5.4, 7.4, 6.1, 7.3, 6.0, 5.8, 6.3, 5.1, 6.3, 5.5]
sepalwidth= [3.8, 3.7, 3.0, 3.4, 3.3, 3.9, 2.8, 2.8, 2.9, 2.7, 2.8, 2.3, 2.5, 2.5, 2.4]
species = ["Setosa","Setosa","Virginica","Setosa","Setosa","Setosa","Virginica","Verscicolor","Virginica","Verscicolor","Virginica","Verscicolor","Verscicolor","Verscicolor","Verscicolor"]
lengh = float(input("sepal length değeri :"))
width= float(input("sepal width değeri:"))
k_değeri = int(input(" K değeri değeri:"))
sözlük={}
for i in range(len(sepallength)):
    lenghfark=sepallength[i]-lengh
for i in range(len(sepalwidth)):
    widthfark=sepalwidth[i]-width
    oklid=math.sqrt(math.pow(lenghfark,2)+math.pow(widthfark,2))
    sözlük.update({i:oklid})
print(sözlük)
dis = {k: v for k, v in sorted(sözlük.items(), key=lambda item: item[1])}
print(dis)
for i in dis:
    print(sepallength[i],"  ",sepalwidth[i],"  ",i,"  ",species[i],"  ",dis[i])
dis_list = list(dis)
klistesi = []
for i in range(k_değeri):
    klistesi.append(species[dis_list[i]])

print(klistesi)
setosa=0
virginica=0
verscicolor=0
virginica=klistesi.count("Virginica")
verscicolor=klistesi.count("Verscicolor")
setosa=klistesi.count("Setosa")
switch = {
        case ( versicolor > setosa and versicolor > virginica):
        print("Sınıflandırma sonucu= Versicolor"),
        case (setosa > versicolor and setosa > virginica):
        print("Sınıflandırma sonucu= Setosa"),
        case:
        print("Sınıflandırma sonucu= Virginica")
 }
