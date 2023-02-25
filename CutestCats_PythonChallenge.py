allCats = []    # array for storing all cat objects

class Cat:
    def __init__(self, catName, catDescription, catWeight, catLength, catAppearance, catLife, catImage):
        self.__name = catName                            # string, name of cat
        self.__description = catDescription              # string, description of cat
        self.__weight = catWeight                        # string, avg weight of cat in pounds
        self.__length = catLength                        # string, avg length of cat in feet
        self.__appearance = catAppearance                # string, coat and colour of cat
        self.__lifeExpectancy = catLife                  # string, avg life expectancy in years
        self.__imageUrl = catImage                       # string, link to picture

    def GetCatDetails(self):
        return self.__name, self.__description, self.__weight, self.__length, self.__appearance, self.__lifeExpectancy, self.__imageUrl

    def GetCatLife(self):
        return self.__name, self.__lifeExpectancy


# getting the numerical components in a string
def extractNum(string):
    numbers = [int(i) for i in string.split() if i.isdigit()]    # extracting digits from a string from GeeksforGeeks
    return numbers

# calculating the numerical average of two numbers. If only 1 number present, that number is returned
def calculateAverage(list):
    if len(list) == 1:
        return list[0]
    elif len(list) == 2:
        avg = ((list[0] + list[1])/2)
        return int(avg)


# cleaning up text file
try:
    fr = open("CutestCats.txt", 'r')
    fw = open("CleanCats.txt", 'w')
    while True:
        fileData = fr.readline()
        if fileData == "":
            break
        elif not fileData.isspace():
            fw.write(fileData)
    fr.close()
    fw.close()
except FileNotFoundError:
    print("File not found.")


# writing data from file into array
f = open("CleanCats.txt", 'r')
while True:
    name = f.readline().strip()
    if name == "":
        break
    description = f.readline().strip()
    oldWeight = f.readline().strip()
    if len(extractNum(oldWeight)) == 1 or len(extractNum(oldWeight)) == 2:
        weight = str(calculateAverage(extractNum(oldWeight))) + " pounds"
    else:
        weight = oldWeight[8:]
    oldLength = f.readline().strip()
    if len(extractNum(oldLength)) ==1 or len(extractNum(oldLength)) == 2:
        length = str(calculateAverage(extractNum(oldLength))) + " feet"
    else:
        length = oldLength[8:]
    looks = f.readline().strip()
    oldLife = f.readline().strip()
    if len(extractNum(oldLife)) > 0:
        life = str(calculateAverage(extractNum(oldLife))) + " years"
    else:
        life = oldLife
    img = f.readline().strip()
    allCats.append(Cat(name, description, weight, length, looks, life, img))

catLife = []     # 2d array for storing cat name and cat life expectancy


# storing 2d array with cat name and cat life expectancy for all cats
def getLives():
    for i in range(len(allCats)):
        stats = Cat.GetCatLife(allCats[i])
        print(stats)
        catLife.append(stats)


# sorting the 2d array in order of life expectancy
def bubbleSort():
    passCount = 1
    swapped = True
    while swapped == True:
        swapped = False
        for index in range(len(catLife) - passCount):
            if catLife[index][1] > catLife[index + 1][1]:
                temp = catLife[index]
                catLife[index] = catLife[index + 1]
                catLife[index + 1] = temp
                swapped = True
        passCount +=1


getLives()
bubbleSort()
print(catLife)
