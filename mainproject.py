from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import random
import sys

print("Covid data visualiser")
print("Note: This program uses data obtained in Decmeber 2021")

def casecountries():
    # covid cases by countries as of dec 2021 top
    # source worldometer dataset

    #declaring the style and a colour list for later use

    plt.style.use("seaborn")
    colours = ["#bc5090","#bc5090","#bc5090","#ff6361","#ff6361","#ff6361","#ff6361","#ffa600","#ffa600","#ffa600"]

    #reading specific coloumns from a csv file

    data = pd.read_csv("data6.csv")
    x = list(data["Country"])
    y = list(data["Total Cases"])

    #converting the lists to a dictionary and sorting them by value

    d = dict(zip(x,y))
    d = sorted(d.items(), key = lambda x:x[1], reverse=True)
    d = d[0:10]
    data_x = []
    data_y = []
    for t in d:
        data_x.append(t[0])
        data_y.append(t[1])

    #using numpy to create a list of indexes to be plotted

    indexes_x = np.arange(len(data_x))

    #plotting a bar graph

    plt.bar(indexes_x,data_y, width=0.5, color=random.choice(colours),label= "Covid cases")

    #specifying some properties of the graph

    plt.xticks(ticks=indexes_x, labels=data_x)
    plt.title("Countries with the highest covid cases as of December 2021")
    plt.xlabel("Countries")
    plt.ylabel("Number of cases in crores")


    #adding credit
    plt.text(7,47000000,"*Data obtained from kaggle dataset", fontdict={"family":"serif","size":8})

    #using tight layout when encountering formatiing issues
    #plt.tight_layout()
    plt.legend()
    plt.show()



def casecountries_year():
    #covid cases by countries seperated by year
    #data inputted from ourworldindata.com manually


    #declaring the style and a colour list for later use


    plt.style.use("seaborn")
    colours = ["#bc5090","#bc5090","#bc5090","#ff6361","#ff6361","#ff6361","#ff6361","#ffa600","#ffa600","#ffa600"]

    #manually declaring data from ourworldindata.org

    data_x = ["United states", "India", "Brazil", "UK", "Russia", "Turkey", "France","Germany", "Iran", "Spain"]
    data_2020 = [20160000,10290000,7680000,2490000,3130000,2210000,2660000,1750000,1230000,1930000]
    data_2021 = [32840000,24500000,14560000,9820000,7100000,7150000,6690000,5300000,4960000,4100000]

    #using numpy to create a list of indexes to be plotted


    index_x = np.arange(len(data_x))

    #specifying a width to plot multiple bars in the same x point
    width = 0.25

    #plotting the bar graphs
    #one of them is displaced by a specified width value

    plt.bar(index_x,data_2020,width=width,label="2020",color="#003f5c")
    plt.bar(index_x+width,data_2021,width=width,label="2021",color="#bc5090")

    #adding credit
    plt.text(7.8,30000000,"*Data obtained from ourworldindata.org", fontdict={"family":"serif","size":8})

    #specifying properties
    plt.xticks(ticks=index_x, labels=data_x)
    plt.ylabel("Number of cases in crores")
    plt.xlabel("Countries")
    plt.title("Number of covid cases by year")



    plt.legend()
    plt.show()



def casestates():

    #covid cases by state
    #data from kaggle dataset

    #declaring the style
    plt.style.use("seaborn")

    #reading specific coloumns from a csv file


    data = pd.read_csv("data4.csv")
    x = list(data["State/UTs"])
    y = list(data["Total Cases"])

    #converting the lists to a dictionary and sorting them by value

    d = dict(zip(x,y))
    d = sorted(d.items(),key = lambda x:x[1], reverse=True)
    d = d[0:10]

    l1 = []
    l2 = []

    for t in d:
        l1.append(t[0])
        l2.append(t[1])

    #using numpy to create a list of indexes to be plotted


    index_x = np.arange(len(l1))

    #plotting the graph

    plt.bar(index_x,l2,width=0.5, label = "Covid cases", color="#bb0055")


    #specifying some properties

    plt.xticks(ticks=index_x, labels=l1)
    plt.title("Covid cases by states")
    plt.ylabel("Covid cases in lakhs")
    plt.xlabel("States")

    #adding credit

    plt.text(7.3,6000000,"*Data obtained from kaggle dataset", fontdict={"family":"serif","size":8})

    plt.legend()
    plt.show()




