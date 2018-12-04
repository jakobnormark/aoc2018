class Claim:
    def __init__(self, id, x_coord, y_coord, x_width, y_width):
        self.id = id
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.x_width = x_width
        self.y_width = y_width
        print(str(self.id) + ' ' + str(self.x_coord) + ' ' + str(self.y_coord) + ' ' + str(self.x_width) + ' ' + str(self.y_width))

    def get_id(self):
        return self.id

    def get_x_coord(self):
        return self.x_coord

    def get_y_coord(self):
        return self.y_coord

    def get_x_width(self):
        return self.x_width
        
    def get_y_width(self):
        return self.y_width

    def get_xmax(self):
        return self.x_coord + self.x_width

    def get_ymax(self):
        return self.y_coord + self.y_width