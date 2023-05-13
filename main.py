# remaking rock, paper, scissors
import os, time, random
import colorama
from termcolor import colored

os.system('cls' if os.name == 'nt' else 'clear')

rock_="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper_="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor_="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


logo = """
██████╗  ██████╗  ██████╗██╗  ██╗    ██████╗  █████╗ ██████╗ ███████╗██████╗     ███████╗ ██████╗██╗███████╗███████╗ ██████╗ ██████╗ ███████╗
██╔══██╗██╔═══██╗██╔════╝██║ ██╔╝    ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗    ██╔════╝██╔════╝██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝
██████╔╝██║   ██║██║     █████╔╝     ██████╔╝███████║██████╔╝█████╗  ██████╔╝    ███████╗██║     ██║███████╗███████╗██║   ██║██████╔╝███████╗
██╔══██╗██║   ██║██║     ██╔═██╗     ██╔═══╝ ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗    ╚════██║██║     ██║╚════██║╚════██║██║   ██║██╔══██╗╚════██║
██║  ██║╚██████╔╝╚██████╗██║  ██╗    ██║     ██║  ██║██║     ███████╗██║  ██║    ███████║╚██████╗██║███████║███████║╚██████╔╝██║  ██║███████║
╚═╝  ╚═╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝╚═╝╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
                                                                                                                                             \n\n"""

class game():
    def __init__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
            
    def refresh(self, text):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        print(f": {text-1} rounds left.")
    
    def start(self):
        print(logo)
        time.sleep(1)
        print("Choose your weapon\n" + (colored("[R]", 'yellow')) + " Rock\n" + (colored("[P]", 'green')) + " Paper\n" + (colored("[S]", 'red')) + " Scissors\n\n")
        while True:
            try:
                global rounds
                rounds = int(input("Rounds: "))
                break
            except ValueError:
                self.SlowType(colored("Please enter the number of rounds you need to play! Restarting the program...", 'red'), 0.02)
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                self.start()

        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        print(f"You will play {rounds} rounds.\n")

        Invalid_attempts = 0
        global attempts
        attempts = 0
        ties= 0
        limit = 10
        score = 0
        my_score = 0
        while Invalid_attempts <= limit:
            if attempts != rounds:
                letters = ['R', 'r', 'P', 'p', 'S', 's']
                input_ = input(">_ ")
                if input_ not in letters and Invalid_attempts < limit: 
                    print(colored(f"Invalid input! You have {limit - Invalid_attempts} attempts left.", 'red'))
                    time.sleep(.5)
                    self.clear(2)
                    Invalid_attempts += 1
                
                
                elif input_ in letters and Invalid_attempts < limit and attempts <= rounds:
                    user = input_
                    Clist = ['R', 'P', 'S']
                    Cchoose = random.choice(Clist)
                    if user.upper() == Cchoose:
                        self.refresh(rounds - attempts)
                        if user.upper == "R":
                            print(colored(rock_ + rock_, 'red'))
                        elif user.upper() == "S":
                            print(colored(scissor_ + scissor_, 'red'))
                        else:
                            print(colored(paper_ + paper_, 'red'))
                        print(f"\nTie! \n")
                        ties += 1
                        attempts += 1

                    elif user.upper() == 'R' and Cchoose == 'S':
                        self.refresh(rounds-attempts)
                        print(colored(rock_, 'green'))
                        print(colored(scissor_, 'red'))
                        print("\nRock beats Scissors\nYou won!\n")
                        score += 1
                        attempts += 1
    
                    elif user.upper() == 'P' and Cchoose == 'R':
                        self.refresh(rounds-attempts)
                        print(colored(paper_, 'green'))
                        print(colored(rock_, 'red'))
                        print("\nPaper beats Rock\nYou won!\n")
                        score += 1
                        attempts += 1

                    elif user.upper() == 'S' and Cchoose == 'P':
                        self.refresh(rounds-attempts)
                        print(colored(scissor_, 'green'))
                        print(colored(paper_, 'red'))
                        print("\nScissors beats Paper\nYou won!\n")
                        score += 1
                        attempts += 1
#--------------------------------------------------------------
                    else:
                        if Cchoose == "S":
                            self.refresh(rounds - attempts)
                            print(colored(paper_, 'red'))
                            print(colored(scissor_, 'green'))
                            
                        elif Cchoose == "R":
                            self.refresh(rounds - attempts)
                            print(colored(scissor_, 'red'))
                            print(colored(rock_, 'green'))
                            
                        else:
                            self.refresh(rounds - attempts)
                            print(colored(rock_, 'red'))
                            print(colored(paper_, 'green'))
                        print("\nI won!\n")
                        attempts += 1
                        my_score += 1

                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(colored('Invalid Invalid_attempts raise up!\n\n', 'red'))
                    print("Use only letters! " + (colored("[R] ", 'yellow')) + (colored("[P] ", 'green')) + (colored("[S]", 'red')))
                    time.sleep(5)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    self.start()
                    
            else:
                self.clear(20)
                self.SlowType("Round Over!\n", 0.07)
                print(f"|Rounds: {rounds}")
                print(f"|Ties: " + (colored(ties, 'red')))
                self.SlowType(f"\n|Your score: " + (colored(score, 'green')), 0.02)
                self.SlowType(f"|My score: " + (colored(my_score, 'yellow')), 0.02)
                input('\n\nPress Enter\n')
                os.system('cls' if os.name == 'nt' else 'clear')
                time.sleep(.5)
                self.start()
                

    def SlowType(self, text:str, speed:float, newline=True):
        for i in text:
            print(i, end='', flush=True)
            time.sleep(speed)
        if newline:
            print()

    def clear(self, lines):
        print("\033[A                                                  \033[A")
        if lines:
            print(f"\n\033[A                                                  \033[A" * lines)



if __name__ == '__main__':
    main = game()
    main.start()

