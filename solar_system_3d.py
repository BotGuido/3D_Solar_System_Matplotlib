import itertools
import matplotlib.pyplot as plt
from vectors import Vector
import math
class SolarSystem:
    '''
    Определяем класс SolarSystem с помощью метода __init__(),
    который включает в себя параметр size.
    bodies представляет собой пустой список, который будет содержать
    все тела в пределах Солнечной системы
    Метод add_body() может быть использован для добавления орбитальных тел в Солнечную систему

    We define the SolarSystem class using the __init__() method,
    which includes the size parameter.
    bodies is an empty list that will contain
    all bodies within the solar system
    The add_body() method can be used to add orbiting bodies to the solar system
    '''
    def __init__(self, size):
        self.size = size
        self.bodies = []
        self.fig, self.ax = plt.subplots(
            1,
            1,
            subplot_kw={"projection": "3d"},
            figsize=(self.size / 50, self.size / 50),
        )
        self.fig.tight_layout()
        '''
        Вызываем plt.subplots(), который возвращает фигуру и набор осей. 
        Возвращаемым значениям присваиваются атрибутам fig и ax. 
        Вызываеем plt.subplots() со следующими аргументами:
        Первые два аргумента равны 1 и 1 для создания единого набора осей на рисунке.
        Параметр subplot_kw имеет словарь в качестве аргумента, который устанавливает проекцию в 3D. 
        Это означает, что созданные оси являются объектом Axes3D.
        figsize задает общий размер фигуры, содержащей объект Axes3D.
        Вызываем метод tight_layout(). Это метод класса Figure в Matplotlib. Он уменьшает поля по краям рисунка.
        
        We call plt.subplots() which returns a figure and a set of axes.
        Return values are assigned to the fig and ax attributes.
        We call plt.subplots() with the following arguments:
        The first two arguments are 1 and 1 to create a single set of axes in the figure.
        The subplot_kw parameter has a dictionary argument that sets the projection to 3D.
        This means that the generated axes are an Axes3D object.
        figsize specifies the overall size of the figure containing the Axes3D object.
        We call the tight_layout() method. This is a method of the Figure class in Matplotlib. It reduces the margins at the edges of the picture.
        '''
        self.ax.view_init(0, 0)
    def add_body(self, body):
        self.bodies.append(body)

    def update_all(self):
        for body in self.bodies:
            body.move()
            body.draw()
    '''
    Метод update_all() проходит через каждое тело в Солнечной системе и перемещает и рисует каждое тело.
    
    The update_all() method goes through every body in the solar system and moves and draws each body.
    '''
    def draw_all(self):
        self.ax.set_xlim((-self.size / 2, self.size / 2))
        self.ax.set_ylim((-self.size / 2, self.size / 2))
        self.ax.set_zlim((-self.size / 2, self.size / 2))
        self.ax.axis(False) # not necessary
        plt.pause(0.001)
        self.ax.clear()
    '''
    Метод draw_all() устанавливает ограничения для трёх осей, используя размер Солнечной системы, 
    и обновляет график с помощью функции pause(). Этот метод также очищает оси, 
    подготавливая их к следующему графику.

    The draw_all() method sets the constraints for the three axes using the size of the solar system,
    and updates the chart with the pause() function. This method also clears the axes,
    preparing them for the next schedule.
    '''
    def calculate_all_body_interactions(self):
        '''
        Метод calculate_all_body_interactions() проходит через все тела в Солнечной системе.
        Каждое тело взаимодействует со всеми другими телами в Cолнечной системе

        The calculate_all_body_interactions() method goes through all the bodies in the solar system.
        Every body interacts with every other body in the solar system
        '''
        bodies_copy = self.bodies.copy()
        '''
        Используем копию self.bodies, чтобы учесть возможность того, что тела будут удалены из 
        Cолнечной системы во время цикла
        
        Use a copy of self.bodies to account for the possibility of bodies being removed from
        solar system during a cycle
        '''
        for idx, first in enumerate(bodies_copy):
            for second in bodies_copy[idx + 1:]:
                '''
                Чтобы убедиться, что ваш код не вычисляет взаимодействия между одними и теми же двумя телами дважды, 
                вы вычисляете только взаимодействия между телом и теми телами, которые следуют за ним в списке
                
                To make sure your code doesn't calculate interactions between the same two bodies twice,
                you calculate only the interactions between the body and those bodies that follow it in the list
                '''
                first.accelerate_due_to_gravity(second)

    def update_all(self):
        self.bodies.sort(key=lambda item: item.position[0])
        '''
        Используем метод sort списка с параметром key, чтобы определить правило для сортировки списка. 
        Лямбда-функция устанавливает это правило. 
        В этом случае используем значение position[0] каждого тела, которое представляет координату x. 
        Следовательно, каждый раз, когда вызываем update_all() в цикле симуляции while, 
        список тел переупорядочивается в зависимости от их положения вдоль оси x.
        
        We use the sort method of the list with the key parameter to define a rule for sorting the list.
        The lambda function sets this rule.
        In this case, use the position[0] value of each body that represents the x coordinate.
        Therefore, every time we call update_all() in the simulation's while loop,
        the list of bodies is reordered based on their position along the x-axis.
        '''
        for body in self.bodies:
            body.move()
            body.draw()

