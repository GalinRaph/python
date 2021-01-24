class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        self.result = [[0, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0]]
        if len(self.list_1) == len(self.list_2):
            for i in range(len(self.list_1)):

                for j in range(len(self.list_1[0])):
                    self.result[i][j] = self.list_1[i][j] + self.list_2[i][j]

            return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.result]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.result]))


my_matrix = Matrix([[1, 2, 5],
                    [3, 4, 28],
                    [14, 3, 19]
                    ],
                   [[5, 6, 17],
                    [7, 8, 11],
                    [3, 4, 28]
                    ])

print(my_matrix.__add__())
