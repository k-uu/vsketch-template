from datetime import date
from pathlib import Path
import shlex

import vpype_cli


def add_meta(name):
    """
    adds the current date to start of name
    """

    today = date.today().strftime("%Y%m%d")
    parts = [today, name]
    return ('_'.join(parts) + ".gcode")

def gwrite(file_path: Path):

    file_path = file_path.parent / add_meta(file_path.stem)
    args = f"gwrite -p plotter {file_path}"
    vpype_cli.cli.main(prog_name="vpype",
                       args=shlex.split(args),
                       standalone_mode=False)
