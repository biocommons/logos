import jinja2

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(searchpath=["."]), auto_reload=True
)

template = env.get_template("pinwheel.svg.jinja2")


def make_pinwheel(
    blade_l: int = 140,
    blade_r: int = 40,
    blade_w: int = 90,
    border_w: int = 4.0,
    clockwise: bool = True,
    flip: bool = False,
    colors: list = None,
    n_blades: int = 10,
    offset_x: int = 0,
    offset_y: int = 0,
    sandbox: bool = False,
):
    blade_w2 = blade_w - blade_r
    blade_l2 = blade_l - blade_r
    rot = 360.0 / n_blades

    return template.render(
        opts=dict(
            blade_l=blade_l,
            blade_r=blade_r,
            blade_w=blade_w,
            border_w=border_w,
            clockwise=clockwise,
            colors=colors,
            flip=flip,
            n_blades=n_blades,
            offset_x=offset_x,
            offset_y=offset_y,
            sandbox=sandbox,
            blade_l2=blade_l2,
            blade_w2=blade_w2,
            rot=rot,
        )
    )
