from modules import *
import view


@deco_save_to_json
@deco_finding_the_roots_of_a_quadratic_equation
def finding_the_roots(a, b, c):
    return finding_the_roots_of_a_quadratic_equation(a, b, c)

if __name__ == '__main__':
    view.task_one()
    csv_file = 'random_triplets.csv'
    generating_random_triplets_in_csv_file(csv_file)
    finding_the_roots(csv_file)
