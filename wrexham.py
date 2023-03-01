class wrexham:
    def __init__(self, playernum, fname, lname, pos):
        self.__PlayerNumber = playernum             # string
        self.__Forename = fname                     # string
        self.__Surname = lname                      # string
        self.__Position = pos                       # string
        self.__CommunityInvolvement = 0.0           # real
        self.__Injured = False                      # boolean

    def GetPlayerInfo(self):
        name = self.__Forename + " " + self.__Surname
        return name, self.__Position

    def ChangeCommunityInvolvement(self, change):
        self.__CommunityInvolvement = self.__CommunityInvolvement + change

    def ChangeInjured(self):
        if self.__Injured == False:
            self.__Injured = True
        elif self.__Injured == True:
            self.__Injured = False


Players = []

try:
    f = open("wrexham.txt", "r")
    while True:
        playerNum = f.readline().strip()
        if playerNum =="":
            break
        fName = f.readline().strip()
        sName = f.readline().strip()
        position = f.readline().strip()
        Players.append(wrexham(playerNum, fName, sName, position))
    f.close()
except FileNotFoundError:
    print('Sorry file not found.')


for i in range(len(Players)):
    print(wrexham.GetPlayerInfo(Players[i]))


        