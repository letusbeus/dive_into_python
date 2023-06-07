import view


def bonus_calc(names: list[str], salaries: list[int], bonuses: list[str]) -> dict[str, float]:
    view.task_two()
    return {name: salary * float(bonus[:-1]) / 100 for name, salary, bonus in zip(names, salaries, bonuses)}
