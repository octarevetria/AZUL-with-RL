NUM_PLAYERS = 2
PIECES = ['yellow', 'red', 'skyblue', 'blue', 'black', 'first_player']
SCOREBOARD_MASK = [(4, 1, 2, 5, 3), (3, 4, 1, 2, 5), (5, 3, 4, 1, 2), (2, 5, 3, 4, 1), (1, 2, 5, 3, 4)]
PLAYERS_BOARD_ROWS = NUM_PLAYERS * 6
PLAYERS_BOARD_COLS = len(PIECES)
PLAYERS_BOARD_HEIGHT = 6
DRAFT_BOARD_ROWS = NUM_PLAYERS * 2 + 2
DRAFT_BOARD_COLS = len(PIECES)