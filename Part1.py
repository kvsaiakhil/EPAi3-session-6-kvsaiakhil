import random

#################################################################################################################################
# 1. Write a single expression that includes lambda, zip, and map functions to select create 52 cards in a deck
#################################################################################################################################

vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', "jack", "queen", "king", "ace"]
suits = ["hearts", "clubs", "diamonds", "spades"]

cards = list(map(lambda suits_lst, vals_lst: list(zip(vals_lst*len(suits_lst), sorted(suits_lst*len(vals_lst)))), [suits], [vals]))

#################################################################################################################################
# 2. Write a normal function without using lambda, zip, and map function to create 52 cards in a deck
#################################################################################################################################

def create_deck(suits_lst: list, vals_lst: list) -> "list of tuples":
    ''' creates a deck of cards from given list of suits and values 
        
        Returns a deck of cards    
    '''
    cards = []
    for suit in sorted(suits_lst):
        for val in vals_lst:
            cards.append((val, suit))
    return cards

#################################################################################################################################
# 3. Write a function that, when given 2 sets of 3 or 4 or 5 cards 
#   (1 game can only have 3 cards with each player or 4 cards or 5 cards per player) 
#   (1 deck of cards only), 
#   (2 players only), 
#   can identify who won the game of poker!
#################################################################################################################################


rank = {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "10": 9, "jack": 10, "queen": 11, "king": 12, "ace": 13}

def get_hand_rank(hand: "list of tuples") -> "(rank, hand type)":
    ''' computes the rank of a hand of cards
    
        Returns the rank and type of the hand
    '''

    hand = sorted(hand, key = lambda card: rank[card[0]])
    vals, suits =  list(zip(*hand))
    suit_types = list(set(suits))
    val_types = list(set(vals))

    is_same_suit =  len(suit_types) == 1

    is_val_royal = {"jack", "queen", "king", "ace"} == set(suits)

    is_val_in_seq = len(set(list(map(lambda a, b: rank[a]+rank[b], vals, vals[::-1])))) == 1 and rank[vals[0]] + 1 == rank[vals[1]]

    is_four_of_a_kind =  len(val_types) == 2 and (vals.count(val_types[0]) == 4 or vals.count(val_types[1] == 4))

    is_full_house =  len(val_types) == 2

    is_flush =  is_same_suit

    is_straight = is_val_in_seq

    is_three_of_a_kind =  len(val_types) == 3 and (vals.count(val_types[0]) == 3 or vals.count(val_types[1]) == 3 or vals.count(val_types[2]) == 3)

    is_two_pair =  len(val_types) == 3

    is_one_pair =  len(val_types) == 4

    is_high_card = len(val_types) == 5

    if is_same_suit and is_val_royal:
        return 1, "ROYAL FLUSH"
    elif is_same_suit and is_val_in_seq:
        return 2, "STRAIGHT FLUSH"
    elif is_four_of_a_kind:
        return 3, "FOUR OF A KIND"
    elif is_full_house:
        return 4, "FULL HOUSE"
    elif is_flush:
        return 5, "FLUSH"
    elif is_straight:
        return 6, "STRAIGHT"
    elif is_three_of_a_kind:
        return 7, "THREE OF A KIND"
    elif is_two_pair:
        return 8, "TWO PAIR"
    elif is_one_pair:
        return 9, "ONE PAIR"
    elif is_high_card:
        return 10, "HIGH CARD"


