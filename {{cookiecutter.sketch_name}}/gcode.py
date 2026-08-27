from datetime import date
from pathlib import Path

def add_meta(name, path):
    """
    adds the current date and iteration number to the gcode filename
    """

    today = date.today().strftime("%d%m%y")

    files = list(path.glob(f"{name}_*"))
    count = len(files) if files else 1
    parts = [name, today, str(count + 1)]
    return ('_'.join(parts) + ".gcode")


def gwrite():
        root = Path.cwd()
        name = "{{cookiecutter.sketch_name}}"
        dir_path = root / name / "gcode"
        file_path = dir_path / add_meta(name, dir_path)
        profile_path = root / ".vpype.toml"
        command = f" gwrite --profile {profile_path} {file_path}"

        return command