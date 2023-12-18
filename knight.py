from chromosome import Chromosome

class Knight:
    def __init__(self, chromosome=None):
        self.position = (0, 0)  
        self.path = [self.position]
        self.fitness = 0
        if chromosome is None:
            self.chromosome = Chromosome()
        else:
            self.chromosome = chromosome

    def move_forward(self, direction):
        moves = {
            1: lambda pos: (pos[0] - 1, pos[1] + 2),
            2: lambda pos: (pos[0] + 1, pos[1] + 2),
            3: lambda pos: (pos[0] + 2, pos[1] + 1),
            4: lambda pos: (pos[0] + 2, pos[1] - 1),
            5: lambda pos: (pos[0] + 1, pos[1] - 2),
            6: lambda pos: (pos[0] - 1, pos[1] - 2),
            7: lambda pos: (pos[0] - 2, pos[1] - 1),
            8: lambda pos: (pos[0] - 2, pos[1] + 1),
        }
        new_pos = moves[direction](self.position)
        self.position = new_pos
        self.path.append(new_pos)

    def move_backward(self, direction):
        self.path.pop()

    def check_moves(self):
        visited_positions = set()
        current_number = 1
        self.path = []

        def valid_moves(pos):
            moves = [
                (pos[0] + dx, pos[1] + dy)
                for dx, dy in [
                    (-2, -1),
                    (-1, -2),
                    (1, -2),
                    (2, -1),
                    (2, 1),
                    (1, 2),
                    (-1, 2),
                    (-2, 1),
                ]
            ]
            return [
                move
                for move in moves
                if 0 <= move[0] < 8
                and 0 <= move[1] < 8
                and move not in visited_positions
            ]

        def sort_moves(pos):
            moves = valid_moves(pos)
            return sorted(moves, key=lambda move: len(valid_moves(move)))

        pos = (0, 0)
        self.path.append((pos, current_number))
        visited_positions.add(pos)

        while len(visited_positions) < 64:
            next_moves = sort_moves(pos)
            if not next_moves:
                break

            pos = next_moves[0]
            visited_positions.add(pos)
            current_number += 1
            self.path.append((pos, current_number))

    def evaluate_fitness(self):
        self.check_moves()
        unique_positions = set(self.path)

        if (
            len(unique_positions) == 64
        ):  
            self.fitness = 64  
        else:
            self.fitness = len(unique_positions)