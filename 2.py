class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.last = None
        self.value = None
        self.args = None

class Stack:
    def __init__(self):
        self.head = node()
        self.tail = node()
        self.size = 0

    def getSize(self):
        return self.size

    def pop(self):
        if self.size != 0:
            if self.size == 1:
                returnable = self.tail
                self.head = None
                self.tail = None
                self.size -= 1
                return returnable.data
            else:
                to_be_popped_node = self.tail
                before = to_be_popped_node.last
                self.tail = before
                before.next = None
                self.size -= 1
                return to_be_popped_node.data
        else:
            return "NULL"

    def push(self, data):
        new_node = node(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            before = self.tail
            self.tail = new_node
            new_node.last = before
            before.next = new_node
        self.size += 1

    def peek(self):
        if self.size != 0:
            return self.tail.data
        else:
            return "NULL"

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def display(self):
        the_list = []
        current_node = self.head
        while current_node.next != None:
            the_list.append(current_node.data)
            current_node = current_node.next
        the_list.append(self.tail.data)
        return the_list

answers = []
def break_down(line):
    opening_brackets_indexes = Stack()
    if line.count("{") == 1:
        # this is the ending condition which happens whenever the line is out of opening brackets which mean it's time
        # to calculate the inner elements.
        parts = line[1:len(line) - 1].split(",")
        parts = list(map(int, parts))
        return sum(parts)
    counter = 0
    while counter < len(line):
        each_char = line[counter]
        if each_char == "{":
            opening_brackets_indexes.push(counter)
            # saves the indexes of the opening brackets inside the string.
        elif each_char == "}":
            # if we hit a closing one, we get the last opening one and we calculate the inner one once more.
            opening_index = opening_brackets_indexes.pop()
            answer = int(break_down(line[opening_index:counter + 1]))
            line = line[0:opening_index] + str(answer) + line[counter + 1:len(line)]
            counter -= (counter - opening_index)
            answers.append(answer)
        counter += 1

inp = input()
break_down(inp)
for each in answers:
    print(each)