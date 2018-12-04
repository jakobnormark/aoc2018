import claim

class Fabric:
    def __init__(self, input_file):
        self.input_file = input_file
        self.fabric_array = 0
        self.width = 0
        self.height = 0

    def parse_line(self, line):
        id_temp = line[1]
        x_coord = 0
        y_coord = 0
        x_width = 0
        y_width = 0
        i = 2
        while line[i] != ' ':
            id_temp = id_temp + line[i]
            i = i + 1

        id = int(id_temp)

        i = line.find('@') + 2
        x_temp = line[i]
        i = i + 1
        while line[i] != ',':
            x_temp = x_temp + line[i]
            i = i + 1

        x_coord = int(x_temp)

        i = i + 1
        y_temp = line[i]
        i = i + 1
        while line[i] != ':':
            y_temp = y_temp + line[i]
            i = i + 1

        y_coord = int(y_temp)

        i = i + 2
        x_width_temp = line[i]
        i = i + 1
        while line[i] != 'x':
            x_width_temp = x_width_temp + line[i]
            i = i + 1

        x_width = int(x_width_temp)

        i = i + 1
        y_width_temp = line[i]
        i = i + 1
        while i < len(line):
            y_width_temp = y_width_temp + line[i]
            i = i + 1

        y_width = int(y_width_temp)

        return claim.Claim(id, x_coord, y_coord, x_width, y_width)

    def parse_input(self):
        claims = []
        with open(self.input_file, 'r') as f:
            rows = f.readlines()
            for line in rows:
                claims.append(self.parse_line(line))

        self.claims = claims
        self.width = self.get_max_x_coordinate(claims)
        self.height = self.get_max_y_coordinate(claims)
        print('Width: ' + str(self.width))
        print('Heigth: ' + str(self.height))

        self.fabric_array = [[set() for x in range(self.width+1)] for y in range(self.height+1)]

        self.populate_matrix()

    def populate_matrix(self):
        for claim in self.claims:
            for x in range(claim.get_x_coord(), claim.get_x_coord() + claim.get_x_width()):
                for y in range(claim.get_y_coord(), claim.get_y_coord() + claim.get_y_width()):
                    self.fabric_array[x][y].add(claim.get_id())

    def get_max_x_coordinate(self, claims):
        x_max = 0
        for claim in claims:
            if claim.get_xmax() > x_max:
                x_max = claim.get_xmax()
        return x_max

    def get_max_y_coordinate(self, claims):
        y_max = 0
        for claim in claims:
            if claim.get_ymax() > y_max:
                y_max = claim.get_ymax()

        return y_max

    def get_overlapping_inches(self):
        ''' Return number of overlapping
            inches with more than two claims '''
        overlaps = 0

        for x in range(0, self.width-1):
            for y in range(0, self.height-1):
                #print(str(x)+ ', ' + str(y) + ': ' + str(self.fabric_array[x][y]))
                if len(self.fabric_array[x][y]) > 1:
                    overlaps = overlaps + 1
        return overlaps

    def find_non_overlapping_id(self):
        for claim in self.claims:
            unique = True
            for x in range(claim.get_x_coord(), claim.get_x_coord() + claim.get_x_width()):
                for y in range(claim.get_y_coord(), claim.get_y_coord() + claim.get_y_width()):
                    if len(self.fabric_array[x][y]) > 1:
                        unique = False
            if unique:
                print('Found unique id: ' + str(claim.get_id()))