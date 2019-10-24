import random
import math
from typing import List, Dict, Tuple


class Ship:
    def __init__(self, size: int) -> None:
        self.hits: int = 0
        self.size: int = size

    def hit(self) -> None:
        self.hits += 1

    def is_sunk(self) -> bool:
        return self.hits == self.size


class Player:
    def __init__(self, name: str = None) -> None:
        self.board: Dict[Tuple[int, int], Ship] = {}
        self.hits: List[Tuple[int, int]] = []
        self.misses: List[Tuple[int, int]] = []
        self.sunk_ships: int = 0
        self.name: str = name

    def init_board(self, ship_pos: Dict) -> None:
        self.board.update(ship_pos)

    def sunk_ship(self) -> None:
        self.sunk_ships += 1


class Game:
    def __init__(self, size: int = 10, num_of_ships: int = 1) -> None:
        self.p1_turn: bool = True
        self.p1: Player = Player("Player 1")
        self.p2: Player = Player("Player 2")
        self.board_size: int = size
        self.num_of_ships: int = num_of_ships
        self.ship_sizes: List[int] = [
            random.randint(2, 5) for i in range(self.num_of_ships)
        ]

    def get_player(self) -> Player:
        return self.p1 if self.p1_turn else self.p2

    def get_opponent(self) -> Player:
        return self.p2 if self.p1_turn else self.p1

    def shoot(self, pos: Tuple[int, int]) -> None:
        player: Player = self.get_player()
        opponent: Player = self.get_opponent()
        if pos not in player.hits + player.misses:
            ship: Ship = opponent.board.get(pos)
            if ship is not None:
                ship.hit()
                player.hits.append(pos)
                print("Hit!")
                if ship.is_sunk():
                    opponent.sunk_ship()
                    print("Ship has been sunk!")
            else:
                player.misses.append(pos)
                print("Miss :(")
        else:
            print("You already shot there dummy")

    def win(self) -> bool:
        opponent: Player = self.get_opponent()
        return opponent.sunk_ships == self.num_of_ships

    def switch_turn(self) -> None:
        self.p1_turn = not self.p1_turn

    def place_ships(self) -> None:
        player: Player = self.get_player()
        for ship_size in self.ship_sizes:
            ship: Ship = Ship(ship_size)
            coords: List[Tuple[int, int]] = []

            while not self.validate_coords(coords, ship_size):
                try:
                    coords = eval(
                        input(
                            f"{player.name} please provide {ship_size} coordinates for ship"
                        )
                    )
                except Exception:
                    coords = []

            board: Dict[Tuple[int, int] : Ship] = {pos: ship for pos in coords}
            player.init_board(board)

    def validate_coords(self, coords: List[Tuple[int, int]], ship_size: int) -> bool:
        if not coords:
            return False

        if len(coords) != ship_size:
            print(f"Please input {ship_size} coordinates")
            return False

        if len(set(coords)) != ship_size:
            print("Please do not include duplicate coordinates")
            return False

        board: Dict[Tuple[int, int], Ship] = self.get_player().board
        if any(coord in board.keys() for coord in coords):
            print("A coordinate is already occupied by another ship")
            return False

        coords = sorted(coords)
        x1: int = coords[0][0]
        x2: int = coords[-1][0]
        y1: int = coords[0][1]
        y2: int = coords[-1][1]

        if x2 >= self.board_size or y2 >= self.board_size:
            print(
                f"Please ensure all coordinates are within the {self.board_size} x {self.board_size} board"
            )
            return False

        if math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) + 1 != ship_size:
            print("Please ensure all coordinates for ship are adjacent")
            return False

        return True


def main() -> None:
    print("Welcome to Battleship!")
    size: int = 0
    while size < 10:
        try:
            size = eval(
                input(
                    "Choose the size of your board. Please choose an integer greater or equal to 10: "
                )
            )
        except Exception:
            size = 0

    num_of_ships: int = 0
    while num_of_ships < 1:
        try:
            num_of_ships = eval(
                input(
                    "How many ships would you like to place? Please choose an integer greater or equal to 1: "
                )
            )
        except Exception:
            num_of_ships = 0

    game: Game = Game(size, num_of_ships)

    game.place_ships()

    game.switch_turn()

    game.place_ships()

    while True:
        game.switch_turn()
        player: Player = game.get_player()
        print(f"\n{player.name} please shoot")
        print(f"Hits: {player.hits}")
        print(f"Misses: {player.misses}")
        xpos: int = eval(input("X Coordinate: "))
        ypos: int = eval(input("Y Coordinate: "))
        game.shoot((xpos, ypos))
        if game.win():
            print(f"Congrats {player.name} you win!")
            break


if __name__ == "__main__":
    main()
