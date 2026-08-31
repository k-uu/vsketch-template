import vsketch
import pathlib
import gcode

LANDSCAPE = {{cookiecutter.landscape}}
PAGE_SIZE = "{{cookiecutter.page_size}}"

class {{cookiecutter.class_name}}(vsketch.SketchClass):

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size(PAGE_SIZE, landscape=LANDSCAPE)
        vsk.scale("{{cookiecutter.preferred_unit}}")

        # Sketch goes here

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype("linemerge linesimplify reloop linesort")

    def post_finalize(self, vsk: vsketch.Vsketch, path: pathlib.Path) -> None:
        gcode.gwrite(path, PAGE_SIZE, landscape=LANDSCAPE)

if __name__ == "__main__":
    {{cookiecutter.class_name}}.display()
