#Program 3 – Girl Guide Cookies
#Description:   The organizers of the annual Girl Guide cookie sale event want to raise 
#               the stakes on the number of cookies sold and are offering cool prizes to
#               those guides who go above and beyond in their sales efforts. The organizers
#               want a program to print the guide list and their prizes.

#Student #:     W0487099
#Student Name:  Alex Barr



def NumberOfGuides(_maxGuides):
    while True:
        try:
            n = int(input("Enter the number of guides selling cookies: "))
            break
        except ValueError:
            print("Nice try! Try again with a number")
            # NumberOfGuides(_maxGuides)
            # break #<--------------  Still don't know if this is necessary, but I'll keep it in there because its been working for me
   
    if (n < 1) or (n > _maxGuides): #I know max guides isn't a limitation in the program but I don't want this program to get out of hand, also hardcoding zero as minimum value because it is a real limitation that will break the code if entered
        print("Nice try! Try again with a reasonable number")
        NumberOfGuides(_maxGuides)
    else:
        return n

def GetGuideInfo(_iteration, _list):
    while True:
        try:
            _name = input(f"Enter the name of guide #{_iteration + 1}: ")
            break
        except ValueError:
            print("Well Done! This shouldn't be an error so it's really weird if your seeing that")
            # GetGuideInfo(_iteration, _list)
            # break #<--------------  Still don't know if this is necessary, but I'll keep it in there because its been working for me
    
    while True:
        try:
            _boxes = int(input(f"Enter the number of boxes sold by {_name}: "))
            break
        except ValueError:
            print("Please input a number.")
    
    _list[0].append(_name)
    _list[1].append(_boxes)
    print("")

def AverageBoxesSold(_list):
    return sum(_list[1])/len(_list[1])

def DeterminePrizes(_guideInfo, _prizes, _numberOfGuides):

    for i in range(_numberOfGuides):
        if _guideInfo[1][i] == max(_guideInfo[1]):
            _guideInfo[2][i] = _prizes[0]
        elif _guideInfo[1][i] > AverageBoxesSold(_guideInfo):
            _guideInfo[2][i] = _prizes[1]
        elif _guideInfo[1][i] > 1:
            _guideInfo[2][i] = _prizes[2]
        else:
            _guideInfo[2][i] = _prizes[3]

def AutoAppend(_list, _length, _height):
    for x in range((_length)):
        _list.append("")
        for y in range((_height)):
            _list[x].append("")
    print(_list)


def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
                #names    boxes   prizes
    guideInfo = [] #[   []  ,   []  ,   [] ]
    prizes = ["Trip to Girl Guide Jamboree in Aruba!", "Super Seller Badge", "Left over cookies", ""]
    AutoAppend(guideInfo,3,5)
    #Enter the number of guies selling cookies
    numberOfGuides = int(NumberOfGuides(5))
    print("")
    
    #Loop
    for i in range(numberOfGuides):
        #Enter the name of the guide
        #Enter the number of boxes sold by the above guide
        GetGuideInfo(i, guideInfo)

    #Show the average number of boxes sold by each guide
    print(f"The average number of boxes sold by each guide was: {AverageBoxesSold(guideInfo)}")

    DeterminePrizes(guideInfo, prizes, numberOfGuides)
    #Display guides and prizes (Optionl extra version where they are ranked)
    print("Guide:                           Prizes Won:")
    print("_"*50)
    for i in range(numberOfGuides):
        print(f"{guideInfo[0][i]}               - ")





    # YOUR CODE ENDS HERE

main()