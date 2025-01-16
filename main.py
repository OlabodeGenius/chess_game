# main.py
import chess
import random

# Piece values
piece_values = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 0,
}

def print_board(board):
    print(board)

def evaluate_board(board):
    """Evaluate the board and return a score."""
    score = 0
    for piece_type in piece_values:
        score += len(board.pieces(piece_type, chess.WHITE)) * piece_values[piece_type]
        score -= len(board.pieces(piece_type, chess.BLACK)) * piece_values[piece_type]
    return score

def get_ai_move(board):
    """Choose the best move for the AI based on piece values."""
    legal_moves = list(board.legal_moves)
    best_move = None
    best_score = float('-inf')

    for move in legal_moves:
        board.push(move)
        score = evaluate_board(board)
        board.pop()

        if score > best_score:
            best_score = score
            best_move = move

    return best_move

def main():
    # Create a new chess board
    board = chess.Board()

    while not board.is_game_over():
        print_board(board)

        # Check if it's white's turn
        if board.turn:  # True if it's white's turn
            move = input("Enter your move (e.g., e2e4): ")
            try:
                board.push_san(move)
            except ValueError:
                print("Invalid move. Please try again.")
        else:  # It's black's turn (AI)
            print("AI is making a move...")
            ai_move = get_ai_move(board)
            board.push(ai_move)
            print(f"AI played: {ai_move}")

    print("Game over!")
    print_board(board)

if __name__ == "__main__":
    main()
