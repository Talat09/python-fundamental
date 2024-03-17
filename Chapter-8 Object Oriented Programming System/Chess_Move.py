def rook_moves(square):
    column = square[0]
    row = int(square[1])

    moves = []

    # Add all squares on the same row, ordered left-to-right, right-to-left
    for i in range(-7, 8):
        if i != 0:
            new_col = chr(ord(column) + i)
            if 'a' <= new_col <= 'h':
                moves.append((new_col + str(row), abs(i)))

    # Add all squares on the same column
    for r in '12345678':
        if r != str(row):
            moves.append((column + r, abs(int(r) - row)))

    # Sort moves prioritizing vertical proximity, then horizontal
    moves.sort(key=lambda x: (x[1] % row, x[1] // row))  # Prioritize vertical moves

    return [move[0] for move in moves]

t = int(input())

for _ in range(t):
    square = input().strip()
    moves = rook_moves(square)
    for move in moves:
        print(move)
