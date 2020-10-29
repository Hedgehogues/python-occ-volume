import typing
from OCC.Core.BRepBndLib import brepbndlib_Add
from OCC.Core.Bnd import Bnd_Box

import io_


def bbox(*, shape: io_.Shape) -> typing.List:
    """
    :param shape:
    :return: sizes
    """
    bbox_ = Bnd_Box()
    brepbndlib_Add(shape.shape_occ, bbox_)
    xmin, ymin, zmin, xmax, ymax, zmax = bbox_.Get()
    x = xmax - xmin
    y = ymax - ymin
    z = zmax - zmin
    sides = sorted([x, y, z])[::-1]
    return sides
