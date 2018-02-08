import random
import time

print("\033[H\033[J")
print("/********************************************************/\n")
print("                   Rock-Paper-Scissor                   \n")
print("/********************************************************/\n")


k = 0
comp_move = [" "," "," "," "," "]
user_move = [" "," "," "," "," "]
for i in range(5):
    rand_num = random.randint(1,3)
    if rand_num == 1:
        comp_move[k] = "Rock"
    elif rand_num == 2:
        comp_move[k] = "Paper"
    elif rand_num == 3:
        comp_move[k] = "Scissor"
    k = k + 1

scUser = 0
scComp = 0

print("---Welcome---\n")

k=0
for i in range(5):
    file = open("score.txt","w")
    file.write(str(scUser))
    file.write(str(scComp))
    file.close()
    print("\nPlay\n")
    choice='a'
    time.sleep(.800)
    while(choice!='y'):
        m = 3
        for j in range(3):
            print("\033[H\033[J")
            print(m)
            time.sleep(1)
            m = m - 1
        file = open("testfile.txt","r")
        move = file.readline()
        file.close()
        print("\nYour move => "+move)
        time.sleep(1)
        choice = input("\nPress Y if its correct : ")
        if choice=='y':
            user_move[k]=move
            time.sleep(.500)
            print("\nPCs move => "+comp_move[k])
            print("\n"+user_move[k]+" Vs "+comp_move[k])
            if user_move[k]=="Scissor" and comp_move[k]=="Rock":
                scComp = scComp + 1
                time.sleep(1)
                print("\nYou lose")
                time.sleep(1)
                print("\033[H\033[J")
            elif user_move[k]=="Scissor" and comp_move[k]=="Paper":
                scUser = scUser + 1
                time.sleep(1)
                print("\nYou win")
                time.sleep(1)
                print("\033[H\033[J")
            elif user_move[k]=="Rock" and comp_move[k]=="Paper":
                scComp = scComp + 1
                time.sleep(1)
                print("\nYou lose")
                time.sleep(1)
                print("\033[H\033[J")
            elif user_move[k]=="Rock" and comp_move[k]=="Scissor":
                scUser = scUser + 1
                time.sleep(1)
                print("\nYou win")
                time.sleep(1)
                print("\033[H\033[J")
            elif user_move[k]=="Paper" and comp_move[k]=="Scissor":
                scComp = scComp + 1
                time.sleep(1)
                print("\nYou lose")
                time.sleep(1)
                print("\033[H\033[J")
            elif user_move[k]=="Paper" and comp_move[k]=="Rock":
                scUser = scUser + 1
                time.sleep(1)
                print("\nYou win")
                time.sleep(1)
                print("\033[H\033[J")
            else:
                time.sleep(1)
                print("\nDraw")
                time.sleep(1)
                print("\033[H\033[J")
            k = k+1
            time.sleep(2)
k=0
for i in range(5):
    print("\n"+user_move[k]+" Vs "+comp_move[k])
    k=k+1

if scUser<scComp:
    print("\nGame over...You lost :(")
elif scUser==scComp:
    print("\nGame draw")
else:
    print("\nCongratulations!! You won :)")