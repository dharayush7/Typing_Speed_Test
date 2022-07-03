from distutils.log import error
from time import *
import random as r


def mistake(partest,user):
    
    error=0
    
    for i in range(len(partest)):
        try:
            if partest[i] != user[i]:  
                error= error +1
        except:  
            error= error +1
    return error

def speed_time(time_s,time_e,userinput):
    
    time_deley = time_e - time_s
    time_r = round(time_deley,2)
    speed = len(userinput)/time_r
    
    return round(speed)
print(" ")   
print("           ******Typing Speed Claculator*****")
while True:
    
    print(" ")
    start = input("Enter 'y' for start test or 'n' for decline : ")
    
    if start == "y":
        
        
        test = ["Please take your dog, Cali, out for a walk he really needs some exercise!",
                "What a beautiful day it is on the beach, here in beautiful and sunny Hawaii.",
                "Rex Quinfrey, a renowned scientist, created plans for an invisibility machine.",
                "Do you know why all those chemicals are so hazardous to the environment?",
                "You never did tell me how many copper pennies where in that jar; how come?",
                "Max Joykner sneakily drove his car around every corner looking for his dog.",
                "The two boys collected twigs outside, for over an hour, in the freezing cold!",
                "When do you think they will get back from their adventure in Cairo, Egypt?",
                "Trixie and Veronica, our two cats, just love to play with their pink ball of yarn.",
                "We climbed to the top of the mountain in just under two hours; isn't that great?",
                "Hector quizzed Mr. Vexife for two hours, but he was unable to get any information.",
                "I have three things to do today: wash my car, call my mother, and feed my dog.",
                "Xavier Puvre counted eighty large boxes and sixteen small boxes stacked outside.",
                "The Reckson family decided to go to an amusement park on Wednesday.",
                "That herd of bison seems to be moving quickly; does that seem normal to you?",
                "All the grandfather clocks in that store were set at exactly 3 o'clock.",
                "There are so many places to go in Europe for a vacation--Paris, Rome, Prague, etc.",
                "Those diamonds and rubies will make a beautiful piece of jewelry.",
                "The steamboats seemed to float down the Mississippi River at a snail's pace.",
                "In order to keep up at that pace, Zack Squeve would have to work all night.kk"
                ]
        test1 = r.choice(test)
        
        print(" ")
        print(test1)
        print(" ")
       
        
        
        time_1 = time()
        testinp=input(" Enter : ")
        print(" ")
        time_2 = time()

        print('speed : ', speed_time(time_1,time_2,testinp),'word/sec.')
        print("error : ", mistake(test1, testinp))
    elif start == "n" :
        print(" ")
        print("               Thank You")
        print(" ")
        break
    else:
        print("Wrong input!")
        


