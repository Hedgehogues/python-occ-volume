import invalid
import valid
from io_ import StepReaderPath

reader = StepReaderPath(filepath='Surf1.STEP')
shape = reader.read()

x = invalid.bbox(shape=shape)
print(x)

x = valid.bbox(shape=shape)
print(x)

reader.close()

