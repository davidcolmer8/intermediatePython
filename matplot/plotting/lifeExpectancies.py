from matplotlib import pyplot
data = open("life_expectancies_usa.txt", "r").readlines()

dates = []
maleLife = []
femaleLife = []

for line in data:
    date, maleLifeExp, femaleLifeExp = line.split(',')
    dates.append(date)
    maleLife.append(float(maleLifeExp))
    femaleLife.append(float(femaleLifeExp))

pyplot.plot(dates, maleLife, "bo-", label = "Men")
pyplot.plot(dates, femaleLife, "mo-", label = "Women")
pyplot.legend(loc= "best")
pyplot.ylabel("Age")
pyplot.xlabel("Year")
pyplot.title("Title")
pyplot.show()

