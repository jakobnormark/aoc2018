#!/usr/local/bin/python3

class Coordinator():
    def __init__(self, input_file):
        self.coordinates = 0
        self.grid = 0
        self.xmax = 0
        self.ymax = 0
        self.parse_input(input_file)

    def parse_input(self, input_file):
        '''  Parse input file and fill coordinate system'''

        #First, parse the file
        with open(input_file, 'r') as f:
            coordinates = []
            rows = f.readlines()
            for row in rows:
                splitted = row.strip('\n').split(',')
                coordinate = [int(splitted[0]), int(splitted[1])]
                coordinates.append(coordinate)
                if coordinate[0] > self.xmax:
                    self.xmax = coordinate[0]+1
                if coordinate[1] > self.ymax:
                    self.ymax = coordinate[1]+1

        self.coordinates = coordinates

        # Then, build the coordinate system
        self.grid = [['.' for y in range(self.ymax)] for x in range(self.xmax)]

        #Populate coordinate system
        self.populate_coordinates()


    def populate_coordinates(self):
        poi = '0'
        for coordinate in self.coordinates:
            x = coordinate[0]
            y = coordinate[1]
            self.grid[x][y] = poi
            poi = chr(ord(poi) + 1)

        print(str(self.xmax))
        print(str(self.ymax))
        #print(str(self.grid))

    def populate_manhattan_distances(self):
        ''' Calculate Manhattan distance to each letter coordinate
            from coordinates that contain a '.'
            If manhattan distance is same for multiple coordinates
            leave the '.'
        '''
        for x in range(0, self.xmax):
            for y in range(0, self.ymax):
                if self.grid[x][y].isalpha() == False:
                    poi = '0'
                    closest_distance = None
                    closest_poi = ''
                    
                    for coordinate in self.coordinates:
                        coord_x = coordinate[0]
                        coord_y = coordinate[1]
                        coord_distance = abs(x-coord_x) + abs(y-coord_y)
                        if closest_distance is None or coord_distance < closest_distance:
                            closest_distance = coord_distance
                            closest_poi = poi
                        elif coord_distance == closest_distance:
                            closest_poi = '.'
                        poi = chr(ord(poi) + 1)
                    
                    self.grid[x][y] = closest_poi

        self.print_grid()

    def print_grid(self):
        grid = ''
        for y in range(0, self.ymax):
            if grid is not '':
                grid = grid + '\n'
            for x in range(0, self.xmax):
                grid = grid + self.grid[x][y]

        print(grid)

    def get_size_of_largest_area_not_infinite(self):
        ''' Return the size or the largest area that is not infinite '''
        poi = '0'
        largest_poi = ''
        largest_area = 0
        for coordinate in self.coordinates:
            grid_coordinates = []
            coordinate_area = 0
            finite = True

            for x in range(0, self.xmax):
                for y in range(0, self.ymax):
                    if self.grid[x][y].upper() == poi:
                        if x == 0 or x == self.xmax or y == 0 or y == self.ymax:
                            print(poi + ' is infinite')
                            finite = False
                            break
                        else:
                            coordinate_area = coordinate_area + 1

            if finite == True:
                if coordinate_area > largest_area:
                    largest_area = coordinate_area
                    largest_poi = poi

            poi = chr(ord(poi) + 1)

        print(largest_poi + ' area is ' + str(largest_area))
        return largest_area