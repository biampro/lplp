import math
import matplotlib.pyplot as plot
points=[(0.15,0.71),(0.08,0.9),(0.16,0.85),(0.2,0.3),(0.25,0.5),(0.24,0.1)]
m1=[0.1,0.6]
m2=[0.3,0.2]
c1=[(0.1,0.6)]
c2=[(0.3,0.2)]
for i in points:
    dist1=math.sqrt((i[0]-m1[0])**2 + (i[1]-m1[1])**2)
    dist2=math.sqrt((i[0]-m2[0])**2 + (i[1]-m2[1])**2)
    if(dist1<=dist2):
        c1.append(i)
        m1[0]=(m1[0]+i[0])/2
        m1[1]=(m1[1]+i[1])/2
       
    else:
        c2.append(i)
        m2[0]=(m2[0]+i[0])/2
        m2[1]=(m2[1]+i[1])/2
        
c11=[]
c21=[]
it=0
while(c11!=c1 and c21!=c2):
  it+=1
  for i in c1:
    dist1=math.sqrt((i[0]-m1[0])**2 + (i[1]-m1[1])**2)
    dist2=math.sqrt((i[0]-m2[0])**2 + (i[1]-m2[1])**2)
    if(dist1<=dist2):
        c11.append(i)
        m1[0]=(m1[0]+i[0])/2
        m1[1]=(m1[1]+i[1])/2
        
    else:
        c21.append(i)
        m2[0]=(m2[0]+i[0])/2
        m2[1]=(m2[1]+i[1])/2
  for i in c2:
    dist1=math.sqrt((i[0]-m1[0])**2 + (i[1]-m1[1])**2)
    dist2=math.sqrt((i[0]-m2[0])**2 + (i[1]-m2[1])**2)
    if(dist1<=dist2):
        c11.append(i)
        m1[0]=(m1[0]+i[0])/2
        m1[1]=(m1[1]+i[1])/2
       
    else:
        c21.append(i)
        m2[0]=(m2[0]+i[0])/2
        m2[1]=(m2[1]+i[1])/2
if points[4] in c1:
    print("Point 6 in Cluster 1!!!")
else:
    print("Point 6 in Cluster 2!!!")
print("final cluster 1 average",str(m1))
print("Final Cluster 2 average",str(m2))
print("Population around cluster 2",str(len(c21)))
x1=[]
x2=[]
y1=[]
y2=[]
for i in c11:
    x1.append(i[0])
    y1.append(i[1])
for i in c21:
    x2.append(i[0])
    y2.append(i[1])

x3=[m1[0],m2[0]]
y3=[m1[1],m2[1]]
plot.scatter(x3,y3, color='blue')    
plot.scatter(x1,y1, color='red')
plot.scatter(x2,y2, color='green')
plot.show()
