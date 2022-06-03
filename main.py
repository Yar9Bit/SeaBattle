class BoardException(Exception):
    pass


class BoardOutException(BoardException):
    pass


class BoardUsedException(BoardException):
    pass


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Dot({self.x}, {self.y})"


class Ship:
    def __init__(self, bow, large, position):
        self.bow = bow
        self.large = large
        self.position = position
        self.lives = 1

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.large):
            current_x = self.bow.x
            current_y = self.bow.y

            if self.position == 0:
                current_x += 1
            elif self.position == 1:
                current_y += 1

            ship_dots.append(Dot(current_x, current_y))

        return ship_dots

    def shoot_ship(self, shot):
        return shot in self.dots


class Board:
    def __init__(self, hid=False, size=6):
        self.size = size
        self.HID = hid
        self.count = 0
        self.field = [["0"] * size for _ in range(size)]
        self.busy = []
        self.ships = []

    def __str__(self):
        result = ""
        result += "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, row in enumerate(self.field):
            result += f"\n{i + 1} | " + " | ".join(row) + " |"

        if self.HID:
            result = result.replace("█", "0")
        return result

    def dot_out(self, dot):
        return not ((0 <= dot.x < self.size) and (0 <= dot.y < self.size))
