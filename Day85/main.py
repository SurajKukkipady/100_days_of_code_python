# The game board, 9 empty spaces
board = [" " for _ in range(9)]
current_player = "X"
winner = None
game_is_running = True

# --- Main Game Loop ---
while game_is_running:
    # 1. Print the board
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

    # 2. Get player input
    try:
        move = int(input(f"Player '{current_player}', enter your move (1-9): "))
        if 1 <= move <= 9 and board[move - 1] == " ":
            board[move - 1] = current_player
        else:
            print("Invalid move or spot already taken. Please try again.")
            continue
    except (ValueError, IndexError):
        print("Invalid input. Please enter a number from 1-9.")
        continue

    # 3. Check for a winner
    win_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == current_player:
            winner = current_player
            print(f"🎉 Player '{winner}' wins! 🎉")
            game_is_running = False
            break # Exit the for loop since a winner is found
    
    if not game_is_running:
        continue # Skip the rest of the loop if a winner was found

    # 4. Check for a draw
    if " " not in board:
        print("It's a draw! 🤝")
        game_is_running = False
        continue

    # 5. Switch the player
    current_player = "O" if current_player == "X" else "X"