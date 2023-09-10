class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """

    def __init__(self):
        """Construct objects of type Board, with the given width and height."""
       
        self.board = [[' ']*8 for row in range(8)]
        self.board[3][3] = "B"
        self.board[3][4] = "W"
        self.board[4][3] = "W"
        self.board[4][4] = "B"
       
        self.LetToNum = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7}

        # We do not need to return anything from a constructor!

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board."""
        s = "\n    A B C D E F G H"
        s +=  "\n   "+ (17) * '-' + "\n"                    # The string to return
        for row in range(0, 8):
            s += str(row) + '  |'
            for col in range(0, 8):
                s +=  self.board[row][col] + '|'
            
            s += "\n   "+ (17) * '-' + "\n" 
            
         
          # Bottom of the board
        s+="    "
       
       
        # Add code here to put the numbers underneath
        return s       # The board is complete; return it 
    
    def addMove(self,row,col,bw):
        row = self.LetToNum[row]
     
        if self.isValidMove(col,row):
            #change horizontal
            self.board[col][row] = bw
            self.board[col] = self.checkHorizontal(self.board[col],row,bw)
            #change vertical
            temp = [self.board[x][row] for x in range(8)]
            temp = self.checkHorizontal(temp,col,bw)
            for i in range(8):
                self.board[i][row] = temp[i]

            #change positive direction
            temp = [bw]
            end = False
            counter = 1
            while not(end):
                try:
                    temp += [self.board[col+ counter][row+counter]]
                    counter+=1
                except:
                    end = True
            end = False
            counter = 1
            print(temp)
            while col+counter<8 and row-counter>-1:


                print(self.board[col+counter][row-counter])
                temp = [self.board[col+ counter][row-counter]] + temp
                counter+=1
             
                 
            print(temp)
            
           

    def checkHorizontal(self,row,newMove,bw):
        
        return (self.changeHorizontal(row[:newMove],bw,True)+[bw]+self.changeHorizontal(row[newMove+1:],bw,False))
    

    def checkVertical(self,col, newMove, bw):
        pass
      
     

    def changeHorizontal(self,row,bw,backwards):
        
        if bw not in row:
            return row
        else:
            found = False
            if backwards:
                row = row[::-1]
            for square in range(len(row)):
                if row[square] != bw and not(found):
                    row[square] = bw
                else:
                    found = True
            if backwards:
                row = row[::-1]
            
            return row
        

    def isValidMove(self,row,col):
        if self.board[col][row] == " ":
            return True
        return False
    
    def aiMove(self):
        pass
    
    def playGame(self):
        print(self)
        while not(self.isFull()):
            choice = input("Where would you like to play your move? ")
            self.addMove(choice[0],int(choice[1]),"W")
            print(self)

    def isFull(self):
        for row in range(8):
            for col in range(8):
                if self.board[col][row] == " ":
                    return False
        return True
    


        


b = Board()
b.board[0][4] = "W"
b.board[1][4] = "B"

b.board[3][4] = "B"
b.board[4][4] = "B"
b.board[5][4] = "W"
b.board[6][4] = "W"
b.board[7][4] = "B"

b.playGame()
    