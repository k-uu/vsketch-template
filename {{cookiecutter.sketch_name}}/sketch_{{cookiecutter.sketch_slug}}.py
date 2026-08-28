import vsketch
import pathlib
from gcode import gwrite

class {{cookiecutter.class_name}}(vsketch.SketchClass):

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("{{cookiecutter.page_size}}", landscape={{cookiecutter.landscape}})
        vsk.scale("{{cookiecutter.preferred_unit}}")

        # Sketch goes here

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")

    def post_finalize(self, vsk: vsketch.Vsketch, path: pathlib.Path) -> None:
        gwrite(path)

if __name__ == "__main__":
    {{cookiecutter.class_name}}.display()
