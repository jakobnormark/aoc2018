from anytree import Node

class NavigationSystem():
    def __init__(self, input_file):
        self.root = None
        self.metadata_sum = 0
        self.parse_input(input_file)

    def get_metadata_sum(self):
        ''' Returns the metadata sum '''
        return self.metadata_sum

    def parse_input(self, input_file):
        with open(input_file, 'r') as f:
            numbers = []
            lines = f.readline().split(' ')
            for line in lines:
                numbers.append(int(line))

            # Build tree
            index = 0
            self.parse_numbers(numbers, index, self.root)
            print(self.root)

    def parse_numbers(self, numbers, index, parent_node):
        ''' Parse number list into binary tree 
            - return the new index'''
        print('index: ' + str(index))
        child_nodes = 0
        number_of_metadata = 0 

        if parent_node == None:
            node = Node(index)

        else:
            node = Node(index, parent_node)
        print('Node created on index: ' + str(index))

        child_nodes = numbers[index] # Get the number of child nodes
        index = index + 1
        number_of_metadata = numbers[index] # Get number of metadata entries
        index = index + 1 # Forward index to next node

        print('Child nodes: ' + str(child_nodes))
        print('Number of metadata: ' + str(number_of_metadata))

        for i in range(0, child_nodes):
            index = self.parse_numbers(numbers, index, node)

        # Finally, add metadata
        for i in range(0, number_of_metadata):
            self.metadata_sum = self.metadata_sum + numbers[index + i]
            print('Metadata: ' + str(numbers[index + i]))

        index = index + number_of_metadata
        return index