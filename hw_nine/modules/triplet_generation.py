import csv
from random import randint


def generating_random_triplets_in_csv_file(file_name):
    with open(file_name, 'w', newline='') as csv_f:
        writer = csv.writer(csv_f)
        for _ in range(randint(100, 1000)):
            row = [randint(1, 20) for _ in range(3)]
            writer.writerow(row)


generating_random_triplets_in_csv_file('../triplets.csv')