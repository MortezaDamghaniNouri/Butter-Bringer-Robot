import random
import time


# This class determines the location of nodes
class Location:
    def __init__(self, input_row, input_column):
        self.row = input_row
        self.column = input_column


    row = -1
    column = -1


# This class simulates the nodes in the search graph
class Node:
    def __init__(self, input_location):
        self.location = input_location




    location = ""
    parent = ""
    children = []
    content = ""
    cost = ""


# This function checks if the input location is available in input array or not
def does_exist(input_array, input_row, input_column, row, column):
    if 0 <= input_row < row and 0 <= input_column < column:
        return True
    return False


# This function finds the robot location
def robot_location_finder(input_array, row, column):
    i = 0
    while i < row:
        j = 0
        while j < column:

            if input_array[i][j].find("r") != -1:
                robot_location = Location(i, j)
                return robot_location

            j += 1

        i += 1


# This function checks if the butter is available among the input children or not
def is_butter_available(children):
    for i in children:
        if i.content.find('b') != -1:
            return i
    return False


# This function checks if the goal is available among the input children or not
def is_goal_available(children):
    for i in children:
        if i.content.find('p') != -1:
            return i
    return False



# This function checks if input location is available among the input children or not
def is_local_goal_available(children, location):
    for i in children:
        if i.location.row == location.row and i.location.column == location.column:
            return i
    return False


# This function finds the cost of the input node
def cost_finder(node):
    content = node.content
    if content.find('p') == -1 and content.find('b') == -1 and content.find('r') == -1:
        return int(content)
    content = content.rstrip(content[-1])
    return int(content)


# This function prints the map of the search
def map_printer(input_array):
    line = "-" * 10 * len(input_array[0])
    print(line)
    for i in input_array:
        row = ""
        for j in i:
            row += "|" + 4 * " " + j + " " * 4
        print(row + "|")
    print(line)
    print()



# This function finds the first children node of the input array
def first_children_finder(input_list):
    random_number = random.randint(0, (len(input_list) - 1))
    return [input_list[random_number], random_number]


# This function finds the children of the input node while searching for the first butter
def butter_children_finder(input_array, node, row, column):
    node_row = node.location.row
    node_column = node.location.column
    children = []
    if does_exist(input_array, node_row, node_column + 1, row, column):
        if input_array[node_row][node_column + 1] != "x":
            child = Node(Location(node_row, node_column + 1))
            child.parent = node
            child.content = input_array[node_row][node_column + 1]
            child.cost = cost_finder(child)
            children.append(child)

    if does_exist(input_array, node_row, node_column - 1, row, column):
        if input_array[node_row][node_column - 1] != "x":
            child = Node(Location(node_row, node_column - 1))
            child.parent = node
            child.content = input_array[node_row][node_column - 1]
            child.cost = cost_finder(child)
            children.append(child)

    if does_exist(input_array, node_row + 1, node_column, row, column):
        if input_array[node_row + 1][node_column] != "x":
            child = Node(Location(node_row + 1, node_column))
            child.parent = node
            child.content = input_array[node_row + 1][node_column]
            child.cost = cost_finder(child)
            children.append(child)

    if does_exist(input_array, node_row - 1, node_column, row, column):
        if input_array[node_row - 1][node_column] != "x":
            child = Node(Location(node_row - 1, node_column))
            child.parent = node
            child.content = input_array[node_row - 1][node_column]
            child.cost = cost_finder(child)
            children.append(child)



    if node.parent != "":
        parent_node = node.parent
        for i in children:
            if i.location.row == parent_node.location.row and i.location.column == parent_node.location.column:
                children.remove(i)
                break

    return children


