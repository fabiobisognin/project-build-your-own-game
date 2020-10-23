#!/usr/bin/env python
# coding: utf-8

# DECK

# In[1]:


import random


# In[2]:


spade = "♠"
heart = "♥"
diamond = "♦"
club = "♣"

spade= { "A♠":11, "2♠":2, "3♠":3, "4♠":4, "5♠":5, "6♠":6, "7♠":7, "8♠":8, "9♠":9, "10♠":10, "J♠":10, "Q♠":10, "K♠":10}
heart= { "A♥":11, "2♥":2, "3♥":3, "4♥":4, "5♥":5, "6♥":6, "7♥":7, "8♥":8, "9♥":9, "10♥":10, "J♥":10, "Q♥":10, "K♥":10}
diamond= {"A♦":11, "2♦":2, "3♦":3, "4♦":4, "5♦":5, "6♦":6, "7♦":7, "8♦":8, "9♦":9, "10♦":10, "J♦":10, "Q♦":10, "K♦":10}
club= { "A♣":11, "2♣":2, "3♣":3, "4♣":4, "5♣":5, "6♣":6, "7♣":7, "8♣":8, "9♣":9, "10♣":10, "J♣":10, "Q♣":10, "K♣":10}


# In[3]:


player_hand = dict()
dealer_hand = dict()


# REPARTIR CARTAS

# In[4]:


deck = {k: v for d in (spade, heart, diamond, club) for k, v in d.items()}


# In[5]:


def give_card(n=1):
    hand = dict() 
    items = random.sample(deck.items(),k = n) #agarramos n cartas del deck
    
    for item in items:
        deck.pop(item[0]) #eliminamos el item del deck
        hand[item[0]] = item[1] #y lo agregamos a la mano
        
    return hand


# In[6]:


player_hand = give_card(2)

def show_hand(x):
    s_hand=list(x.keys())
    s_result=sum(x.values())
    
    return print(" ".join(s_hand), 'with', s_result, "points.")

show_hand(player_hand)


# In[8]:


def choose_winner (player_points, dealer_points):
    if  player_points > dealer_points:
        return print('Congratulations, you win!!!')
    elif player_points < dealer_points:
        return print('YOU LOSE')
    else: # player_points = dealer_points
        return print('DRAW')


# Funcion Sumar puntos de la mano

# In[9]:


def sum_points(card):
    return sum(card.values())


# GAME

# In[10]:


print("--21-BLACKJACK--\n")
while(True): #Game loop (while players wants to keep playing)
    #begin
    player_lose = False
    player_wins = False
    deck = {k: v for d in (spade, heart, diamond, club) for k, v in d.items()} #se crea el deck
    print("SHUFFLING AND DEALING CARDS...")
    player_hand = give_card(2)#se reparten dos cartas al jugador
    dealer_hand = give_card()#se reparte una carta al dealer
    dealer_points = sum_points(dealer_hand)# se inician los puntos de cada quien
    player_points = sum_points(player_hand)# // // //
    print("----STARTING HANDS----")
    print("Dealer hand:")
    show_hand(dealer_hand)
    print("Your hand:")
    show_hand(player_hand)
    print("----PLAYER TURN----")
    while(player_points <= 21): #HIT LOOP      
        if input("HIT OR STOP H/S: ").lower() == 'h':
            card_to_add = give_card()
            player_hand.update(card_to_add) #se actualiza la mano
            player_points += sum_points(card_to_add) #se actualizan los puntos
            print("Your hand:")
            show_hand(player_hand)
            if player_points > 21:
                player_lose = True
                break
        else:
            break
    #end HIT LOOP     
    if not player_lose:
        print('----DEALER TURN----')
        while(dealer_points < 17): #STOP LOOP
            card_to_add = give_card()
            dealer_hand.update(card_to_add)
            dealer_points += sum_points(card_to_add)
            print("Dealer hand:")
            show_hand(dealer_hand)
            if dealer_points > 21:
                player_wins = True
                break
        #end STOP LOOP
    #verificar quien gano

    if player_wins == True:
        print("YOU WIN!")
        print("Your hand:")
        show_hand(player_hand)
        print("vs\nDealer hand:")
        show_hand(dealer_hand)    
    elif player_lose == True:
        print("YOU LOSE")
        print("Your hand:")
        show_hand(player_hand)
        print("vs\nDealer hand:")
        show_hand(dealer_hand)    
    else:
        print("MOMENT OF TRUTH...")
        choose_winner(player_points, dealer_points)
        print("Your hand:")
        show_hand(player_hand)
        print("vs\nDealer hand:")
        show_hand(dealer_hand)  
    res = input("Want to play again? Y/N: \n").lower()
    if res != 'y':
        break

