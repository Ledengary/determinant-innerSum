def two_to_two(matrix):
    answer = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    return answer

def build(matrix, exception_i, exception_j):
    # this functipon gets an i and j and bilds a new matrix by deleting that row and coloumn.
    new_matrix = []
    for i in range(0, len(matrix)):
        if i != exception_i:
            row = []
            for j in range(0, len(matrix)):
                if j != exception_j:
                    row.append(matrix[i][j])
            if len(row) != 0:
                new_matrix.append(row)
    return new_matrix

def three_to_three(matrix):
    answer = 0
    i = 0
    for j in range(0, len(matrix)):
        answer += (1 if j % 2 == 0 else -1) * (matrix[i][j] * two_to_two(build(matrix, i, j)))
    return answer

def calculate_determinant(matrix):
    # this is the main function which gets the matrix and travers through the first i elements.
    # the finishing condition is when the code hits the 2 * 2 matrix.
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return two_to_two(matrix)
    # elif len(matrix) == 3:
    #     return three_to_three(matrix)
    else:
        answer = 0
        i = 0
        for j in range(0, len(matrix)):
            answer += (1 if j % 2 == 0 else -1) * (matrix[i][j] * calculate_determinant(build(matrix, i, j)))
        return answer

n = int(input())
matrix = [[0 for x in range(n)] for y in range(n)]
for i in range(0, n):
    line = input()
    line_inputs = line.split(" ")
    for j in range(0, n):
        matrix[i][j] = float(line_inputs[j])


final_answer = str(calculate_determinant(matrix))
parts = final_answer.split(".")
if len(parts[1]) < 3:
    parts[1] += (3 - len(parts[1])) * '0'
else:
    parts[1] = parts[1][0:3]

print(parts[0] + "." + parts[1])