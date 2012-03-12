import numpy as np

SHORT = 2
LONG = 3

all_walls = []

def is_legal(wall, width, layer_of_new, width_of_new):
    my_width = sum(wall[layer_of_new]) + width_of_new
    height = len(wall)
    assert width_of_new == SHORT or width_of_new == LONG
    # Exceed width of wall?
    if my_width > width:
        return False
    # Match end of wall?
    if my_width == width:
        return True
    # Is there a layer above this?
    if layer_of_new < height - 1:
        running_sum = 0
        # Can I make the partial sum of the layer above match my_width?
        for brick in wall[layer_of_new + 1]:
            running_sum += brick
            if running_sum == my_width:
                return False
    # Is there a layer below this?
    if layer_of_new > 0:
        running_sum = 0
        for brick in wall[layer_of_new - 1]:
            running_sum += brick
            if running_sum == my_width:
                return False
    return True


def copy_wall(wall):
    new_wall = []
    for layer in range(len(wall)):
        new_wall.append([])
        for brick in wall[layer]:
            new_wall[layer].append(brick)
    return new_wall

def is_done(wall, width, height):
    for i in range(height):
        if sum(wall[i]) != width:
            return False
    else:
        return True


def is_adjacent(layer_one, layer_two):
    so_far_one = layer_one[0]
    so_far_two = layer_two[0]
    bookmark_one = 1
    bookmark_two = 1

    while True:
        if so_far_one < so_far_two:
            so_far_one += layer_one[bookmark_one]
            bookmark_one += 1
        elif so_far_one == so_far_two:
            if so_far_one == sum(layer_one):
                '''
                print layer_one
                print layer_two
                print
                '''
                return True
            else:
                return False
        else:  #if so_far_one > so_far_two
            so_far_two += layer_two[bookmark_two]
            bookmark_two += 1

def create_matrix(width):
    global all_walls
    all_walls = []
    lay_bricks(width)
    dimen = len(all_walls)
    matrix = [[None for j in range(dimen)] for i in range(dimen)]

    for i in range(dimen):
        for j in range(dimen):
            matrix[i][j] = 1 if is_adjacent(all_walls[i][0], all_walls[j][0]) else 0

    return matrix


def lay_bricks(width, height=1):
    wall = [[] for i in range(height)]

    def lay_brick(wall):
        if is_done(wall, width, height):
            all_walls.append(copy_wall(wall))
            return
        else:
            for layer in range(height):
                if sum(wall[layer]) == width - 1:
                    return
                elif sum(wall[layer]) == width:
                    continue
                else:
                    for size in [SHORT, LONG]:
                        if is_legal(wall, width, layer, size):
                            my_copy = copy_wall(wall)
                            my_copy[layer].append(size)
                            lay_brick(my_copy)
                    else:
                        return
    lay_brick(wall)


def one_row(width):
    if width == 1:
        return 0
    elif width == 2:
        return 1
    elif width == 3:
        return 1
    else:
        return one_row(width - 2) + one_row(width - 3)


def sum_of_adjacency_to_power(my_matrix, power):
    '''Hard coded script copied and pasted. "power" is assumed to be 9'''
    print 'taking: b = my_matrix * my_matrix...'  # **2
    b = np.dot(my_matrix, my_matrix)
    print 'taking: c = b * b...' # **4
    c = np.dot(b, b)
    print 'taking: d = c * c...' # **8
    d = np.dot(c, c)
    print 'taking e = my_matrix * d...' # **9
    e = np.dot(my_matrix, d)
    print 'taking np.sum(e)...'
    print np.sum(e)
    return np.sum(e)


def sum_of_vector_multiplied_by_adjacency(power):
    '''Hard coded script copied and pasted. "power" is assumed to be 9'''
    print 'creating matrix...'
    my_matrix = np.matrix(create_matrix(32))

    print 'matrix created.'
    print 'creating vector of 1\'s...'
    vect = np.matrix([1 for i in range(len(my_matrix))])
    print "vector of 1's created."
    print 'running loop'

    for i in range(9):
        print 'Working on: ' + str(i)
        vect = vect * my_matrix

    return np.sum(vect)


if __name__ == '__main__':
    import time
    start = time.time()
    print sum_of_vector_multiplied_by_adjacency(9)
    print "Execution took {0} seconds".format(time.time() - start)
