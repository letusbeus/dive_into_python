import os
import view


def split_path(data: str) -> tuple[str, str, str]:
    view.task_one()
    path, filename = os.path.split(data)
    name, ext = os.path.splitext(filename)
    return path, name, ext
