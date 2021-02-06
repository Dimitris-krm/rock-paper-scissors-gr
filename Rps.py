import random


def play():
    user = input("A)Πέτρα Β)Ψαλίδι Γ)Χαρτί :")
    computer = random.choice(["Α", "Β", "Γ "])

    if user == computer:
        print("Ισοπαλία")
        print("Ο αντιπαλός σου έπαιξε " + computer)
    elif win(user, computer):
        print("Νίκησες")
        print("Ο αντιπαλός σου έπαιξε " + computer)
    else:
        print("\nΈχασες")
        print("Ο αντιπαλός σου έπαιξε " + computer)


def win(player, pc):
    if (player == "Α" and pc == "Β") or (player == "Β" and pc == "Γ") or (player == "Γ" and pc == "Α"):
       return True

play()
