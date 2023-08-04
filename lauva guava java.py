import random
score=0
computer_score=0
while True:
    choice=input("lava guava java")
    options = ['lava','guava',"java"]
    enemy = random.choice(options)
    if choice ==enemy :
        print ("just win") 
    if choice == 'guava' and enemy == 'java':
        print ("you win guava beats java it can make a delicouse juice that guava cant resist")
        score=score+1
    if choice == "java" and enemy == "lava":
        print("java beats lava becuase it can cool it down and salitify it because its a versitile programing language" ) 
        score=score+1
    if choice == "lava" and enemy== 'guava':
        print('lava beats guava because it can burn it and turn it into ashes')
        score=score+1
    if choice =="guava" and enemy == "java":
        print ("YOU LOSE lava beats guava because it can burn it and turn it into ashes")
        score=score-1
    if choice=="lava" and enemy == "java":
        print ("you lose because java beats lava becuase it can cool it down and salitify it because its a versitile programing language")
        score=score-1
    if choice=="java" and enemy =='guava':
        print ("you lose guava beats java it can make a delicouse juice that guava cant resist")
        score=score-1
    print(f'the score is: {score} to {computer_score}')
    don=input ("wanna play again")
    if don == "no":

        break