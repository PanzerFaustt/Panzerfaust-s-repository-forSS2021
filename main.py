"""import cv2 as cv
img = cv.imread('/home/duck1/Рабочий стол/1')
hsv = cv.cvtColor(img,cv.COLOR_BGR2XYZ
                  )
res_img = cv.resize(img,(500,806), cv.INTER_NEAREST)
cv.imshow('RGB IMAGE',img)
cv.waitKey(0)
cv.imshow('HSV image', hsv)
cv.waitKey(0)
cv.destroyAllWindows()
"""
"""
import a as a
"""
"""import cv2 as cv
img = cv.imread("/home/duck1/Рабочий стол/1")
img = cv.resize(img, (810, 806), cv.INTER_NEAREST)
cv.imshow("RGB Image", img)
cv.waitKey(0)
"""
"""import cv2 as cv
img = cv.imread('/home/duck1/Рабочий стол/1.png')

center = (int(w/2), int(h/2))
rotation_matrix = cv.getRotationMatrix2D(center, -45, 0.6)
rotated = cv2.warpAffine(image, rotation_matrix, (w, h))
cv2_imshow(rotated)
"""
"""
#1
int(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8, i=9, k=10)
int(x=a ** 3, y= b ** 3, z=c ** 3, r=d ** 3, t =e ** 3, u=f ** 3, o=g ** 3, p=h ** 3, w=i ** 3, q=k ** 3)
list = {a:x, b:y, c:z , d:r , e:t, f:u, g:o , h:p, i:w , k:q }
print(list)
"""
"""
l=[i for i in range(10)]
d = {}
for i in l:
    i+=1
    d[i]=i**3
print(d)
"""
"""
int x = 0

l = {x:68,town:5,duckietown:594, dickiedown:2314 }
"""
"""
test = [48,67,9,4,3,56]
print("Список : " + str(test))
res = test[::len(test)-1]
print("Первый и последний элементы списка : " + str(res))
"""


"""
import cv2 as cv
img = cv.imread('/home/duck1/Рабочий стол/1')
#cv.imshow('tractor',img)
cv.imwrite('/home/duck1/opencvTest/tractor2.jpg',img)
cv.waitKey(0)
cv.destroyAllWindows()
print("Высота"+" "+str(img.shape[0]))
print("Ширина"+" "+str(img.shape[1]))
Pixel =img[1,1]
print(Pixel)
dimension = img.shape
print(dimension)
"""
""""js=input()
if len(s)<1 and len(s)>6 and not(s.isdigit()) :
    print("error")
elif int(s[0])+int(s[1])+int(s[2])==int(s[3])+int(s[4])+int(s[5]):
    print("Счастливый билет")
else: print("это обычный билет")

"""
"""
while True:
    x=int(input())
    if x>100:
        break
    elif x<10:
        continue
    else: print(x)
"""
"""
str='0,1,y,y,4,5,r,7,8,o,t'
x=0
for i in range(len(str)):
   if str[i].isdigit()==True:
      x+=1
      print(x)
   else:
      continue
"""
"""
person = {"name": "Kelly", 'age':25, "City":"New york"}
x=person.get("age")
print(x)
"""
"""
models_data = {"Vaz": "2106", 'tesla':"Model S" "Tesla plaid" "model x", "Bmw":"X3" "M5" "M2"}
print(models_data['tesla'][)
"""
"""
num=int(input())
sum=0
while(num!=0):
    sum=sum+num%10
    num=num//10
print(sum)
"""

"""
str1=str(input())
print(str1)
k=0
for elem in str1:
    if elem.isdigit():
        k+= int(elem)
        print(elem)
print("k=",k)
"""
"""
N2
m=[11,5,8,32,15,3,20,132,21,4,555,9,20]
for i in range(len(m)):
   if m[i]<30 and m[i]% 2==0:
       print(m[i])
       continue
"""
"""
dic = input().split()
dic2 = input().split()
dic3{}
i =0
for i in range(len(dic))
    dic3[dic[i]]=dic2[i]

print((dic3))
"""
"""
a=input().split()
b=input().split()
dic{a[i]:b[i], for i in range()}
"""
"""
s=str(input())
s1=s[::-1]
for elem in s1:
    if elem.islower():
        print(elem)
print(s1)

"""