import os
import uuid

from OCC.Core.IFSelect import IFSelect_RetDone
from OCC.Core.STEPControl import STEPControl_Reader


class Shape:
    def __init__(self, shape, reader):
        self.__reader = reader
        self.__shape = shape

    @staticmethod
    def __extract(unit):
        return unit.First().ToCString().lower()

    @property
    def shape_occ(self):
        return self.__shape


class StepReader:
    def __init__(self, stream):
        """
        StepReader read file and returns shape of STEP model

        ### Warning ###
        you need to close stream, after finish working

        :param stream:
        """
        self.__temp_filename = f'data/{str(uuid.uuid4())}'
        with open(self.__temp_filename, 'w') as out_fd:
            out_fd.write(stream.read())
        self.__reader = None

    def close(self):
        os.remove(self.__temp_filename)

    def read(self):
        try:
            self.__reader = STEPControl_Reader()
            status = self.__reader.ReadFile(self.__temp_filename)
            assert status == IFSelect_RetDone
            roots = self.__reader.NbRootsForTransfer()
            if roots > 1:
                return None

            ok = self.__reader.TransferRoot(1)
            if not ok:
                return None

            number_of_shapes = self.__reader.NbShapes()
            if number_of_shapes > 1:
                return None
            if number_of_shapes == 0:
                return None
            shape = self.__reader.Shape(1)
            return Shape(shape=shape, reader=self.__reader)
        except Exception as e:
            print(e)
            return None


class StepReaderPath(StepReader):
    def __init__(self, filepath):
        """
        StepReader read file and returns shape of STEP model

        :param filepath: path to file
        """
        StepReader.__init__(self, open(filepath, 'r'))
