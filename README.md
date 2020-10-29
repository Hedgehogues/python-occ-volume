# python-occ-volume (Russian)

В этом репозитории я привожу пример двух способов вычисления объёма. Один из них я нашёл в официальном репозитории. Другой 
сделал сам, так как столкнулся с ошибкой. 

### Способ 1

В официальном репозитории предлагается строить вокруг модели Bounding Box. В результате чего, мы легко можем вычислить
его объём. Но, к сожалению, для ряда "сложных" поверхностей такой подход неприемлем, поскольку они могут выходить сильно
дальше, чем это предполагается рассчитать минимальные и максимальные координаты этого Bounding Box. 

В данном подходе не учитывается тот факт, что "сложные", теоритические поверхности: 

    [
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
    
могут выходить далеко за пределы заготовки, от чего происходит неверный рассчёт координат.

Пример детали, для который неверно рассчитываются координаты, Вы можете найти [здесь](Surf1.STEP). 

### Способ 2

Этот способ предлагает исключить все части, которые принадлежат множеству указанному в первом способе. Для остальных 
частей мы будем поочередно строить Bounding box и тогда сможем путем объединения таких Bounding box найти минимальный
возможный, в который входит деталь. 

### Комментарий

Если Вы хотите убедититься в правильности второго способа, откройте модель во FreeCad и выполните:

    FreeCAD.ActiveDocument.Objects[0].Shape.BoundBox
    
Вы также можете использовать любой другой софт. 

# python-occ-volume (English)

In this repository, I give an example of two ways to calculate volume. I found one of them in the official repository. Other
did it myself, as I ran into an error.

### Method 1

The official repository suggests building around the Bounding Box model. As a result, we can easily calculate
its volume. But, unfortunately, for a number of "complex" surfaces, this approach is unacceptable, since they can go out strongly
further than it is supposed to calculate the minimum and maximum coordinates of this Bounding Box.

This approach does not take into account the fact that "complex", theoretical surfaces:

    [
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
    
can go far beyond the workpiece, from which the coordinates are incorrectly calculated.

An example of a part for which the coordinates are incorrectly calculated can be found [here] (Surf1.STEP)

### Method 2

This method suggests excluding all parts that belong to the set specified in the first method. For others
parts we will build a Bounding box one by one, and then we can find the minimum
possible, which includes the part.

### Comment

If you want to make sure that the second method is correct, open the model in FreeCad and run:

     FreeCAD.ActiveDocument.Objects [0] .Shape.BoundBox
    
You can also use any other software.
