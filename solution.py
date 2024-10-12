class Star_Cinema:
    __hall_list=[]
    def entry_hall(self,hall):
        self.__hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no):
        self.__rows=rows
        self.__cols=cols
        self.__hall_no=hall_no
        self.__show_list=[]
        self.__idList=[]
        self.__seats={}
        super().__init__()
        self.entry_hall(self)


# entry_show method

    def entry_show(self,id,movie_name,time):
        self.__show_list.append(f'Id: {id}, Movie name: {movie_name},Time: {time}')
        self.__seats[id]=[]
        self.__idList.append(id)
        for i in range(self.__rows):
             tmp=[]
             for j in range(self.__cols):
                tmp.append('Available')
             self.__seats[id].append(tmp)

# book_seats method

    def book_seats(self,id,seatList):
        for i in range(len(seatList)):
            row=seatList[i][0]-1
            col=seatList[i][1]-1
            if self.__rows<row+1 or self.__cols<col+1:
               print('\n\tYou have enter invalid seat number')
               continue
            if self.__seats[id][row][col]=='Available':
               print(f'\n\n\tYou have successfully book {row+1}{col+1} seat.\n\tEnjoy the show.')
               self.__seats[id][row][col]=f'Booked by someone'
            else:
               print(f'\n\n\tSeat {row+1}{col+1} is booked by someone. Please choose another seat.')
        

# view_show_list method

    def view_show_list(self):
        for i in self.__show_list:
            print(f'\n\t{i}')

# view_available_seats method

    def view_available_seats(self,id):
        print('\n\tSeat Status:')
        for i in range(0,len(self.__seats[id])):
            for j in range(0,len(self.__seats[id][i])):
                print(f'\tSeats no: {i+1},{j+1}, Status: {self.__seats[id][i][j]}')
        print('\n')
# check id 
    def checkId(self,id):
        if id in self.__idList:
            return True
        return False
    

st=Star_Cinema()
hall1=None
userType=None
totalShow=0
while True:
    
    userType=input('\tAre you want to buy ticket or view available seats for today or view showlist? (Y/N):')
    if userType=='Y' or userType=='y':
        if hall1==None:
            print('\tHall not prepared. If you are from administration please press n.')
            continue
            
    if userType=='y' or userType=='Y':
     while True:
        option=int(input('\tEnter 1 for available shows today, 2 for view available seats, 3 for booking seats, 0 for exit:'))
        if option==1:
            if totalShow<1:
               print('\n\tNo show available')
               continue
            hall1.view_show_list()
        elif option==2:
            if totalShow<1:
               print('\n\tNo show available')
               continue
            hall1.view_show_list()
            id=int(input('\tEnter movie id:'))
            if(hall1.checkId(id)==False):
                print('\tIncorrect movie id.')
                continue
            hall1.view_available_seats(id)
        elif option==3:
            if totalShow<1:
               print('\n\tNo show available')
               continue
            hall1.view_show_list()
            id=int(input('\tEnter movie id:'))
            if(hall1.checkId(id)==False or totalShow<1):
                print('\tIncorrect movie id.')
                continue
            # hall1.view_available_seats(id)
            hall1.view_available_seats(id)
            howManySeatsYouNeed=int(input('\tHow many seats you need? '))
            seatList=[]
            for i in range(howManySeatsYouNeed):
                seatNumberRow=int(input('\t(N.B. Before entering seat number check available seats.)\n\tEnter your desired seat row number:'))
                seatNumberCol=int(input('\tEnter your desired seat col number:'))
                seatList.append([seatNumberRow,seatNumberCol])
                print(f'\n\tSelected seats are: {seatList}')
            hall1.book_seats(id,seatList)
        else:
           print('\tThank you for visiting')
           break
    elif userType=='N' or userType=='n':
        userType=input('\n\tAre you from administration?(Y/N):')
        if userType=='Y' or userType=='y':
            userName=input('\n\tEnter user name:')
            userPassword=input('\n\tEnter password:')
            if userName=='admin' and userPassword=='admin':
                userType='admin'
                print('\n\tAdmin Log in successful')
                while True:
                  option=int(input('\n\t1 for prepared hall, 2 for entry a show, 3 for view show list, 4 for available seats, 0 for exit:'))
                  if option==0:
                    break
                  elif option==1:
                    if hall1!=None:
                       print('\tHall already exist')
                       continue
                    rows=int(input('\n\tEnter number of column:'))
                    cols=int(input('\n\tEnter number of column:'))
                    hall_no=int(input('\n\tEnter hall no:'))
                    hall1=Hall(rows,cols,hall_no)
                    print('\tHall prepared successfully')
                  elif hall1==None:
                     print('\tHall not prepare please prepare hall first')
                     continue
                  elif option==2:
                    id=int(input('\tEnter show id:'))
                    movie_name=input('\tEnter show name:')
                    time=input('\tEnter show time:')
                    hall1.entry_show(id,movie_name,time)
                    totalShow+=1
                  elif option==3:
                     if totalShow<1:
                        print('\tNo show available')
                        continue
                     hall1.view_show_list()
                  elif option==4:
                     if totalShow<1:
                        print('\tNo show available')
                        continue
                     hall1.view_show_list()
                     id=input('\n\tEnter id:')
                     if hall1.checkId(int(id)):
                        hall1.view_available_seats(int(id))
                     else:
                      print('\tInvalid show id')
            else:
               print('\tIncorrect administrator credential. Try again')
        else:    
           yes=input('\n\tAre you want to exit?(y/n)')
           if yes=='y' or yes=='Y':
            break
           else:
            continue

    





"""
Testcase 1: hall is not ready
Testcase 2: hall is ready but no entry show
Testcase 3: inccorrect show_id
Testcase 4: If someone gives a wrong id of a show
Testcase 5: If someone tries to book a seat that is invalid
Testcase 6: If someone tries to book a seat that is already booked
"""