def deathcountries():

    #covid deaths by countries
    #data from worldometer dataset

    #declaring the style

    plt.style.use("seaborn")

    #reading specific columns from a scv file
    x = []
    y = []
    data = pd.read_csv("data6.csv")
    x = list(data["Country"])
    y = list(data["Total Deaths"])


    #converting the lists to dictionary and sorting them by values

    d = dict(zip(x, y))
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    d = d[0:10]
    data_x = []
    data_y = []
    for t in d:
        data_x.append(t[0])
        data_y.append(t[1])


    #plotting the graph

    plt.bar(np.arange(len(data_x)), data_y, label="Deaths", color="#ffa600")

    #specifying some properties

    plt.xticks(ticks=np.arange(len(data_x)), labels=data_x)

    plt.ylabel("Deaths")
    plt.title("Covid deaths by countries")
    plt.xlabel("Countries")


    #adding credits
    plt.text(8, 800000, "*Data obtained from Worldometer.org", fontdict={"family": "serif", "size": 8})

    plt.legend()
    plt.show()


def piecasescountries():

    #pie chart on covid cases by countries
    #data inputted manually from worldometer.com


    #manually inputting data
    data_x = ["United states", "India", "Brazil", "UK", "Russia", "Turkey", "France","Germany", "Iran", "Spain"]
    data_y = [53222424,34793333,22239436,11891292,10415230,9307124,9116068,7009634,6184762,5718007]


    #converting raw numbers to percentages
    total_cases = 285000000
    percent = []
    for i in data_y:
        a = (i/total_cases)*100
        percent.append(a)


    #declaring a colour set
    colours =["#003F5C","#58508D","#BC5090","#FF6361","#FFA600","#6050DC","#D52DB7","#FF2E7E","#FF6B45","#FFAB05"]
    random.shuffle(colours)

    #declaring a explode list to highlight a specific part of the graph
    explode = [0,0.09,0,0,0,0,0,0,0,0]

    #plotting the pie chart
    plt.pie(percent,labels=data_x,wedgeprops={"edgecolor": "black"}, autopct="%1.2f%%",explode = explode,shadow=True,colors=colours)
    plt.title("Covid cases by countries")


    #plt.legend()
    plt.show()



def deathstates():

    #covid deaths by states
    #data from kaggle dataset



    #declaring the style

    plt.style.use("seaborn")


    #reading specific columns from a csv file
    data = pd.read_csv("data4.csv")
    x = data["State/UTs"]
    y = data["Deaths"]
    states = list(x)
    deaths = list(y)

    #converting the lists to a dictionary and sorting them

    d = {}

    for i,j in zip(states,deaths):
        d[i] = j

    f = sorted(d.items(),key=lambda x:x[1],reverse=True)
    mydata = f[0:10]
    data_x = []
    data_y=[]

    for t in mydata:
        data_x.append(t[0])
        data_y.append(t[1])


    #declaring a index list to be plotted
    index_x = np.arange(len(data_x))

    #plotting the graph
    plt.bar(index_x,data_y, label="Deaths", color = "#58508D")


    #specifying some properties

    plt.xticks(ticks=index_x,labels=data_x)
    plt.title("Covid death by states")
    plt.ylabel("Deaths")
    plt.xlabel("States/UTs")

    plt.legend()
    plt.show()




def piecasesstates():
    #pie chart on covid cases by states
    #data from kaggle dataset


    #declaring the style
    #plt.style.use("seaborn")

    #reading specific columns from a csv file

    data = pd.read_csv("data4.csv")
    x = data["State/UTs"]
    y = data["Total Cases"]

    #converting the dictionary

    d = dict(zip(x,y))
    d = sorted(d.items(),key = lambda x:x[1], reverse=True)
    d = d[0:10]

    states=[]
    cases=[]
    for t in d:
        states.append(t[0])
        cases.append(t[1])


    #converting raw data to percentages
    total_cases = 34800000

    percent = []
    for i in cases:
        a = (i/total_cases)*100
        percent.append(a)


    #declaring a colour list

    colours =["#003F5C","#58508D","#BC5090","#FF6361","#FFA600","#6050DC","#D52DB7","#FF2E7E","#FF6B45","#FFAB05"]
    random.shuffle(colours)


    #plotting a pie chart
    plt.pie(percent, wedgeprops={"edgecolor":"black"}, autopct="%1.2f%%",colors=colours,shadow=True,labels=states)

    plt.title("Covid cases by states")

    plt.show()



