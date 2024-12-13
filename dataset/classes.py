ENCODING_MAP = {
    "-": (0, 0),  # Sky
    "o": (0, 100),  # Coin
    "X": (1, 100),  # Ground
    "S": (0, 115),  # Brick
    "C": (0, 130),  # Coin Brick Block
    "U": (0, 145),  # Mushroom Brick Block
    "?": (0, 160),  # Special Question Block
    "!": (0, 175),  # Question Block
    "1": (0, 190),  # Invisible 1 up block
    "2": (0, 205),  # Invisible coin block
    "g": (2, 100), # Goomba (Removed E)
    "G": (2, 115), # Winged Goomba
    "k": (2, 130), # Green Koopa
    "K": (2, 145), # Winged Green Koopa
    "r": (2, 160), # Red Koopa
    "R": (2, 175), # Winged Red Koopa
    "y": (2, 190), # Spiky
    "B": (2, 205), # Bullet Billington head
    "b": (2, 220), # Bullet Billington body
    "<": (3, 100), # Top left pipe
    ">": (3, 115), # Top right pipe
    "(": (3, 130), # Top left pipe with plant
    ")": (3, 145), # Top right pipe with plant
    "[": (3, 175), # Left pipe
    "]": (3, 190), # Right pipe
    "#": (0, 220), # Hard Block
    "L": (1, 150), # 1 Up Block
    "E": (2, 220), # Enemys
}

class BidirectionalMap:
    def __init__(self, mapping):
        self.key_to_value = mapping
        self.value_to_key = {v: k for k, v in mapping.items()}

    def get_value(self, key):
        return self.key_to_value.get(key)

    def get_key(self, value):
        return self.value_to_key.get(value)

# Create the bidirectional map object
mapping = {
    '-': (0, 0), 'o': (0, 100), 'X': (1, 100), 'S': (0, 115),
    'C': (0, 130), 'U': (0, 145), '?': (0, 160), '!': (0, 175),
    '1': (0, 190), '2': (0, 205), 'g': (2, 100), 'G': (2, 115),
    'k': (2, 130), 'K': (2, 145), 'r': (2, 160), 'R': (2, 175),
    'y': (2, 190), 'B': (2, 205), 'b': (2, 220), '<': (3, 100),
    '>': (3, 115), '(': (3, 130), ')': (3, 145), '[': (3, 175),
    ']': (3, 190), '#': (0, 220), 'L': (1, 150), 'E': (2, 220)
}

ENCODING_MAP2 = BidirectionalMap(mapping)