def print_cards(player_name: str, player_hand_type: "hand type",  cards: "list of tuples") -> None:
    ''' prints hand of cards'''

    vdict = {"2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9", "10": "10", "jack": "J", "queen": "Q", "king": "K", "ace": "A"}

    symbol_dict = {"clubs": "♣", "diamonds":"♦", "hearts":"♥", "spades":"♠"}

    print("PLAYER: " + player_name + " - " + player_hand_type)
    print(cards)
    print("+---------+  +---------+  +---------+  +---------+  +---------+")
    print(f"| {vdict[cards[0][0]]: <2}      |  | {vdict[cards[1][0]]: <2}      |  | {vdict[cards[2][0]]: <2}      |  | {vdict[cards[3][0]]: <2}      |  | {vdict[cards[4][0]]: <2}      |")
    print(f"| {symbol_dict[cards[0][1]]}       |  | {symbol_dict[cards[1][1]]}       |  | {symbol_dict[cards[2][1]]}       |  | {symbol_dict[cards[3][1]]}       |  | {symbol_dict[cards[4][1]]}       |")
    print("|         |  |         |  |         |  |         |  |         |")
    print(f"|       {symbol_dict[cards[0][1]]} |  |       {symbol_dict[cards[1][1]]} |  |       {symbol_dict[cards[2][1]]} |  |       {symbol_dict[cards[3][1]]} |  |       {symbol_dict[cards[4][1]]} |")
    print(f"|      {vdict[cards[0][0]]: >2} |  |      {vdict[cards[1][0]]: >2} |  |      {vdict[cards[2][0]]: >2} |  |      {vdict[cards[3][0]]: >2} |  |      {vdict[cards[4][0]]: >2} |")
    print("+---------+  +---------+  +---------+  +---------+  +---------+")

def distribute_cards(cards: "list of tuples") -> "(player_1 hand, player_2 hand)":
    ''' function distributes equal no cards (3, 4 or 5) to each of the two players,
        the rest as community cards (total of 5 cards) from a deck of cards 
        
        Returns player_1 cards, player_2 cards and community cards
    '''
    random.shuffle(cards)
    player_1 = []
    player_2 = []
    community = []
    no_p_cards = random.choice([3,4,5]) 
    no_com_cards = 5 - no_p_cards

    def add_card(p_list):
        p_list.append(cards.pop(-1))

    for i in range(no_p_cards):
        add_card(player_1)
        add_card(player_2)

    for i in range(no_com_cards):
        add_card(community)

    return player_1, player_2, community

def poker_winner(player_1: "list of tuples", player_2: "list of tuples", community: "list of tuples") -> int:
    ''' function decides the winner of a poker game
        
        Returns:
            a. 1 if player ONE won
            b. 2 if player TWO won
            c. 0 if its a draw
    '''
    no_p_cards = len(player_1)
    no_c_cards = len(community)

    player_1.extend(community)
    player_2.extend(community)

    p1_rank, p1_hand = get_hand_rank(player_1)
    p2_rank, p2_hand = get_hand_rank(player_2)

    print("NO. OF PLAYER CARDS: " + str(no_p_cards) + " | " + "NO. OF COMMUNITY CARDS: " + str(no_c_cards) + "\n")

    print_cards("1", p1_hand, player_1)
    print_cards("2", p2_hand, player_2)
    
    print("===============================================================")
    if p2_rank > p1_rank:
        print("                         PLAYER 1 WON !!!")
        print("===============================================================")
        return 1
    elif p2_rank < p1_rank:
        print("                         PLAYER 2 WON !!!")
        print("===============================================================")
        return 2
    else:
        card_vals = lambda card: (rank[card[0]], card[1])

        p1_hand = sorted(map(card_vals, player_1), key = lambda card: card[0])
        p1_vals, p1_suits =  list(zip(*p1_hand))

        p2_hand = sorted(map(card_vals, player_2), key = lambda card: card[0])
        p2_vals, p2_suits =  list(zip(*p2_hand))
        
        p1_vals = list(p1_vals)
        p2_vals = list(p2_vals)

        for i in range(5):
            if max(p1_vals) > max(p2_vals):
                print("                         PLAYER 1 WON !!!")
                print("===============================================================")
                return 1
            elif max(p1_vals) < max(p2_vals):
                print("                         PLAYER 2 WON !!!")
                print("===============================================================")
                return 2
            else:
                maxv = max(p1_vals)
                p1_vals.remove(maxv)
                p2_vals.remove(maxv)
        if len(p1_vals) == 0:
            print("                          IT'S A DRAW")
            print("===============================================================")
            return 0
    