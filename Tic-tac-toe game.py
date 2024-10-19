class Solution():
    def tictactoe(self, moves):
         # Set of all possible winning combinations
        wins = [
        {(0, 0), (0, 1), (0, 2)},
        {(1, 0), (1, 1), (1, 2)},
        {(2, 0), (2, 1), (2, 2)},
        {(0, 0), (1, 0), (2, 0)},
        {(0, 1), (1, 1), (2, 1)},
        {(0, 2), (1, 2), (2, 2)},
        {(0, 0), (1, 1), (2, 2)},
        {(0, 2), (1, 1), (2, 0)},
    ]
        X_moves = []
        O_moves = []
        # Split the moves between X and O
        for i in range(len(moves)):
            if i % 2:  # If index is odd, it's O's turn
                O_moves.append(moves[i])
            else:  # If index is even, it's X's turn
                X_moves.append(moves[i])

        # Convert lists to sets for easy comparison
        X_moves = set(tuple(move) for move in X_moves)
        O_moves = set(tuple(move) for move in O_moves)

        # Check if X or O has any winning set
        for win_set in wins:
            if win_set <= X_moves:  # Check if X has a winning combination
                return "A"
            if win_set <= O_moves:  # Check if O has a winning combination
                return "B"

        # Check if the game is a draw or still pending
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"