def insert_card(sorted_cards, new_card):
    for i in range(len(sorted_cards)):
        if new_card < sorted_cards[i]:
            sorted_cards.insert(i, new_card)
            return
    sorted_cards.append(new_card)

cards = [3, 5, 8, 12]
print(f"Before: {cards}")
while True:
    new = int(input("Enter a new card or type 0 to exit: "))
    if new == 0:
        break
    insert_card(cards, new)
    print(f"After inserting {new}: {cards}\n")