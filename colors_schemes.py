class Colors:
    def __init__(self):
        self.colors = []
        self.load_colors()
        self.i = 0

    def load_colors(self):
        with open('/home/benoit/.config/qtile/colors_schemes', 'r') as f:
            self.colors = [l.strip() for l in f.readlines()]

    def get_next_color(self):
        j = self.i
        self.i += 1
        if self.i >= len(self.colors):
            self.i = 0
        return self.colors[j]
