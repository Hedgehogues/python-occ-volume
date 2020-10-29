import typing
from OCC.Core.BRepAdaptor import BRepAdaptor_Surface
from OCC.Core.BRepBndLib import brepbndlib_Add
from OCC.Core.Bnd import Bnd_Box
from OCC.Extend.TopologyUtils import TopologyExplorer

import io_


def is_curve(obj):
    try:
        cast_obj = BRepAdaptor_Surface(obj)
    except Exception as e:
        return True
    casts = [
        'Circle',
        'Cylinder',
        'Line',
        'BasisSurface',
        'OffsetCurve',
        'Ellipse',
        'Bezier',
        'Curve',
        'Sphere',
        'Parabola',
        'BSpline',
        'Hyperbola',
        'Cone',
        'Torus',
    ]
    curve = False
    for c in casts:
        try:
            getattr(cast_obj, c)()
            curve = True
            break
        except Exception as e:
            pass
    return curve


def bbox(*, shape: io_.Shape) -> typing.List:
    """
    :param shape:
    :return: volume (float)
    """
    te = TopologyExplorer(shape.shape_occ)
    max_x = -1
    max_y = -1
    max_z = -1
    min_x = None
    min_y = None
    min_z = None
    for obj in te.faces():
        if is_curve(obj):
            continue
        bbox_ = Bnd_Box()
        brepbndlib_Add(obj, bbox_)
        xmin, ymin, zmin, xmax, ymax, zmax = bbox_.Get()
        if xmax > max_x:
            max_x = xmax
        if ymax > max_y:
            max_y = ymax
        if zmax > max_z:
            max_z = zmax
        if min_x is None or xmin < min_x:
            min_x = xmin
        if min_y is None or ymin < min_y:
            min_y = ymin
        if min_z is None or zmin < min_z:
            min_z = zmin
    return [abs(max_x-min_x), abs(max_y-min_y), abs(max_z-min_z)]
