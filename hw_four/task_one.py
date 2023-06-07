import view


orig_matrix = [[2, 1, 3], [3, 1, 5]]


def transpose_matrix(data: list[[int]]) -> None:
    view.task_one(data)
    output_matrix = [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]
    view.task_one_result(output_matrix)