def deathratebystates():

    #barh death rate by state
    #data from kaggle dataset



    #declaring the style
    plt.style.use("seaborn")

    #reading specific columns from a csv file

    data = pd.read_csv("data4.csv")
    x = list(data["State/UTs"])
    y = list(data["Death Ratio"])


    #converting the lists into dictionary and sorting them by value
    dic = dict(zip(x,y))

    dic = sorted(dic.items(), key = lambda x:x[1], reverse=True)
    dic = dic[0:10]
    dic.reverse()

    states = []
    deathratio = []

    for t in dic:
        states.append(t[0])
        deathratio.append(t[1])


    #declaring an index list to plot

    indexes = np.arange(len(states))


    #plotting a horizontal bar graph
    plt.barh(indexes,deathratio,color= "#6050DC",label = "Death rate")

    #specifying some properties
    plt.yticks(ticks=indexes,labels=states)
    plt.xlabel("Death rate")
    plt.title("Death rate by states")

    plt.text(2.2, 8, "*Data obtained from Worldometer.org", fontdict={"family": "serif", "size": 8})


    plt.legend()
    plt.show()


def casesdischargedstates():

    #graph on cases/discharged
    #data from kaggle dataset

    #declaring the style

    plt.style.use("seaborn")


    #reading sepcific columns from a csv file
    data = pd.read_csv("data4.csv")
    states = data["State/UTs"]
    cases = data["Total Cases"]
    dis = data["Discharged"]


    #converting them into a nested list(tuple) and sorting them
    x = list(zip(cases,states,dis))
    y = sorted(x,reverse=True)

    data1 = []
    data2 = []
    data3 = []


    for i in y:
        data1.append(i[0])
        data2.append(i[1])
        data3.append(i[2])

    data1 = data1[0:9]
    data2 = data2[0:9]
    data3 = data3[0:9]


    #creating a index list for plotting

    indexes = np.arange(len(data2))

    #plotting the bar graphs with one slightly displaced
    plt.bar(indexes,data1,width=0.25,label = "Total cases",color="#BC5090")
    plt.bar(indexes+0.25,data3,width=0.25,label="Discharged",color="#FFAB05")

    #specifying some properties
    plt.legend()
    plt.xticks(ticks=indexes,labels=data2)
    plt.ylabel("Cases/Discharged in lakhs")
    plt.xlabel("States")
    plt.title("Total cases and discharges by state")

    plt.text(6, 5000000, "*Data obtained from Worldometer.org", fontdict={"family": "serif", "size": 8})


    plt.show()



def casespopulationstates():

    #graph on cases vs population(scatter plot)



    #declaring the style
    plt.style.use("seaborn")

    #reading specific columns from a csv file

    data = pd.read_csv("data4.csv")
    states = data["State/UTs"]
    cases = data["Total Cases"]
    pop = data["Population"]


    #converting the data to nested list(tuple) and sorting them
    x = list(zip(cases,states,pop))
    y = sorted(x,reverse=True)

    data1 = []
    data2 = []
    data3 = []


    for i in y:
        data1.append(i[0])
        data2.append(i[1])
        data3.append(i[2])

    data1 = data1[0:20]
    data2 = data2[0:20]
    data3 = data3[0:20]

    #plotting the graph

    plt.scatter(data3,data1,edgecolors="black",linewidths=1,alpha=0.75,color="red")


    #naming each point in a graph
    for i,label in enumerate(data2):
        plt.annotate(label,(int(data3[i]-10000000),int(data1[i])))



    #specifying some properties

    plt.xlabel("Population")
    plt.ylabel("Covid cases")
    plt.title("Population vs Covid cases")


    plt.show()

while True:
    print("\n")
    print("Graphs available")
    print("\n")
    print("1. Covid cases by countries | Graph type: BAR")
    print("2. Covid cases by countries per year | Graph type: DOUBLE BAR ")
    print("3. Covid deaths by countries | Graph type: BAR")
    print("4. Percentage of global covid cases by countries | Graph type: PIE")
    print("5. Covid cases by states | Graph type: BAR")
    print("6. Covid deaths by states | Graph type: BAR")
    print("7. Percentage of covid cases in India by states | Graph type: PIE")
    print("8. Covid death rate by states | Graph type: HORIZONDAL BAR")
    print("9. Covid cases and discharges by states | Graph type: DOUBLE BAR")
    print("10. Cases vs population by states | Graph type: SCATTER")
    print("E/e Exit the program")

    x = input("Enter the number of the graph you wish to see: ")

    if x == "e" or x == "E":
        sys.exit("Thanks for using the program")

    try:

        if int(x) == 1:
            casecountries()

        if int(x) == 2:
            casecountries_year()

        if int(x) == 3:
            deathcountries()

        if int(x) == 4:
            piecasescountries()

        if int(x) == 5:
            casestates()

        if int(x) == 6:
            deathstates()

        if int(x) == 7:
            piecasesstates()

        if int(x) == 8:
            deathratebystates()

        if int(x) == 9:
            casesdischargedstates()

        if int(x) == 10:
            casespopulationstates()

        else:
            print("Please enter a valid input")

    except ValueError:
        print("Please enter a valid input")
        continue


