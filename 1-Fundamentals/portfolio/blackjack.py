import random

# Globals

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

suits = ('♣️Clubs♣️', '♠️Spades♠️', '♦️Diamonds♦️', '♥️Hearts♥️')

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


# Classes


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_count = ''
        for card in self.deck:
            deck_count += "\n" + card.__str__()
        return "The deck has:" + deck_count

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def ace_adjustment(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Tally:
    def __init__(self):
        self.player_win = 0
        self.comp_win = 0
        self.ties = 0
        self.game = 0

    def win_game(self):
        self.player_win += 1
        print("The tally is now: ", "\nPlayer Wins: ", self.player_win,
              "\nDealer Wins: ", self.comp_win, "\nTie Games: ", self.ties)

    def lose_game(self):
        self.comp_win += 1
        print("The tally is now: ", "\nPlayer Wins: ", self.player_win,
              "\nDealer Wins: ", self.comp_win, "\nTie Games: ", self.ties)

    def tie_game(self):
        self.ties += 1
        print("The tally is now: ", "\nPlayer Wins: ", self.player_win,
              "\nDealer Wins: ", self.comp_win, "\nTie Games: ", self.ties)


# Options


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.ace_adjustment()


def hit_or_stand(deck, hand):
    global playing

    while True:
        choice = input(
            '\nHit or Stand? (Enter "Hit" / "H" or "Stand" / "S"): ')
        if choice == 'Hit' or choice == 'H':
            hit(deck, hand)
        elif choice == 'Stand' or choice == 'S':
            print("You stand. Dealer's turn: ")
            playing = False
        else:
            print("Incorrect input. Please enter 'Hit' / 'H' or 'Stand' / 'S: ")
            continue
        break


# Turns

def initial_deal(dealer, player):
    print("Dealer's Hand:")
    print("---Hidden Card---")
    print(dealer.cards[1])
    print("\nYour Hand:", *player.cards, sep="\n")


def every_turn_after(dealer, player):
    print("\nDealer's Hand:", *dealer.cards, sep="\n")
    print("\nDealer's Hand:", dealer.value)
    print("\nYour Hand:", *player.cards, sep="\n")
    print("\nYour Hand:", player.value)


# Endgame


def player_wins(player, dealer, tally):
    print("\nYou win!\n")
    tally.win_game()


def player_loses(player, dealer, tally):
    print("\nYou lose!\n")
    tally.lose_game()


def dealer_wins(player, dealer, tally):
    print("\nThe dealer wins!\n")
    tally.lose_game()


def dealer_loses(player, dealer, tally):
    print("\nThe dealer loses!\n")
    tally.win_game()


def tie(player, dealer, tally):
    print("\nIt's a tie!\n")
    tally.tie_game()


# Playing the Game

while True:
    print("\nLet's play Blackjack!\n")

    deck = Deck()
    deck.shuffle()

    tally = Tally()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    initial_deal(dealer_hand, player_hand)

    while playing:
        hit_or_stand(deck, player_hand)

        every_turn_after(dealer_hand, player_hand)

        if player_hand.value > 21:
            player_loses(player_hand, dealer_hand, tally)
            break

    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            print("\nDealer hits again...\n")
            hit(deck, dealer_hand)

        every_turn_after(dealer_hand, player_hand)

        if dealer_hand.value > 21:
            dealer_loses(player_hand, dealer_hand, tally)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, tally)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, tally)
        else:
            tie(player_hand, dealer_hand, tally)

    new_game = input("\nPlay again? (Enter 'Yes' / 'Y' or 'No' / 'N'): ")

    if new_game == "Yes" or new_game[0] == "Y":
        playing = True
        continue
    elif tally.player_win == 3:
        print("\nYou have beat the dealer 3 times!")
        break
    else:
        print("\nHope you had fun, thanks for playing!")
        break
