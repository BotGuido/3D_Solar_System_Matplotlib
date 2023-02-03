import math
class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    '''
    Метод __init__() для класса Vector имеет три параметра, представляющих значение вдоль каждой оси.
    
    The __init__() method for the Vector class has three parameters representing a value along each axis.
    '''
    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
    '''
    __repr__() возвращает вывод, предназначенный для программиста, 
    показывающий имя класса. Выходные данные из repr() 
    могут быть использованы для воссоздания объекта
    
    __repr__() returns output intended for the programmer,
    showing the name of the class. Output from repr()
    can be used to recreate the object
    '''
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
    '''
    __str__() возвращает непрограммную версию строкового представления объекта. 
    В этом случае он возвращает изображение, которое обычно используется в математике
    для представления векторов, используя единичные векторы i, j и k.
    
    __str__() returns the non-program version of the object's string representation.
    In this case it returns an image which is commonly used in math
    to represent vectors using the unit vectors i, j, and k.
    '''
    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        elif item == 2:
            return self.z
        else:
            raise IndexError("There are only three elements in the vector")
    '''
    Определив __getitem__(), делаем класс Vector индексируемым. 
    Первый элемент в векторе – это значение x, второй – значение y, а третий – значение z. 
    Любой другой индекс вызовет ошибку.
    
    By defining __getitem__() , we make the Vector class indexable.
    The first element in the vector is the x value, the second is the y value, and the third is the z value.
    Any other index will raise an error.
    '''
    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
        )
    '''
    __add__() возвращает другой объект Vector, 
    каждый элемент которого равен сложению 
    соответствующих элементов в двух исходных векторах
    
    __add__() returns another Vector object,
    each element of which is equal to the addition
    corresponding elements in the two original vectors
    '''
    def __sub__(self, other):
        return Vector(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
        )
    '''
    __sub__() возвращает другой объект Vector, 
    каждый элемент которого равен вычитанию 
    соответствующих элементов в двух исходных векторах

    __sub__() returns another Vector object,
    each element of which is equal to the subtraction
    corresponding elements in the two original vectors
    '''
    def __mul__(self, other):
        if isinstance(other, Vector):  # Vector dot product
            return (
                    self.x * other.x
                    + self.y * other.y
                    + self.z * other.z
            )
        elif isinstance(other, (int, float)):  # Scalar multiplication
            return Vector(
                self.x * other,
                self.y * other,
                self.z * other,
            )
        else:
            raise TypeError("operand must be Vector, int, or float")
    '''
    Результат использования оператора * будет зависеть от того, 
    является ли второй операнд, следующий за символом *, скаляром или вектором. 
    Если второй операнд, представленный параметром other, имеет тип Vector, 
    вычисляется точечное произведение. Однако, если other имеет тип int или float, 
    возвращаемый результат представляет собой новый вектор, масштабированный соответствующим образом.
    
    The result of using the * operator will depend on whether
    whether the second operand following the * character is a scalar or a vector.
    If the second operand represented by other is of type Vector,
    dot product is calculated. However, if other is of type int or float,
    the result returned is a new vector scaled accordingly.
    '''
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector(
                self.x / other,
                self.y / other,
                self.z / other,
            )
        else:
            raise TypeError("operand must be int or float")
    '''
    Два вектора не могут быть разделены. Однако можно разделить вектор на скаляр
    
    The two vectors cannot be separated. However, one can divide a vector into a scalar
    '''
    def get_magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    '''
    Если есть вектор, то можно найти его величину
    
    If there is a vector, then you can find its value
    '''
    def normalize(self):
        magnitude = self.get_magnitude()
        return Vector(
            self.x / magnitude,
            self.y / magnitude,
            self.z / magnitude,
        )
    '''
    Нормализуем вектор
    
    Normalize the vector
    '''


