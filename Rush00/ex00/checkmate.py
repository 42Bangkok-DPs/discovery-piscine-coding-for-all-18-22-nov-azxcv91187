def Attack_Sword(piece, position, king_pos, board):
    
    #ตรวจสอบการโจมตีของตัวหมากสามารถที่จะโจมตี King ได้หรือไม่
#1. กำหนดทิศทางการเคลื่อนที่ของตัวหมาก
    directions = {
        'P': [(-1, -1), (-1, 1)],
        'B': [(-1, -1), (-1, 1), (1, -1), (1, 1)],
        'R': [(0, -1), (0, 1), (-1, 0), (1, 0)],
        'Q': [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, -1), (0, 1), (-1, 0), (1, 0)]
    }
#2. ตรวจสอบว่าหมากที่ให้สามารถโจมตีได้หรือไม่
    if piece not in directions:
        return False
#3. เดินหมากตามทิศทางที่กำหนด
    for dr, dc in directions[piece]:
        r, c = position
        if piece == 'P': #4. กรณี Pawn (P) Pawn เดินไปแค่ 1 ช่องในแนวเฉียง (เฉพาะแนวโจมตี) ถ้า Pawn เดินไปตำแหน่งของ King ได้ คืนค่า True
            r += dr
            c += dc
            if (r, c) == king_pos:
                return True
            continue
#5. กรณีหมากอื่น (Bishop, Rook, Queen) ใช้ while loop เพื่อเดินในทิศทาง
        while 0 <= r < len(board) and 0 <= c < len(board[r]):
            r += dr
            c += dc
            if (r, c) == king_pos:
                return True
            if 0 <= r < len(board) and 0 <= c < len(board[r]) and board[r][c] != '.':
                break
#คืนค่า False หากไม่มีการโจมตี
    return False

def checkmate(board):
    #ตรวจสอบว่าจะมีตัวหมากใดที่สามารถเข้าโจมตี King ได้หรือไม่
    #1. หา King บนกระดานใช้ Nested loop วนดูทุกช่องบนกระดาน (board)ถ้าพบตำแหน่งของKing (K) เก็บในตัวแปร king_pos แล้วหยุดค้นหา
    king_pos = None
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == 'K':
                king_pos = (i, j)
                break
        if king_pos:
            break
#ถ้าไม่พบ King บนกระดาน คืนค่า "Fail"
    if not king_pos:
        return "Fail"
   #2. ตรวจสอบตัวหมากที่โจมตี King ได้ 
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell in "PBRQ":
                if Attack_Sword(cell, (i, j), king_pos, board):
                    return "Success"
#3. ถ้าไม่มีตัวหมากไหนโจมตี King ได้
    return "Fail"