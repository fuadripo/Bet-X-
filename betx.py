
import random 

def betting():
    print('''
           ---------------
          |      BetX     |
           ---------------
          ''')
    balance = 0
    lost = 0
    deposit = int(input("Deposit Amount: "))
    balance += deposit

    while True:

        if not balance == 0:
            ex_it = input("Do You Want Exit? Y/N : ").upper()
            if ex_it == "Y":
                break
            
            bet_amount = int(input("Bet Amount: "))

            if bet_amount > 0 and bet_amount <= balance:

                bet_x = int(input("Bet Number (1, 2, ...10): "))
                if bet_x >= 1 and bet_x <= 10:
                    balance -= bet_amount
                    
                    bet_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

                    bet_num = random.choice(bet_numbers)

                    for bet_loop in range(1, bet_num+1):
                        print(f"{bet_loop}x")

                        if bet_x == bet_loop:
                            bet_amount *= bet_loop
                            balance += bet_amount

                    if bet_x > bet_num:

                        crushed = [
                            " ---------------------- ",
                            "|      CRUSHED!        |",
                            " ---------------------- "
                        ]
                            
                        for crush in crushed:
                            print(crush)
                        
                        print(f"You lost : {lost + bet_amount}$")


                    print(f"Current Balance : {balance}$")


                else:
                    print("You have to Bet between 1x to 10x ")
                    
                    
            else:
                print(f"You Have {balance}$, You have to Bet between 1 to {balance}$")
                

        else:
            print("Keep deposit more than zero!")
            betting()



betting()