class SolarSystemBody:
    min_display_size = 10
    display_log_base = 1.3
    '''
    Атрибуты класса min_display_size и display_log_base задают параметры для определения 
    размера маркеров, которые будут отображаться на 3D-графике
    
    The min_display_size and display_log_base class attributes set parameters for determining
    the size of the markers that will be displayed on the 3D graphics
    '''
    def __init__(
        self,
        solar_system,
        mass,
        position=(0, 0, 0),
        velocity=(0, 0, 0),
    ):
        self.solar_system = solar_system
        self.mass = mass
        self.position = position
        self.velocity = Vector(*velocity)
        self.display_size = max(
            math.log(self.mass, self.display_log_base),
            self.min_display_size,
        )
        '''
        Атрибут экземпляра display_size в методе  __init__() выбирает между 
        рассчитанным размером маркера и установленным минимальным размером маркера. 
        Чтобы определить размер отображения тела в этом проекте, используем его массу.
        
        The display_size instance attribute in the __init__() method chooses between
        the calculated marker size and the set minimum marker size.
        To determine the display size of the body in this project, use its mass.
        '''
        self.colour = "orange"
        self.solar_system.add_body(self)
    '''
    solar_system позволяет вам связать тело с Солнечной системой. Аргумент должен быть типа SolarSystem.
    mass– это целое число или число с плавающей точкой, которое определяет массу тела. 
    position – это точка в трёхмерном пространстве, определяющая положение тела. 
    Это кортеж, содержащий x-, y- и z-координаты точки. По умолчанию используется исходное значение.
    velocity определяет скорость тела. Поскольку скорость движущегося тела имеет величину и направление, 
    она должна быть вектором. Хотя аргумент, необходимый при создании экземпляра SolarSystemBody , 
    является кортежем, вы можете преобразовать кортеж в векторный объект, присвоив ему атрибут self.velocity
    
    solar_system allows you to associate a body with the solar system. The argument must be of type SolarSystem.
    mass is an integer or floating point number that specifies the mass of the body.
    position is a point in 3D space that defines the position of the body.
    This is a tuple containing the x-, y-, and z-coordinates of the point. The default is the original value.
    velocity determines the speed of the body. Since the speed of a moving body has magnitude and direction,
    it must be a vector. Although the argument required when creating an instance of SolarSystemBody ,
    is a tuple, you can convert the tuple to a vector object by giving it the self.velocity attribute
    '''
    def move(self):
        self.position = (
            self.position[0] + self.velocity[0],
            self.position[1] + self.velocity[1],
            self.position[2] + self.velocity[2],
        )
    '''
    Метод move() переопределяет атрибут position на основе атрибута velocity. 
    
    The move() method overrides the position attribute based on the velocity attribute.
    '''
    def draw(self):
        self.solar_system.ax.plot(
            *self.position,
            marker="o",
            markersize=self.display_size + self.position[0] / 30,
            color=self.colour
        )
    def accelerate_due_to_gravity(self, other):
        '''
        accelerate_due_to_gravity() вызывается для объекта типа SolarSystemBody
        и нуждается в другом теле SolarSystemBody в качестве аргумента.
        Параметры self и other представляют два тела, взаимодействующих друг с другом

        accelerate_due_to_gravity() is called on an object of type SolarSystemBody
        and needs another SolarSystemBody as an argument.
        The parameters self and other represent two bodies interacting with each other
        '''
        distance = Vector(*other.position) - Vector(*self.position)
        distance_mag = distance.get_magnitude()
        force_mag = self.mass * other.mass / (distance_mag ** 2)
        force = distance.normalize() * force_mag
        reverse = 1
        for body in self, other:
            acceleration = force / body.mass
            body.velocity += acceleration * reverse
            reverse = -1
class Sun(SolarSystemBody):
    def __init__(
        self,
        solar_system,
        mass=10000,
        position=(0, 0, 0),
        velocity=(0, 0, 0),
    ):
        super(Sun, self).__init__(solar_system, mass, position, velocity)
        self.colour = "yellow"

class Planet(SolarSystemBody):
    colours = itertools.cycle([(1, 0, 0), (0, 1, 0), (0, 0, 1)])
    def __init__(
        self,
        solar_system,
        mass=10,
        position=(0, 0, 0),
        velocity=(0, 0, 0),
    ):
        super(Planet, self).__init__(solar_system, mass, position, velocity)
        self.colour = next(Planet.colours)