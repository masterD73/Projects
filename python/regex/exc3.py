# -------------------------
# title: State Machine
# -------------------------
# -------------------------
# Description: 
# -------------------------
# ------------------------
# Author: Daniel Merchav.
# Reviewer: Netta Savin.
# AI2 InfinityLabs.
# ------------------------
from random import randint
from enum import Enum


class States(Enum):
    ON = "0"
    OFF = "1"


class Stages(Enum):
    START = "start"
    TRANSITION = "transition"
    DEAD = "dead"
    END = "end"


def machine_state(numbers: str) -> bool:
    state = Stages.START.value
    table = {
        Stages.START.value: {States.ON.value: Stages.TRANSITION.value, States.OFF.value: Stages.DEAD.value},
        Stages.DEAD.value: {States.ON.value: Stages.DEAD.value, States.OFF.value: Stages.DEAD.value},
        Stages.TRANSITION.value: {States.ON.value: Stages.END.value, States.OFF.value: Stages.TRANSITION.value},
        Stages.END.value: {States.ON.value: Stages.END.value, States.OFF.value: Stages.TRANSITION.value}
    }
    if numbers[0] == States.OFF.value or numbers[-1] == States.OFF.value:
        return False
    for number in numbers:
        state = table[state][number]
    return state == list(table.keys())[-1]


def main():
    length = randint(1, 20)
    numbers = ""
    try:
        for i in range(length):
            numbers += str(randint(0, 1))
        if machine_state(numbers):
            print(f"Succeeded. string: {numbers}")
        else:
            print(f"Failed. string: {numbers}")
    except KeyError as e:
        print(f"Input number is wrong. {e} detected.")
    print("Tests done.")


if __name__ == '__main__':
    main()