# This function finds the children of the input node while searching for the first butter
def goal_children_finder(input_array, node, row, column):
    node_row = node.location.row
    node_column = node.location.column
    children = []
    if does_exist(input_array, node_row, node_column + 1, row, column):
        if input_array[node_row][node_column + 1] != "x":
            child = Node(Location(node_row, node_column + 1))
            child.parent = node
            child.content = input_array[node_row][node_column + 1]
            child.cost = cost_finder(child)
            children.append(child)

    if does_exist(input_array, node_row, node_column - 1, row, column):
        if input_array[node_row][node_column - 1] != "x":
            child = Node(Location(node_row, node_column - 1))
            child.parent = node
            child.content = input_array[node_row][node_column - 1]
            child.cost = cost_finder(child)
            children.append(child)

    if does_exist(input_array, node_row + 1, node_column, row, column):
        if input_array[node_row + 1][node_column] != "x":
            child = Node(Location(node_row + 1, node_column))
            child.parent = node
            child.content = input_array[node_row + 1][node_column]
            child.cost = cost_finder(child)
            children.append(child)

    if does_exist(input_array, node_row - 1, node_column, row, column):
        if input_array[node_row - 1][node_column] != "x":
            child = Node(Location(node_row - 1, node_column))
            child.parent = node
            child.content = input_array[node_row - 1][node_column]
            child.cost = cost_finder(child)
            children.append(child)

    return children




# This function is used to find the proper location of the robot to push the butter
def ids_location_finder(input_array, row, column, start_location, local_goal_location, opened_nodes, generated_nodes):
    finished = False
    allowed_depth = 1
    current_depth = 0
    cost = 0
    unchanged_opened_nodes = opened_nodes
    unchanged_generated_nodes = generated_nodes
    current_node = Node(start_location)
    opened_nodes += 1
    current_node.children = butter_children_finder(input_array, current_node, row, column)
    generated_nodes += 1
    current_node.content = input_array[start_location.row][start_location.column]
    current_node.cost = cost_finder(current_node)
    path = [current_node]
    butter_node = ""
    failure = False

    while True:
        while current_depth < allowed_depth:
            if len(current_node.children) != 0:
                cost += int(current_node.cost)
                is_local_goal_available_result = is_local_goal_available(current_node.children, local_goal_location)
                generated_nodes += len(current_node.children)
                if is_local_goal_available_result == False:
                    [next_node, index] = first_children_finder(current_node.children)
                    current_node.children.pop(index)
                    current_node = next_node
                    path.append(current_node)
                    current_depth += 1
                    current_node.cost = cost_finder(current_node)
                    current_node.children = butter_children_finder(input_array, current_node, row, column)
                    opened_nodes += 1



                else:
                    butter_node = is_local_goal_available_result
                    finished = True
                    break

            else:
                if current_node.parent != "":
                    current_node = current_node.parent
                    path.append(current_node)
                    current_depth = current_depth - 1

                else:
                    current_depth = 0
                    if allowed_depth >= 100000:
                        failure = True
                        break
                    generated_nodes = unchanged_generated_nodes + 1
                    opened_nodes = unchanged_opened_nodes + 1
                    allowed_depth = allowed_depth + 1
                    current_node = Node(start_location)
                    current_node.children = butter_children_finder(input_array, current_node, row, column)
                    current_node.content = input_array[start_location.row][start_location.column]
                    current_node.cost = cost_finder(current_node)
                    path = [current_node]



        if failure:
            return [failure, path]
        if finished:
            break
        else:
            current_depth = current_depth - 1
            current_node = current_node.parent
            path.append(current_node)



    path.append(butter_node)
    return [failure, path, opened_nodes, generated_nodes, current_depth, cost]


# This function locates the places of Xs in the input array in another array and returns the array
def x_locator(input_array, row, column):
    output_array = []
    i = 0
    while i < row:
        temp = []
        j = 0
        while j < column:
            temp.append(" ")
            j += 1
        output_array.append(temp)
        i += 1

    i = 0
    while i < row:
        j = 0
        while j < column:
            if input_array[i][j] == "x":
                output_array[i][j] = "x"
            j += 1
        i += 1
    return output_array




# This function copies the input array
def array_copier(input_array, row, column):
    copied_array = []
    i = 0
    while i < row:
        temp = []
        j = 0
        while j < column:
            temp.append(" ")
            j += 1
        copied_array.append(temp)
        i += 1

    i = 0
    while i < row:
        j = 0
        while j < column:
            copied_array[i][j] = input_array[i][j]
            j += 1
        i += 1
    return copied_array


# This function checks if a butter is available in the input array
def does_butter_exist(input_array):
    for i in input_array:
        for j in i:
            if j.find("b") != -1:
                return True
    return False


