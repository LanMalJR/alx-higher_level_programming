#!/usr/bin/python3
'''
Generate the Pascal triangle of n rows.
'''
def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        current_row = [1]

        for j in range(1, i):
            current_row.append(triangle[i-1][j-1] + triangle[i-1][j])

        current_row.append(1)

        triangle.append(current_row)

    return triangle


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
