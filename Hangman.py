
import numpy as np

global word
word = "apple"
global word_list
#make the word as list
word_list = [char for char in word]
global answerlist
answerlist = np.full((1, len(word_list)), "_", dtype='<U1')
print(answerlist)

def no_empty(matrix):
    if "_" in answerlist:
        return False
    else:
        return True
global game
game=True
def start():
    guesses = 5
    length= len(word)
    print("length of the word is ",length)
    while (guesses>0):
        if game==False:
            break
        print("=====No of Guesses is ",guesses,"=====")
        character = input ("Enter the guessed character : ")
        if character in word:
            for i in range(len(word)):
                if word[i]==character:
                    if answerlist[0][i]=="_":
                        answerlist[0][i]=word[i]
                        if no_empty(answerlist):
                            
                            print("=========YOU WON THE GAME=========")
                            print(answerlist)
                            game_over=False
                            break
                        else:
                            pass
                        
                        print(answerlist)
                    
            
            
        else:
            print("!! You have guessed the worng character !!")
            guesses= guesses-1
    else:
        print("========YOUR GUESSES ARE OVER============")
start()