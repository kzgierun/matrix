
import math


class Matrix:
    def __init__(self, values):
        if not math.sqrt(len(values)).is_integer():
            raise ValueError(
                f"The list provided must have length equal to square of natural number. Current length: {len(values)}")

        self.columns = int(math.sqrt(len(values)))
        self.rows = int(math.sqrt(len(values)))
        self.indices = self.columns ** 2
        self.values = [[0 for i in range(self.columns)] for j in range(self.rows)]
        counter = 0
        for i in range(self.rows):
            for j in range(self.columns):
                self.values[i][j] = values[counter]
                counter += 1

    def __str__(self):
        return f"Columns:{self.columns}, Rows:{self.rows}, Indices:{self.indices} Values:{self.values}"

    def __getitem__(self, index):
        x, y = index
        return self.values[x][y]

    def __add__(self, m2):
        if not len(self.values) == len(m2.values):
            raise ValueError(
                f"The matrices must have the same lengths. Current lengths: {self.indices} & {m2.indices}")

        return Matrix([self.values[i][j] + m2.values[i][j] for i in range(self.columns) for j in range(self.rows)])

    def __sub__(self, m2):
        if not len(self.values) == len(m2.values):
            raise ValueError(
                f"The matrices must have the same lengths. Current lengths: {self.indices} & {m2.indices}")

        return Matrix([self.values[i][j] - m2.values[i][j] for i in range(self.columns) for j in range(self.rows)])

    def __mul__(self, scalar):
        return Matrix([self.values[i][j] * scalar for i in range(self.columns) for j in range(self.rows)])

    def __matmul__(self, m2):
            if self.indices != m2.indices:
                raise ValueError(f"The matrices must have the same lengths. Current lengths: {self.indices} & {m2.indices}")

            mul = [0 for i in range(self.indices)]
            for i in range(self.columns):
                for j in range(self.columns):
                    for k in range(self.columns):
                        mul[i*self.columns + j] += self[i,k] * m2[k,j]
            return Matrix(mul)

    __rmul__ = __mul__

    def __eq__(self, m2):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.values[i][j] != m2.values[i][j]:
                    return False
        return True

    def __neg__(self):
        return self * (-1)

    def det(self):
        det = 0
        mat = self

        if mat.columns == 1:
            return mat[0,0]

        sign = 1

        for i in range(mat.columns):
            temp = Matrix.minor(mat,0,i)
            det += sign * mat[0,i] * Matrix.det(temp)

            # print(f"{det} += {sign} * {mat[0,i]} * {Matrix.det(temp)}")

            sign *= -1

        return det

    def minor(self, i, j):
        minor = []
        for x in range(self.columns):
            for y in range(self.rows):
                if x != i and y != j:
                    minor.append(self[x,y])
        return Matrix(minor)

values = [1,2,3,4]
values2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
values3 = [-5, 0, -1, 1, 2, -1, -3, 4, 1]
m1 = Matrix(values)
m2 = Matrix(values2)
m3 = m1 @ m2
print(m3)


assert Matrix([1,2,3,4]) + Matrix([2,3,4,5]) == Matrix([3,5,7,9])
assert Matrix([1,2,3,4]) - Matrix([2,3,4,5]) == Matrix([-1,-1,-1,-1])
assert Matrix([1,2,3,4]) * 10 == Matrix([10,20,30,40])
assert 10 * Matrix([1,2,3,4]) == Matrix([10,20,30,40])
assert -Matrix([1,2,3,4]) == Matrix([-1,-2,-3,-4])
assert Matrix([1,2,3,4]) == Matrix([1,2,3,4])
assert Matrix.minor(Matrix([1,2,3,4,5,6,7,8,9]), 0, 0) == Matrix([5,6,8,9])
assert Matrix.det(Matrix([4,3,2,2,   0,1,-3,3,   0,-1,3,3,   0,3,1,1])) == -240
values = [1,2,3,4]
values2 = [5,6,7,8]
m1 = Matrix(values)
m2 = Matrix(values2)
assert Matrix.det(m1) * Matrix.det(m2) == Matrix.det(m1 @ m2)
