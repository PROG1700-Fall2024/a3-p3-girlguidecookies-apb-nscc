#Program 3 – Girl Guide Cookies
#Description:   The organizers of the annual Girl Guide cookie sale event want to raise 
#               the stakes on the number of cookies sold and are offering cool prizes to
#               those guides who go above and beyond in their sales efforts. The organizers
#               want a program to print the guide list and their prizes.

#Student #:     W0487099
#Student Name:  Alex Barr


#Get the number of girl guides
def NumberOfGuides(_maxGuides):
    while True:
        try:
            n = int(input("Enter the number of guides selling cookies: "))
            break
        except ValueError:
            print("Error! Try again with a number")
            # NumberOfGuides(_maxGuides)
            # break #<--------------  Still don't know if this is necessary, but I'll keep it in there because its been working for me
   
    if (n < 1) or (n > _maxGuides): #I know max guides isn't a limitation in the program but I don't want this program to get out of hand, also hardcoding zero as minimum value because it is a real limitation that will break the code if entered
        print("Incorrect value. Try again.")
        return NumberOfGuides(_maxGuides)
    else:
        return n

#This is the function to get the name and boxes sold of the girl guides, as well as another list that will be filled with prizes later on
def GetGuideInfo(_iteration, _list):
    while True:
        try:
            _name = input(f"Enter the name of guide #{_iteration + 1}: ")
            break
        except ValueError:
            print("This shouldn't be an error so it's really weird if your seeing this")
            # GetGuideInfo(_iteration, _list)
            break #<--------------  Still don't know if this is necessary, but I'll keep it in there because its been working for me
    
    while True:
        try:
            _boxes = int(input(f"Enter the number of boxes sold by {_name}: "))
            if _boxes < 0:
                print("Cannot sell less than zero boxes. Try again.")
                continue
            break
        except ValueError:
            print("Please input a number.")
            continue
    
    _list[0].append(_name)
    _list[1].append(_boxes)
    print("")

#Gets the average number of boxes sold
def AverageBoxesSold(_list):
    return sum(_list[1])/len(_list[1])

#This adds the appropriate prizes based on the other guide information in the guideInfo list
def DeterminePrizes(_guideInfo, _prizes, _numberOfGuides):

    for i in range(_numberOfGuides):
        if _guideInfo[1][i] == max(_guideInfo[1]): #If the guide has sold the most cookies (For simplicities sake I'll say ties share the top prize)
            _guideInfo[2].append(_prizes[0]) 
        elif _guideInfo[1][i] > AverageBoxesSold(_guideInfo): #If they aren't the winner, if they have over the average amount of boxes sold they get a badge
            _guideInfo[2].append(_prizes[1]) 
        elif _guideInfo[1][i] > 0: #If they have sold more than zero boxes then they get to share the cookies
            _guideInfo[2].append(_prizes[2]) 
        else:
            _guideInfo[2].append(_prizes[3])  #They don't get a prize if they didn't sell any boxes.

#This is just a for fun function I made that will sort the guides by rank and display them in the right order
def SortByPlace(_numberOfGuides, _guideInfo):
    print("")
    _sort = input("Would you like to sort by rank? (y/n): ")

    if _sort.lower() == "n":
        return
    elif _sort.lower() == "y":
        print("")
        print("Guide:       Boxes Sold:                        Prizes Won:")
        print("---------------------------------------------------------------------------")
        print("")

        _tempList = [[],[],[]]
        
        #Go through guideInfo looking for the person with the most boxes sold, append them to a temporary list and del the index from guideInfo (each index in each row for siplicity and organization)
        x = 0
        while (len(_guideInfo[0]) > 0):
            if _guideInfo[1][x] == max(_guideInfo[1]):
                _tempList[0].append(_guideInfo[0][x])
                _tempList[1].append(_guideInfo[1][x])
                _tempList[2].append(_guideInfo[2][x])
                del _guideInfo[0][x]
                del _guideInfo[1][x]
                del _guideInfo[2][x]
                x = 0
                continue
            else:
                x += 1

        #Recompile the guideInfo list by simply going through the list one index at a time (for all rows)
        for i in range(len(_tempList[0])): #Using the range of one of the lists because they are all the same size and using it without [] gave an error
            _guideInfo[0].append(_tempList[0][i])
            _guideInfo[1].append(_tempList[1][i])
            _guideInfo[2].append(_tempList[2][i])


        for i in range(_numberOfGuides):
            print(f"#{i+1}\t{_guideInfo[0][i]}\t\t{_guideInfo[1][i]}\t\t\t\t- {_guideInfo[2][i]} ")
    else:
        print("Please enter y or n.")
        return SortByPlace(_numberOfGuides, _guideInfo)



def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
                #names    boxes   prizes
    guideInfo = [   []  ,   []  ,   [] ]
    prizes = ["Trip to Girl Guide Jamboree in Aruba!", "Super Seller Badge", "Left over cookies", ""]

    #Enter the number of guies selling cookies
    numberOfGuides = int(NumberOfGuides(100))
    print("")
    
    #Loop
    for i in range(numberOfGuides):
        #Enter the name of the guide
        #Enter the number of boxes sold by the above guide
        GetGuideInfo(i, guideInfo)

    #Show the average number of boxes sold by each guide
    print(f"The average number of boxes sold by each guide was: {AverageBoxesSold(guideInfo):.1f}") #Updated to round average
    print("")
    DeterminePrizes(guideInfo, prizes, numberOfGuides)
    #Display guides and prizes (Optionl extra version where they are ranked)
    print("Guide:                           Prizes Won:")
    print("---------------------------------------------------------------------------")
    print("")
    for i in range(numberOfGuides):
        print(f"{guideInfo[0][i]}\t\t\t\t\t\t- {guideInfo[2][i]} ")

    SortByPlace(numberOfGuides, guideInfo)
    print("")


    # YOUR CODE ENDS HERE

main()