class Colors:
    RED_PREFIX = "\033[41m"
    BLUE_PREFIX = "\033[41m"
    GREEN_PREFIX = "\033[41m"
    YELLOW_PREFIX = "\033[41m"


class Card:
    def __init__(self, color, content, card_type) -> None:
        self.color = color
        self.content = content
        self.type = card_type


    def __str__(self) -> str:
        return f"\033[41m{self.content}\033[0m"



red_9 = Card("red", "9", "number")
print(red_9)


