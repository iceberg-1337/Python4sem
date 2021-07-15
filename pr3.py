class C32:
    def __init__(self):
        self.state = 'A'

    def tag(self):
        if self.state == 'A':
            self.state = 'A'
            return 1
        if self.state == 'C':
            self.state = 'D'
            return 3
        if self.state == 'D':
            self.state = 'E'
            return 5
        if self.state == 'E':
            self.state = 'F'
            return 7
        if self.state == 'F':
            self.state = 'G'
            return 9
        return

    def trim(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'B':
            self.state = 'C'
            return 2
        if self.state == 'C':
            self.state = 'F'
            return 4
        if self.state == 'D':
            self.state = 'B'
            return 6
        if self.state == 'E':
            self.state = 'A'
            return 8

