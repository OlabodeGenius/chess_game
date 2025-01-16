# gui.py
import pygame
import chess
import os

# Piece values
piece_values = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 0,
}

# Constants
WIDTH, HEIGHT = 800, 800
SQUARE_SIZE = WIDTH // 8

# Colors
LIGHT_BROWN = (222, 184, 135)
DARK_BROWN = (139, 69, 19)

# Load piece images
def load_images():
    images = {}
    pieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
    colors = ['white', 'black']
    for color in colors:
        for piece in pieces:
            image_path = os.path.join('images', f'{color}_{piece}.png')
            image = pygame.image.load(image_path)
            # Resize the image to fit the square size
            image = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))
            images[f'{color}_{piece}'] = image
    return images

def draw_board(screen):
    for row in range(8):
        for col in range(8):
            color = LIGHT_BROWN if (row + col) % 2 == 0 else DARK_BROWN
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces(screen, board, images):
    for piece_type in chess.PIECE_TYPES:  # Use PIECE_TYPES instead of PIECE_NAMES
        for square in board.pieces(piece_type, chess.WHITE):
            x, y = chess.square_file(square), chess.square_rank(square)
            screen.blit(images[f'white_{chess.PIECE_NAMES[piece_type].lower()}'], (x * SQUARE_SIZE, (7 - y) * SQUARE_SIZE))

        for square in board.pieces(piece_type, chess.BLACK):
            x, y = chess.square_file(square), chess.square_rank(square)
            screen.blit(images[f'black_{chess.PIECE_NAMES[piece_type].lower()}'], (x * SQUARE_SIZE, (7 - y) * SQUARE_SIZE))

def get_ai_move(board):
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

def evaluate_board(board):
    score = 0
    for piece_type in piece_values:
        score += len(board.pieces(piece_type, chess.WHITE)) * piece_values[piece_type]
        score -= len(board.pieces(piece_type, chess.BLACK)) * piece_values[piece_type]
    return score

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess Game")
    clock = pygame.time.Clock()

    board = chess.Board()
    images = load_images()  # Load images

    running = True
    selected_square = None
    player_turn = True  # True for white's turn, False for black's turn

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and player_turn:
                mouse_x, mouse_y = event.pos
                col = mouse_x // SQUARE_SIZE
                row = mouse_y // SQUARE_SIZE
                square = chess.square(col, 7 - row)

                if selected_square is None:
                    # Select a square
                    if board.piece_at(square) is not None and board.piece_at(square).color == chess.WHITE:
                        selected_square = square
                else:
                    # Move the piece
                    move = chess.Move(selected_square, square)
                    if move in board.legal_moves:
                        board.push(move)
                        selected_square = None
                        player_turn = False  # Switch to AI turn

        # AI's turn
        if not player_turn:
            ai_move = get_ai_move(board)
            if ai_move:
                board.push(ai_move)
            player_turn = True  # Switch back to player's turn

        # Drawing the board and pieces
        draw_board(screen)
        draw_pieces(screen, board, images)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
