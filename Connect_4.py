#CONNECT 4
#By Alexandros Tourloukis
#June 24, 2023
import os
import readchar
#SlotList gets read like this
# 0 1 2 3  4  5  6
# 7 8 9 10 11 12 13
#...          40 41

def clear_terminal():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

class Slot:
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol

SlotList = []
for k in range(0, 42):
    SlotList.append(Slot((k % 7), (k // 7), " "))

def FindLowest(userposition, SlotList, symbol):
    global turn_count
    lowest = -1
    for i in range(0, 42):
        if SlotList[i].x == userposition and SlotList[i].y > lowest and SlotList[i].symbol == " ":
            lowest = SlotList[i].y
    if lowest == -1:
        return SlotList
    for j in range(0, 42):
        if SlotList[j].x == userposition and SlotList[j].y == lowest:
            
            turn_count += 1  # Increment turn count when a piece is placed

            SlotList[j].symbol = symbol
            break
    return SlotList

def DrawScreen(turn_count, top_list):
    top_string = ""
    print("Player:", ((turn_count % 2) + 1), "        turn:", turn_count)
    i=0
    while top_list[i]==' ':
        i=i+1
    if turn_count%2==0 and top_list[i]=='O':
        top_list[i]='X'
    if turn_count%2==1 and top_list[i]=='X':
        top_list[i]='O'
    for k in range(0, 29):
        top_string += top_list[k]
    print(top_string)
    print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")

    j = 0
    for i in range(0, 6):
        print("|", SlotList[j].symbol, "|", SlotList[j+1].symbol, "|", SlotList[j+2].symbol, "|", SlotList[j+3].symbol, "|", SlotList[j+4].symbol, "|", SlotList[j+5].symbol, "|", SlotList[j+6].symbol, "|")
        print("▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁")
        j += 7
    print("Press Space to exit")

def GetUserInput(symbol, top_list, userposition, SlotList):
    global win_flag
    global turn_count  
    while True:
        key = readchar.readkey()
        if key == readchar.key.DOWN:
            top_list[userposition * 4 + 2] = symbol
            SlotList = FindLowest(userposition, SlotList, symbol)
            
            top_list[userposition * 4 + 2] = symbol
            break
        elif key == readchar.key.RIGHT:
            top_list[userposition * 4 + 2] = " "
            userposition = (userposition + 1) % 7
            top_list[userposition * 4 + 2] = symbol
        elif key == readchar.key.LEFT:
            top_list[userposition * 4 + 2] = " "
            userposition = (userposition - 1) % 7
            top_list[userposition * 4 + 2] = symbol
        elif key==readchar.key.SPACE:
            exit()
        clear_terminal()
        DrawScreen(turn_count, top_list)
    return top_list, userposition, SlotList

def CheckHorizontal(SlotList, turn_count, top_list):
    global win_flag  # Declare global to modify it
    i = 0
    while i < 39 :
        if ((SlotList[i].symbol == SlotList[i + 1].symbol == SlotList[i + 2].symbol == SlotList[i + 3].symbol) and (SlotList[i].symbol != " ")and (i%7<4)):
                if SlotList[i].symbol == "X":
                    win_flag = 1
                    clear_terminal()
                    DrawScreen(turn_count, top_list)
                    print("Player 1 wins!")
                else:
                    win_flag = 2
                    clear_terminal()
                    DrawScreen(turn_count, top_list)
                    print("Player 2 wins!")
                return
        else:
            i += 1
def CheckVertical(SlotList, turn_count, top_list):
    global win_flag
    for i in range (41,20,-1):
        if (SlotList[i].symbol==SlotList[i-7].symbol==SlotList[i-14].symbol==SlotList[i-21].symbol)and (SlotList[i].symbol != " "):
            if SlotList[i].symbol == "X":
                    win_flag = 1
                    clear_terminal()
                    DrawScreen(turn_count, top_list)
                    print("Player 1 wins!")
            else:
                win_flag = 2
                clear_terminal()
                DrawScreen(turn_count, top_list)
                print("Player 2 wins!")
            return
        
def CheckDiagonalLeft(SlotList, turn_count, top_list):
    global win_flag
    for i in range(41, 23,-1):  
        if (SlotList[i].symbol == SlotList[i -8].symbol == SlotList[i -16].symbol == SlotList[i -24].symbol) and (SlotList[i].symbol != " ") and i%7>2:
                if SlotList[i].symbol == "X":
                    win_flag = 1
                    clear_terminal()
                    DrawScreen(turn_count, top_list)
                    print("Player 1 wins!")
                else:
                    win_flag = 2
                    clear_terminal()
                    DrawScreen(turn_count, top_list)
                    print("Player 2 wins!")
                return

def CheckDiagonalRight(SlotList, turn_count, top_list):
    global win_flag
    for i in range(21, 39):
            if ((SlotList[i].symbol == SlotList[i - 6].symbol == SlotList[i - 12].symbol == SlotList[i - 18].symbol) and (SlotList[i].symbol != " ")and (i%7<4)):
                if SlotList[i].symbol == "X":
                    win_flag = 1
                    clear_terminal()
                    DrawScreen(turn_count, top_list)
                    print("Player 1 wins!")
                else:
                    win_flag = 2
                    clear_terminal()
                    DrawScreen(turn_count, top_list)
                    print("Player 2 wins!")
                return    
            


def main(SlotList):
    global turn_count
    turn_count = 0
    userposition = 3
    while True:
        if turn_count % 2 == 0:
            symbol = "X"
        else:
            symbol = "O"
        top_list = [" "] * 14 + [symbol] + [" "] * 14
        global win_flag
        win_flag = 0
        while turn_count < 42 and win_flag == 0:
            if turn_count % 2 == 0:
                symbol = "X"
            else:
                symbol = "O"

            clear_terminal()
            DrawScreen(turn_count, top_list)
            top_list, userposition, SlotList = GetUserInput(symbol, top_list, userposition, SlotList)
            if turn_count > 6:
                CheckHorizontal(SlotList, turn_count, top_list)
                CheckVertical(SlotList, turn_count, top_list)
            if turn_count >9:
                CheckDiagonalLeft(SlotList, turn_count, top_list)
                CheckDiagonalRight(SlotList, turn_count, top_list)
        while turn_count==42 and win_flag==0:
            print("Tie game!\n Would you like to play again?\ny/n")
            if readchar.readkey() == "n":
                exit()
            elif readchar.readkey() == "y":
                turn_count = 0
                win_flag = 0
                userposition=3
                SlotList.clear()
                for k in range(0, 42):
                    SlotList.append(Slot((k % 7), (k // 7), " "))
            else:
                win_flag==0


        while win_flag == 1:
            print("Player 1 won!\n Would you like to play again?\ny/n")
            if readchar.readkey() == "n":
                exit()
            elif readchar.readkey() == "y":
                turn_count = 0
                win_flag = 0
                userposition=3
                SlotList.clear()
                for k in range(0, 42):
                    SlotList.append(Slot((k % 7), (k // 7), " "))
            else:
                win_flag==1
        while win_flag == 2:
            print("Player 2 won!\n Would you like to play again?\ny/n")
            if readchar.readkey() == "n":
                exit()
            elif readchar.readkey() == "y":
                turn_count = 0
                win_flag = 0
                userposition=3
                SlotList.clear()
                for k in range(0, 42):
                    SlotList.append(Slot((k % 7), (k // 7), " ")) 
            else:
                win_flag==2
main(SlotList)

