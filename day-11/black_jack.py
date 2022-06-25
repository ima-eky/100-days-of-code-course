import  random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
from art import logo



def deal_card(cards):
    return random.choice(cards)


def calculate_score(cards_dealt):
    total = sum(cards_dealt)
    if len(cards_dealt) == 2 and (total == 21):
        return 0
    elif total > 21 and 11 in cards_dealt:
        cards_dealt.remove(11)
        cards_dealt.append(1)
    return total


def compare(first_score, second_score):
    if first_score == second_score:
        print(f'It is a draw')
    elif second_score == 0:
        print(f'Lose.Opponents wins with a blackjack.')
    elif first_score > 21:
        print(f'You went overboard.You lose!')
    elif first_score == 0:
        print(f'You win with a blackjack.')
    elif second_score > 21:
        print(f'Opponent went overboard.You win!')
    else:
        if first_score > second_score:
            print('You win.')
        else:
            print('You  lose.')


def play_game():
    print(logo)
    user_cards = [deal_card(cards), deal_card(cards)]
    computer_cards = [deal_card(cards), deal_card(cards)]
    should_deal = True
    while (should_deal):
        user_score = calculate_score(user_cards)
        print(f'Your cards:{user_cards},current score: {user_score}')

        computer_score = calculate_score(computer_cards)
        print(f'Computer\'s first card:{computer_cards[0]}')
        if user_score == 0 or computer_score == 0 or user_score > 21:
            should_deal = False
        else:
            user_choice = input(f"Type 'y' to get another card or 'n' to pass: ")
            if user_choice == 'y':
                user_cards.append(deal_card(cards))
                user_score = calculate_score(user_cards)
            else:
                should_deal = False

    computer_score = calculate_score(computer_cards)
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card(cards))
        computer_score = calculate_score(computer_cards)
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    compare(user_score, computer_score)


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
else:
    print(f'Goodbye')