from datetime import date
from pathlib import Path
import shlex

import vpype_cli


def add_meta(name):
    """
    adds the current date to start of name.
    """

    today = date.today().strftime("%Y%m%d")
    parts = [today, name]
    return '_'.join(parts)

def gwrite(input_path: Path, landscape=True):
    """
    writes gcode from the input svg using gwrite with local plotter config.
    Appends the current date to the gcode filename. If the file is not in
    landscape format, rotate the sketch and fit to landscape for plotting
    """

    config_path = input_path.parents[2] / ".vpype.toml"
    out_path = input_path.parents[1] / "gcode" / add_meta(input_path.stem)

    args = f"-c {config_path} read {input_path} "

    if not landscape:
        args += f"pagerotate -cw "

    g_args = f"gwrite -p plotter {out_path}.gcode"

    vpype_cli.cli.main(prog_name="vpype",
                       args=shlex.split(args + g_args),
                       standalone_mode=False)

