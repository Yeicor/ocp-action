import cadquery as cq

show_object(
    cq.Workplane("XY").box(1, 2, 3),
    "simple_box", {"color": (0.25, 1.0, 0.75), "alpha": 0.5},
)
