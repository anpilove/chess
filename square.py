class Square:

    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece
        self.coord = None
        self.true_coords = None


    def has_piece(self):
        return self.piece is not None
