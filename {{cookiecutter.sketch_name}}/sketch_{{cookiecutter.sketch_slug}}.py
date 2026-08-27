import vsketch

from gcode import gwrite

class {{cookiecutter.class_name}}(vsketch.SketchClass):

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("{{cookiecutter.page_size}}", landscape={{cookiecutter.landscape}})
        vsk.scale("{{cookiecutter.preferred_unit}}")

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vpype = "linemerge linesimplify reloop linesort"
        vsk.vpype(vpype + gwrite())


if __name__ == "__main__":
    {{cookiecutter.class_name}}.display()