# This function generates the output file and stores it in Outputs folder
def output_file_generator(opened_nodes, generated_nodes, butter_finding_part_depth, goal_finding_part_depth, cost, time, input_file_name, algorithm_type):
    output_file = open("Outputs/" + input_file_name.rstrip(".txt") + "_" + algorithm_type + ".txt", "wt")





# This function implements the IDS algorithm
def ids_algorithm(input_array, row, column, input_file_name):
    start_time = time.perf_counter()
    generated_nodes = 1
    opened_nodes = 1
    cost = 0
    butter_finding_part_depth = 0
    goal_finding_part_depth = 0
    while does_butter_exist(input_array):
        robot_location = robot_location_finder(input_array, row, column)
        finished = False
        allowed_depth = 1
        current_depth = 0
        initial_generated_nodes = generated_nodes
        initial_opened_nodes = opened_nodes
        current_node = Node(robot_location)
        current_node.children = butter_children_finder(input_array, current_node, row, column)
        current_node.content = input_array[robot_location.row][robot_location.column]
        current_node.cost = cost_finder(current_node)
        butter_node = ""
        butter_finding_failure = False
        path = []

        while True:
            while current_depth < allowed_depth:
                if len(current_node.children) != 0:
                    cost += int(current_node.cost)
                    is_butter_available_result = is_butter_available(current_node.children)
                    generated_nodes += len(current_node.children)
                    if is_butter_available_result == False:
                        [next_node, index] = first_children_finder(current_node.children)
                        current_node.children.pop(index)
                        current_node = next_node
                        path.append(current_node)
                        current_node.cost = cost_finder(current_node)
                        current_depth += 1
                        current_node.children = butter_children_finder(input_array, current_node, row, column)
                        opened_nodes += 1




                    else:
                        butter_node = is_butter_available_result
                        finished = True
                        break

                else:
                    if current_node.parent != "":
                        current_node = current_node.parent
                        path.append(current_node)
                        current_depth = current_depth - 1

                    else:
                        current_depth = 0
                        if allowed_depth >= 100000:
                            butter_finding_failure = True
                            break
                        opened_nodes = initial_opened_nodes
                        allowed_depth = allowed_depth + 1
                        current_node = Node(robot_location)
                        current_node.children = butter_children_finder(input_array, current_node, row, column)
                        generated_nodes = initial_generated_nodes
                        current_node.content = input_array[robot_location.row][robot_location.column]
                        current_node.cost = cost_finder(current_node)
                        path = [current_node]

            if butter_finding_failure:
                print("UNABLE TO FIND A PATH TO THE BUTTER BY IDS")
                return 0
            if finished:
                break
            else:
                current_depth = current_depth - 1
                current_node = current_node.parent
                path.append(current_node)

        # print("path: ")
        # for i in path:
        #    print(str(i.location.row) + ", " + str(i.location.column))
        # print("===============")
        # print("Butter location: ")
        # print(str(butter_node.location.row) + ", " + str(butter_node.location.column))
        # print("current location: ")
        # print(str(current_node.location.row) + ", " + str(current_node.location.column))

        print("The path from robot location to the butter: ")
        for i in path:
            map_array = x_locator(input_array, row, column)
            map_array[i.location.row][i.location.column] = "r"
            map_array[butter_node.location.row][butter_node.location.column] = "b"
            map_printer(map_array)



        print("BUTTER FOUND")
        goal_finding_part_depth = 0
        butter_finding_part_depth = current_depth
        first_robot_location = robot_location
        copy_input_array = array_copier(input_array, row, column)
        robot_location = current_node.location
        goal_finished = False


        first_butter_node = butter_node
        butter_path = [butter_node.location]
        butter_node.children = goal_children_finder(copy_input_array, butter_node, row, column)

        counter = 1
        while True:
            # A number is chose for infinite loop handling
            if len(butter_node.children) != 0 and counter <= 10000000:
                [next_node, index] = first_children_finder(butter_node.children)

                if next_node.location.row == butter_node.location.row and next_node.location.column == butter_node.location.column - 1:
                    if does_exist(copy_input_array, butter_node.location.row, butter_node.location.column + 1, row,
                                  column) and copy_input_array[butter_node.location.row][butter_node.location.column + 1] != "x":
                        local_goal_location = Location(butter_node.location.row, butter_node.location.column + 1)
                        if robot_location.row != local_goal_location.row or robot_location.column != local_goal_location.column:
                            [failure_result, local_path, opened_nodes, generated_nodes, output_depth, output_cost] = ids_location_finder(copy_input_array, row, column, robot_location, local_goal_location, opened_nodes, generated_nodes)
                            goal_finding_part_depth += output_depth
                            cost += output_cost
                        else:
                            failure_result = False
                            local_path = []

                        if not failure_result:
                            for k in local_path:
                                path.append(k)
                            for m in local_path:
                                map_array = x_locator(input_array, row, column)
                                map_array[m.location.row][m.location.column] = "r"
                                map_array[butter_node.location.row][butter_node.location.column] = "b"
                                map_printer(map_array)

                        if failure_result:
                            butter_node.children.pop(index)

                        else:
                            robot_location = butter_node.location
                            path.append(Node(robot_location))
                            butter_path.append(next_node.location)
                            if input_array[next_node.location.row][next_node.location.column].find('p') != -1:
                                goal_finished = True
                                break
                            copy_input_array[butter_node.location.row][butter_node.location.column] = \
                            input_array[butter_node.location.row][butter_node.location.column]
                            if copy_input_array[butter_node.location.row][butter_node.location.column].find('b') != -1:
                                copy_input_array[butter_node.location.row][butter_node.location.column] = \
                                copy_input_array[butter_node.location.row][butter_node.location.column].rstrip('b')
                            # copy_input_array[next_node.location.row][next_node.location.column] = "x"
                            butter_node = Node(Location(next_node.location.row, next_node.location.column))

                            map_array = x_locator(input_array, row, column)
                            map_array[robot_location.row][robot_location.column] = "r"
                            map_array[butter_node.location.row][butter_node.location.column] = "b"
                            map_printer(map_array)
                            butter_node.children = goal_children_finder(copy_input_array, butter_node, row, column)

                    else:
                        butter_node.children.pop(index)

                if next_node.location.row == butter_node.location.row and next_node.location.column == butter_node.location.column + 1:

                    if does_exist(copy_input_array, butter_node.location.row, butter_node.location.column - 1, row,
                                  column) and copy_input_array[butter_node.location.row][butter_node.location.column - 1] != "x":
                        local_goal_location = Location(butter_node.location.row, butter_node.location.column - 1)
                        if robot_location.row != local_goal_location.row or robot_location.column != local_goal_location.column:
                            [failure_result, local_path, opened_nodes, generated_nodes, output_depth, output_cost] = ids_location_finder(copy_input_array, row, column, robot_location, local_goal_location, opened_nodes, generated_nodes)
                            goal_finding_part_depth += output_depth
                            cost += output_cost
                        else:
                            failure_result = False
                            local_path = []

                        if not failure_result:
                            for k in local_path:
                                path.append(k)

                            for m in local_path:
                                map_array = x_locator(input_array, row, column)
                                map_array[m.location.row][m.location.column] = "r"
                                map_array[butter_node.location.row][butter_node.location.column] = "b"
                                map_printer(map_array)

                        if failure_result:
                            butter_node.children.pop(index)

                        else:
                            robot_location = butter_node.location
                            path.append(Node(robot_location))
                            butter_path.append(next_node.location)
                            if input_array[next_node.location.row][next_node.location.column].find('p') != -1:
                                goal_finished = True
                                break
                            copy_input_array[butter_node.location.row][butter_node.location.column] = \
                            input_array[butter_node.location.row][butter_node.location.column]
                            if copy_input_array[butter_node.location.row][butter_node.location.column].find('b') != -1:
                                copy_input_array[butter_node.location.row][butter_node.location.column] = \
                                copy_input_array[butter_node.location.row][butter_node.location.column].rstrip('b')
                            # copy_input_array[next_node.location.row][next_node.location.column] = "x"
                            butter_node = Node(Location(next_node.location.row, next_node.location.column))

                            map_array = x_locator(input_array, row, column)
                            map_array[robot_location.row][robot_location.column] = "r"
                            map_array[butter_node.location.row][butter_node.location.column] = "b"
                            map_printer(map_array)
                            butter_node.children = goal_children_finder(copy_input_array, butter_node, row, column)
                    else:
                        butter_node.children.pop(index)

                if next_node.location.row == butter_node.location.row - 1 and next_node.location.column == butter_node.location.column:
                    if does_exist(copy_input_array, butter_node.location.row + 1, butter_node.location.column, row,
                                  column) and copy_input_array[butter_node.location.row + 1][butter_node.location.column] != "x":
                        local_goal_location = Location(butter_node.location.row + 1, butter_node.location.column)
                        if robot_location.row != local_goal_location.row or robot_location.column != local_goal_location.column:
                            [failure_result, local_path, opened_nodes, generated_nodes, output_depth, output_cost] = ids_location_finder(copy_input_array, row, column, robot_location, local_goal_location, opened_nodes, generated_nodes)
                            goal_finding_part_depth += output_depth
                            cost += output_cost
                        else:
                            failure_result = False
                            local_path = []

                        if not failure_result:
                            for k in local_path:
                                path.append(k)

                            for m in local_path:
                                map_array = x_locator(input_array, row, column)
                                map_array[m.location.row][m.location.column] = "r"
                                map_array[butter_node.location.row][butter_node.location.column] = "b"
                                map_printer(map_array)

                        if failure_result:
                            butter_node.children.pop(index)

                        else:
                            robot_location = butter_node.location
                            path.append(Node(robot_location))
                            butter_path.append(next_node.location)
                            if input_array[next_node.location.row][next_node.location.column].find('p') != -1:
                                goal_finished = True
                                break
                            copy_input_array[butter_node.location.row][butter_node.location.column] = \
                            input_array[butter_node.location.row][butter_node.location.column]
                            if copy_input_array[butter_node.location.row][butter_node.location.column].find('b') != -1:
                                copy_input_array[butter_node.location.row][butter_node.location.column] = \
                                copy_input_array[butter_node.location.row][butter_node.location.column].rstrip('b')
                            # copy_input_array[next_node.location.row][next_node.location.column] = "x"
                            butter_node = Node(Location(next_node.location.row, next_node.location.column))

                            map_array = x_locator(input_array, row, column)
                            map_array[robot_location.row][robot_location.column] = "r"
                            map_array[butter_node.location.row][butter_node.location.column] = "b"
                            map_printer(map_array)
                            butter_node.children = goal_children_finder(copy_input_array, butter_node, row, column)
                    else:
                        butter_node.children.pop(index)

                if next_node.location.row == butter_node.location.row + 1 and next_node.location.column == butter_node.location.column:
                    if does_exist(copy_input_array, butter_node.location.row - 1, butter_node.location.column, row,
                                  column) and copy_input_array[butter_node.location.row - 1][butter_node.location.column] != "x":
                        local_goal_location = Location(butter_node.location.row - 1, butter_node.location.column)
                        if robot_location.row != local_goal_location.row or robot_location.column != local_goal_location.column:
                            [failure_result, local_path, opened_nodes, generated_nodes, output_depth, output_cost] = ids_location_finder(copy_input_array, row, column, robot_location, local_goal_location, opened_nodes, generated_nodes)
                            goal_finding_part_depth += output_depth
                            cost += output_cost
                        else:
                            failure_result = False
                            local_path = []

                        if not failure_result:
                            for k in local_path:
                                path.append(k)
                            for m in local_path:
                                map_array = x_locator(input_array, row, column)
                                map_array[m.location.row][m.location.column] = "r"
                                map_array[butter_node.location.row][butter_node.location.column] = "b"
                                map_printer(map_array)

                        if failure_result:
                            butter_node.children.pop(index)

                        else:
                            robot_location = butter_node.location
                            path.append(Node(robot_location))
                            butter_path.append(next_node.location)
                            if input_array[next_node.location.row][next_node.location.column].find('p') != -1:
                                goal_finished = True
                                break
                            copy_input_array[butter_node.location.row][butter_node.location.column] = \
                            input_array[butter_node.location.row][butter_node.location.column]
                            if copy_input_array[butter_node.location.row][butter_node.location.column].find('b') != -1:
                                copy_input_array[butter_node.location.row][butter_node.location.column] = \
                                copy_input_array[butter_node.location.row][butter_node.location.column].rstrip('b')
                            # copy_input_array[next_node.location.row][next_node.location.column] = "x"
                            butter_node = Node(Location(next_node.location.row, next_node.location.column))

                            map_array = x_locator(input_array, row, column)
                            map_array[robot_location.row][robot_location.column] = "r"
                            map_array[butter_node.location.row][butter_node.location.column] = "b"
                            map_printer(map_array)
                            butter_node.children = goal_children_finder(copy_input_array, butter_node, row, column)

                    else:
                        butter_node.children.pop(index)


            else:
                if (butter_node.location.row == 0 and butter_node.location.column == 0) or (
                        butter_node.location.row == 0 and butter_node.location.column == column - 1) or (
                        butter_node.location.row == row - 1 and butter_node.location.column == 0) or (
                        butter_node.location.row == row - 1 and butter_node.location.column == column - 1):
                    robot_location = butter_node.location
                    path.append(Node(robot_location))
                    butter_path.append(next_node.location)
                    if input_array[next_node.location.row][next_node.location.column].find('p') != -1:
                        goal_finished = True
                        break
                    copy_input_array[butter_node.location.row][butter_node.location.column] = \
                    input_array[butter_node.location.row][butter_node.location.column]
                    if copy_input_array[butter_node.location.row][butter_node.location.column].find('b') != -1:
                        copy_input_array[butter_node.location.row][butter_node.location.column] = \
                        copy_input_array[butter_node.location.row][butter_node.location.column].rstrip('b')
                    # copy_input_array[next_node.location.row][next_node.location.column] = "x"
                    butter_node = Node(Location(next_node.location.row, next_node.location.column))

                    map_array = x_locator(input_array, row, column)
                    map_array[robot_location.row][robot_location.column] = "r"
                    map_array[butter_node.location.row][butter_node.location.column] = "b"
                    map_printer(map_array)
                    butter_node.children = goal_children_finder(copy_input_array, butter_node, row, column)
                else:
                    print("FAILURE")
                    break
            counter += 1
        if goal_finished:
            map_array = x_locator(input_array, row, column)
            map_array[robot_location.row][robot_location.column] = "r"
            map_array[butter_path[-1].row][butter_path[-1].column] = "b"
            map_printer(map_array)
            print("GOAL FOUND")
            print("=================")
            print("The robot path: ")
            for i in path:
                print(str(i.location.row) + ", " + str(i.location.column))

            print("=================")
            print("The butter path: ")
            for i in butter_path:
                print(str(i.row) + ", " + str(i.column))

            print("=================")
            print("The input array is: ")
            input_array[first_butter_node.location.row][first_butter_node.location.column] = str(first_butter_node.cost)
            input_array[first_robot_location.row][first_robot_location.column] = input_array[first_robot_location.row][first_robot_location.column].rstrip("r")
            input_array[butter_path[-1].row][butter_path[-1].column] = "x"
            input_array[robot_location.row][robot_location.column] += "r"
            map_printer(input_array)


    # This part of the code stops the timer
    finish_time = time.perf_counter()
    output_file_generator(opened_nodes, generated_nodes, butter_finding_part_depth, goal_finding_part_depth, cost, finish_time - start_time, input_file_name, "IDS")
















# Main part of the project starts here
input_file_name = input("Enter the name of the input file: ")
try:
    input_file = open("Inputs/" + input_file_name, "rt")
    row = ""
    while True:
        char = input_file.read(1)
        if char == '\t':
            break
        row += char

    row = int(row)

    column = ""
    while True:
        char = input_file.read(1)
        if char == '\n':
            break
        column += char

    column = int(column)


    input_array = []
    temp_row = []
    new_line = False
    end_of_file = False
    while True:

        cell = ""
        while True:
            char = input_file.read(1)
            if not char:
                end_of_file = True
                break

            if char == '\t':
                break

            if char == '\n':
                new_line = True
                break
            cell += char
        temp_row.append(cell)
        if new_line:
            input_array.append(temp_row)
            temp_row = []
            new_line = False
        if end_of_file:
            input_array.append(temp_row)
            break





    copy_input_array = array_copier(input_array, row, column)
    ids_algorithm(copy_input_array, row, column, input_file_name)










    input_file.close()
except (FileExistsError, FileNotFoundError) as e:
    print("This file does not exist in the Inputs folder")






































































