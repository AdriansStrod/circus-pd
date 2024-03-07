# Specifikācija
# - 1pt Spelētāji sāk no lauciņa nr. 1, vispār 100 lauciņu. Ir divi spēlētāji. Vinē tas kurš pirmais sasniedz pēdējo lauciņu
# - 1pt Maksimāli - 30 raundi, ja beidzas raundi - neizšķirts
# - 1pt Viens pēc otra met kauliņu (ar nejauša ciparu ģenerātora palidzību) un iet uz priekšu
# - 1pt Ja trāpa uz lauciņu ar kāpnem:
# -- zilas kāpnes ved uz leju, 16 -> 5, 65 -> 44 , 78 -> 67, 72 -> 61
# -- sarkanas kāpnes ved uz augšu, 13 -> 22, 37 -> 46, 31 -> 50, 85 -> 94 
# - 1pt Katrā raundā tik drukāta informācija kur atrodas spēlētājs, dators un vai ir uzkāpts uz kāpnem

# Koda vertēšanas kritēriji
# - 1pt Kodā izmanto mainīgus, ciklus (for vai while), zarošanu (if)
# - 1pt Kods strādā bez kļūdam
# - 1pt Mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā
# - 1pt Kodam ir jēdzīgi komentāri, pirms "if, for" koda konstrukcijam
# - 1pt Izmaiņas saglabātas versiju vadības sistēmā Git

# Dokumentācija
player_1 = 1
player_2 = 1
kubik = 0

#met_kauliņu
import random

for round in range (30):
    print("round", round + 1)
    kubik = random.randint(1, 6)
    print("player_1 met kauliņu", kubik)
    #parada_kura_lauciņa_ir_players
    player_1= player_1 + kubik
    print("player 1 iet uz",player_1)
    #ja_pirmais_player_uzkap_u_zilam_kapnem
    if player_1 == 16:
        print("player_1_go_on_the_blue_ledder")
        player_1 = 5
    elif player_1 == 65:
        print("player_1_go_on_the_blue_ledder")
        player_1 = 44
    elif player_1 == 78:
        print("player_1_go_on_the_blue_ledder")
        player_1 = 67
    elif player_1 == 72:
        print("player_1_go_on_the_blue_ledder")
        player_1 = 61

    #ja_pirmais_player_uzkap_uz_sarkanam_kapnem
    if player_1 == 13:
        print("player_1_go_on_the_red_ledder")
        player_1 = 22
    elif player_1 == 37:
        print("player_1_go_on_the_red_ledder")
        player_1 = 46
    elif player_1 == 31:
        print("player_1_go_on_the_red_ledder")
        player_1 = 50
    elif player_1 == 85:
        print("player_1_go_on_the_red_ledder")
        player_1 = 94


    kubik = random.randint(1, 6)
    print("2 met kauliņu", kubik)
    player_2 = player_2 + kubik
    print("player 2 iet uz",player_2)
    #ja_otrais_player_uzkap_uz_zilam_kapnem
    if player_2 == 16:
        print("player_2_go_on_the_blue_ledder")
        player_2 = 5
    elif player_2 == 65:
        print("player_2_go_on_the_blue_ledder")
        player_2 = 44
    elif player_2 == 78:
        print("player_2_go_on_the_blue_ledder")
        player_2 = 67
    elif player_2 == 72:
        print("player_2_go_on_the_blue_ledder")
        player_2 = 61

    #ja_otrais_player_uzkap_uz_sarkanam_kapnem
    if player_2 == 13:
        print("player_2_go_on_the_red_ledder")
        player_2 = 22
    elif player_2 == 37:
        print("player_2_go_on_the_red_ledder")
        player_2 = 46
    elif player_2 == 31:
        print("player_2_go_on_the_red_ledder")
        player_2 = 50
    elif player_2 == 85:
        print("player_2_go_on_the_red_ledder")
        player_2 = 94
    #pirmais player_uzvareja
    if player_1 >= 100:
        print("player_1 Win the game!!! ")
        break
    #otrais_player_uzvareja
    if player_2 >= 100:
        print("player_2 Win the game!!! ")
        break
     if round >= 30:
        print('Gamer over:tie')
    # ja pargaja 30 raundi tad nav uzvaretaja
    
    print("========")
    


# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Nejauša skaitļa generēšana - https://www.w3schools.com/python/ref_random_randint.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git
