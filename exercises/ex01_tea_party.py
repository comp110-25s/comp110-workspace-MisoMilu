"""Cozy tea party - everyone is welcomed!!"""

__author__: str = "730564205"


def main_planner(guests: int) -> None:
    """4. Bringing these function together in a “main planner” function"""
    print(f"A cozy party for {guests} people!")
    print(f"Tea bags: {tea_bags(guests)}")
    print(f"Treats: {treats(guests)}")
    print(f"Cost: ${cost(tea_bags(guests), treats(guests))}")


def tea_bags(people: int) -> int:
    """1.Compute the number of tea bags needed based on number of guests"""
    return people * 2


def treats(people: int) -> int:
    """2.Compute the number of treats needed based on the number of teas guests"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """3. A function to compute the cost of the tea bags and the treats combined"""
    return tea_count*0.50 + treat_count*0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))