
def error_m():
    print("The provided input is not a valid input, please use inputs of (Y or Yes) for Yes and (N or No) for No (Capitalization doesn't matter).")
def cont_ask():
    Y_or_N = input("Congradulations, you have reached an ending, would you like to restart and try again?: ").lower()
    if Y_or_N == "y" or Y_or_N == "yes":
        return(True)
    elif Y_or_N == "n" or Y_or_N == "no":
        return(False)
    else:
        error_m()
cont = True  
while cont:

    print("Welcome to the Day off boolean story game, please use inputs of (Y/Yes and N/No)\n")
    wakeup_alarm = input("You wake up from your alarm on your day off, it is 8:00am, Do you Go back to sleep?: ").lower()

    if wakeup_alarm == "y" or wakeup_alarm == "yes":
        print("You deicde to go back to sleep, this results in you waking up at 1pm")
        fastfood = input("Do you eat lunch out?:").lower()
        if fastfood == "y" or fastfood == "yes":
            print("You decide to get in your car and go get fast food, on the way there your car runs out of gas and you have to pull over.")
            helpcall = input("Do you call for help?: ").lower()
            if helpcall == "n" or helpcall == "no":
                print("You decide to not call for help and try to walk to a nearby gas station, along the way you walk into an active construction zone and trip into an open manhole")
                react = input("Do you stay calm in this situation?: ").lower()
                if react == "y" or react == "yes":
                    print("After barely avoiding falling into sewer water, you finnish getting gas and decide to just go home for the day (Ending 8)boring ending")
                    cont = cont_ask()
                elif react == "n" or react == "no":
                    print("As you panic, you fall into the sewers and while thinking this day couldnt get any worse, then you are suddenly approached by a group of turtles and a rat (Ending 9)Teenage mutant ninja turtles ending")
                    cont = cont_ask()
                else:
                    error_m()
            elif helpcall == "y" or helpcall == "yes":
                print("You decide to call for help, you call and a tow truck company picks up, they give you a time estimate of 1 hour")
                stayincar = input("Do you stay in your non air conditioned car?: ").lower()
                if stayincar == "y" or stayincar == "yes":
                    print("You decide to stay in your hot, non air conditioned car, this results in you passing out from the heat")
                    print("Afterwards you find yourself awake, back at the start of the day, like this never happened (Ending 6), groundhog day ending")
                    cont = cont_ask()
                elif stayincar == "n" or stayincar == "no":
                    print("You deicide to wait in an air conditioned gas station nearby while a tow truck arrives")
                    print("Once the tow truck arrives and takes you to a gas station, seeing the bill for the about 100 foot tow causes you to be vaporized, thanos snap style (Ending 7) No money ending")
                    cont = cont_ask()
                else:
                    error_m()
            else:
                error_m()
        elif fastfood == "n" or fastfood == "no":
            print("Instead of getting fast food you deicide to stay home and make lunch, you look in the fridge and find a premade meal")
            print("After sitting down on your couch to watch some tv it feels as if you are permanently attached to the couch, days later you wake up again and realize you are permanently attached to the couch, (Ending 10) Eternal couch")
        else:
            error_m()
    elif wakeup_alarm == "n" or wakeup_alarm == "no":
        print("You deicde that waking up now is the better idea and go to have breakfast")
        eggs = input("Do you have eggs with your breakfast?: ").lower()
        coffee = input("Coffee?: ").lower()
        toast = input("Toast?: ").lower()
        bricks = input("Concrete Bricks?: ").lower()
        if bricks == "y" or bricks == "yes":
            print("You attempt to eat Concrete Bricks, the table breaks and you fail to eat the bricks, this is pretty dumb(Ending 1 Reached)")
            cont = cont_ask()
        elif coffee == "y" or coffee == "yes":
            print("As you have your breakfast, you notice that your coffee tastes strange, then your mind slowly starts to speed up")
            hero = input("As you accidentally throw your coffe across the room with a slight flinch, you noticed you have developed super speed, do you decide to do good with these abilities?: ").lower()
            if hero == "y" or hero == "yes":
                print("Using your newfound abilities you immidiantly run out of your house and search desperately for any nearby criminal activity, which is a person speeding 3 mph over the speed limit...")
                Care = input("Do you actually care enough to try and apprehend someone for something they wouldnt even be pulled over for?: ").lower()
                if Care == "y" or Care == "yes":
                    print("Against common sense, you decide to pull the person out of their car and onto the sidewalk, causing the car to drift forward with no driver and hit a lamp pole.")
                    print("Then before questioning them or letting them speak, you take them to the nearest maximum security prison")
                    print("The gaurds at the maximum security prison see a superpowered man holding an innocent person and assume this to be a hostage situation")
                    print("A sniper opens fire on you and you arent skilled enough with your super speed to avoid it(Ending 2)")
                    cont = cont_ask()
                elif Care == "n" or Care == "no":
                    print("Instead of annoying someone for something nobody cares about, you pull out your phone and look for major crime reports and find a bank robery reported nearby")
                    print("You arrive at the bank and find a large scene almost like a movie with police all around the area")
                    charge = input("Do you charge into the bank blindly?: ").lower()
                    if charge == "y" or charge == "yes":
                        print("You decide to charge into the surrounded biulding and try to tie up the robbers")
                        print("As you apprehend the robbers you notice your super speed begin to wear off, the last of the remaining robbers are then able to free the apprehended ones and capture you, they then put a mask on you and frame you as a robber, leading to your arrest(Ending 3) ")
                        cont = cont_ask()
                    elif charge == "n" or charge == "no":
                        print("Instead of chargin in blindly you consult an officer who doesnt belive your super speed untill you show him, you are then able to colaberate with the police to bring out the robbers one by one with minimal damage, you are treated as a local hero(Ending 4)")
                        cont = cont_ask()
                    else:
                        error_m()
                else:
                    error_m()
            elif hero == "n" or hero == "no":
                print("You decide against doing good with these powers and instead to use them for greed.")
                print("You look on your phone and find a nearby bank robery and decide to join in")
                print("You arrive at the scene and as you are bringing the money to your house you feel your powers running out")
                print("The police aswell as the now angry robbers both fight for a moment before turning on and capturing you (Ending 5)")
                cont_ask()
            else:
                error_m()
        elif eggs == "y" or eggs == "yes" or toast == "y" or toast == "yes":
            print("You enjoy your fairly normal breakfast, you then notice the mailman arriving outside")
            print("Upon going outside to meet the mailman, you see a file from the government telling you that you forgot to pay your taxes and are going to be arrested for tax evasion.")
            tax_evade = input("Do you try to go pay them off anyway to hopefully not get arrested?: ").lower()
            if tax_evade == "yes" or tax_evade == "y":
                print("You drive to the nearest government biudling and turn in the amound of money you think you owed for taxes")
                print("Through a stroke of luck they somehow accept the payment and tell you that they will call off the criminal charges")
                print("But because the gonvernment is slow, on the way home you are pulled over and arrested for tax evasion(Ending 11)")
                cont = cont_ask()
            elif tax_evade == "no" or tax_evade == "n":
                print("Against common sense, you dont try to pay your taxes in time and have now pissed off the government")
                print("I dont know what you expected but about an hour later a group of police officers appear at your front door")
                print("(Ending 12) bad ending")
                cont = cont_ask()
            else:
                error_m()
        elif (eggs == "n" or eggs == "no") and (coffee == "n" or coffee == "no") and (toast == "no" or toast == "n") and (bricks == "n" or bricks == "no"):
            print("You oddly decide to skip breakfast, this leaves you tired for the rest of the day.")
            back_to_sleep = input("You sort of feel like just going to bed, do you?: ").lower()
            if back_to_sleep == "yes" or back_to_sleep == "y":
                print("You go back to bed, I dont know what you expected")
                print("Like literally why would you do this, nothing else happens\n There is no reason at all for anything else to happen")
                print(".\n.\n.\n.")
                print("Okay fine something can happen")
                print("You.. uhh, fall out of bed and wake up in Jurassic park I guess")
                print("Cool")
                print("Bye(Ending 13)")
                cont = cont_ask()
            elif back_to_sleep == "no" or back_to_sleep == "n":
                print("Despite being incredibly tired and not having eaten anything you decide to go on with your day")
                print("Suddenly you get a call from your boss, informing you that this was not infact a day off")
                print("You have been fired (True ending)")
                cont = cont_ask()
            else:
                error_m()
        else:
            error_m()
    else:
        error_m()