import random


print("Enter the number of friends joining (including you):")
number = int(input())


def read_people(count: int) -> list:
    people = []
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(count):
        people.append(input())
    print()
    return people


def get_lucky_person(people: list) -> str:
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    apply_lucky = input()
    person = None
    if apply_lucky == "Yes":
        person = random.choice(people)
        print(f"{person} is the lucky one!")
    else:
        print("No one is going to be lucky")
    print()
    return person


def get_total() -> int:
    print("Enter the total bill value:")
    total = int(input())
    print()
    return total


if number > 0:
    friends = read_people(number)
    ticket = get_total()
    lucky = get_lucky_person(friends)

    if lucky:
        index = friends.index(lucky)
        friends.pop(index)

    amount = round(ticket / len(friends), 2)
    bill = dict.fromkeys(friends, amount)
    if lucky:
        bill[lucky] = 0

    print(bill)
else:
    print("No one is joining for the party")

