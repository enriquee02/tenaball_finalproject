import random
# Select a random top 10 category for the game

def tenaball():
    """
    This game challenges the player to guess the top 10 footballers in a randomly selected category.
    The player has 3 lives to complete the list and must guess each player's full name correctly.
    The game includes a variety of predefined categories such as top goalscorers, most national caps, 
    and top signings. The game tracks correct guesses, provides feedback, and indicates when a player loses or wins.
    """
    #each category has been chosen one by one
    #barcelonas most expensive signings

    barcelona_signings = ["Philippe Coutinho", "Ousmane Dembele", "Antoine Griezmann", "Neymar Jr", "Frenkie de Jong", "Luis Suarez", "Zlatan Ibrahimovic", "Miralem Pjanic", "Raphinha", "Dani Olmo"]

    #most appearances with keeper David de Gea

    degea_app = ["Marcus Rashford", "Chris Smalling", "Anthony Martial", "Juan Mata", "Antonio Valencia", "Ashley Young", "Luke Shaw", "Wayne Rooney", "Phil Jones", "Victor Lindelof"]

    #most combined games for Real Madrid and Juventus

    juve_real = ["Cristiano Ronaldo", "Zinedine Zidane", "Gonzalo Higuain", "Alvaro Morata", "Sami Khedira", "Danilo", "Fabio Cannavaro", "Angel Di Maria", "Emerson", "Micheal Laudrup"]

    #most spanish national team appearances

    spain_app = ["Sergio Ramos", "Iker Casillas", "Sergio Busquets", "Xavi", "Andres Iniesta", "Andoni Zubizarreta", "David Silva", "Xabi Alonso", "Fernando Torres", "Cesc Fabregas"]

    #highest alltime goalscorers

    top_goals = ["Cristiano Ronaldo", "Lionel Messi", "Pele", "Romario", "Ferenc Puskas", "Josef Bican", "Robert Lewandowski", "Jimmy Jones", "Gerd Muller", "Joe Bambrick"]

    #most appearances with teammate Antony

    antony_app = ["Lisandro Martinez", "Bruno Fernandes", "Dusan Tadic", "Andre Onana", "Diogo Dalot", "Ryan Gravenberch", "Casemiro", "Davy Klaassen", "Daley Blind", "Edson Alvarez" ]

    #most used players by coach Carlo Ancelotti at Real Madrid

    ancelotti_used = ["Luka Modric", "Dani Carvajal", "Karim Benzema", "Federico Valverde", "Toni Kroos", "Vinicius Junior", "Thibaut Courtois", "Rodrygo", "Antonio Rudiger", "Nacho Fernandez"]

    #most used players by coach Luis Suarez at Fc Barcelona

    lEnrique_used = ["Lionel Messi", "Luis Suarez", "Neymar Jr", "Sergio Busquets", "Gerard Pique", "Javier Mascherano", "Ivan Rakitic", "Jordi Alba", "Andres Iniesta", "Ter Stegen"]

    #code to chose the tenaball that the player will face

    random_tenaball, category  = random.choice([
        (barcelona_signings, "most expensive barça signings"),
        (degea_app, "most appearances with teammate David de Gea"),
        (juve_real, "players with the most combined appearances for Juventus and Real Madrid"),
        (spain_app, "players with the most caps for the Spanish National Team"),
        (top_goals, "all time goalscorers"),
        (antony_app, "players with most appearances with teammate Antony"),
        (ancelotti_used, "most used players by coach Ancelotti at Real Madrid"),
        (lEnrique_used, "most used players by coach lEnrique at Fc Barcelona"),
    ])

    #so that we can track how many the player has guessed
    correct_answer = []
    lives = 3

    #Scoreboard object so the player can see each time what player he guessed right
    reveal_ans = ["?" for _ in random_tenaball]

    #starting the game
    print("Welcome to our Tenaball game mode")
    play = input("Do you want to play or exit?")
    if play == "exit":
        print("Bye!")
        return
    else:
        print(f"find the top 10 {category}")


        while lives > 0 and len(correct_answer) < 10:
            print(f"\nYou have {lives} lives left")

            print("tenaball tower:")
            for i, name in enumerate(reveal_ans, start = 1):
                print(f"{i}. {name}")

            player = input("Enter a player's full name: ")

        #check if guessed player is in the top 10
            if player in random_tenaball and player not in correct_answer:
                 #will show what position in the top 10 the player is in
                position = random_tenaball.index(player) + 1
                print(f"You guessed {player} correctly, he is number {position} on the list")
                 #will then add the correct player to the list
                reveal_ans[position-1] = player
                correct_answer.append(player)
                lives = 3

            elif player in correct_answer:
                print("You already guessed that player")
                #lives == lives

            else:
                print(f"{player} is not on the list")
                lives -= 1

        if len(correct_answer) == 10:
            print("\nYou beat the Tenaball")

        else:
            print("\nThe Tenaball beat you")
            print(f"The correct players were:")
            for position, player in enumerate(random_tenaball, start=1):
                print(f"{position}. {player}")

if __name__ == "__main__":
    tenaball()











