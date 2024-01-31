'''We are going to develop and test a card game based on the module cards available here at GitHub. Study it as you will use the code in cards.play() as a starting point for your own code.

First, write an auxiliary Python function card_value(card) that, given a card, returns its value. The values of the cards correspond to their numerical value from 2-10, all face cards (Jack, Queen, King) count 10 and the Ace counts 11. If the card colour is black (i.e. from clubs or spades suit) its value is doubled.

Then write a new Python function play(seed_value) that returns a string with the winners of the game sorted and separated with a space (for example, "P1 P4"). The winners of each turn, the ones with the most valuable cards, earn one point each, and the final winners are the ones with the maximum number of points. The seed method (from the random module) must be used to initialize the pseudo-random number generator using random.seed(seed_value).

As in the original play() function from the module cards, the game goes as follows:

1. We deal a hand of 13 cards to each player.
2. Then a start player is chosen and the players take turns playing their cards.
3. The players will randomly play one card at each turn until their hands are empty.
4. The turn winner, or winners in case there's a draw, are the ones with the most valuable card.
5. The game winner, or winners in case there's a draw, are computed in the end.
'''
from cards import create_deck, deal_hands, choose, player_order
import random

def play(seed_value) -> None:
    random.seed(seed_value)
    deck = create_deck(shuffle=True)
    names = "P1 P2 P3 P4".split()
    hands = {n: h for n, h in zip(names, deal_hands(deck))}
    start_player = choose(names)
    turn_order = player_order(names, start=start_player)
    wins = [0, 0, 0, 0]
    while hands[start_player]:
        lista = []
        for name in turn_order:
            card = choose(hands[name])
            lista.append(card_value(card))
            hands[name].remove(card)
        max1 = max(lista)
        for i in range(len(lista)):
            if lista[i] == max1:
                wins[i] += 1
    max2 = max(wins)
    res = ""
    if wins[turn_order.index("P1")] == max2:
        res += "P1 "
    if wins[turn_order.index("P2")] == max2:
        res += "P2 "
    if wins[turn_order.index("P3")] == max2:
        res += "P3 "
    if wins[turn_order.index("P4")] == max2:
        res += "P4 "
    return res[:-1]


def card_value(card):
    val = 0
    if card[1].isdigit():
        val += int(card[1])
    elif card[1] == "A":
        val += 11
    else:
        val += 10
    if card[0] == "♠" or card[0] == "♣":
        val *= 2
    return val
