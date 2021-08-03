import random
import plotly.express as px
import plotly.figure_factory as ff
result=[]
count=[]
for i in range(0,100):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    result.append(dice1+dice2)
    count.append(i)
print(result)   
graph=ff.create_distplot([result],["result"],show_hist=False)
graph.show() 

