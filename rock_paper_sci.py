import random

def user_choice():
    choice=input('Choose one: r,p,s for rock, paper and scissor: ')
    print(f'User choice: {choice}')
    return choice

def computer_choice():
    choice_container=['r','p','s']
    rand_num=random.randint(0,len(choice_container)-1) 
    choice=choice_container[rand_num]
    print(f'Computer choice: {choice}')
    return choice
     
def check_winner():
    user_result=user_choice()
    computer_result=computer_choice()
    if user_result==computer_result:
        print(f'User: {user_result} Computer: {computer_result} DRAW!')
    elif user_result=='r' and computer_result=='s' or user_result=='p' and computer_result=='r' or user_result=='s' and computer_result=='p':
        print(f'User: {user_result} Computer: {computer_result} USER WIN!') 
    else:
        print(f'User: {user_result} Computer: {computer_result} COMPUTER WIN!') 
    user_inquiry=input('Do you want to continue playing?: (Y/N) '.lower()) 
    return user_inquiry   

def main():
    print('ROCK BEATS SCISSOR | PAPER BEATS ROCK | SCISSOR BEATS PAPER')
    game_on=True
    while game_on:
        result=check_winner()
        if result=='n':
            game_on=False
    print('Game finished')        
        

        
    
if __name__=='__main__':
    main()
        