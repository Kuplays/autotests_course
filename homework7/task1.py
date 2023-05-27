# Напишите класс Segment
# Для его инициализации нужно два кортежа с координатами точек (x1, y1), (x2, y2)
# Реализуйте методы классы:
# 1. length, который возвращает длину нашего отрезка, с округлением до 2 знаков после запятой
# 2. x_axis_intersection, который возвращает True, если отрезок пересекает ось абцисс, иначе False
# 3. y_axis_intersection, который возвращает True, если отрезок пересекает ось ординат, иначе False
# Например (Ввод --> Вывод) :
# Segment((2, 3), (4, 5)).length() --> 2.83
# Segment((-2, -3), (4, 5)).x_axis_intersection() --> True
# Segment((-2, -3), (4, -5)).y_axis_intersection() --> False

# Здесь пишем код

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ

class Segment:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def length(self):
        """
        Возвращает длину отрезка до 2 знаков после запятой
        :return: длина отрезка по формуле корень((x2 - x1)^2 + (y2- y1)^2)
        """

        x_axis_part_square = pow((self.end_point[0] - self.start_point[0]), 2)
        y_axis_part_square = pow((self.end_point[1] - self.start_point[1]), 2)

        return round(pow(x_axis_part_square + y_axis_part_square, 0.5), 2)

    def x_axis_intersection(self):
        """
        Определяет пересечение отрезком координатной оси Х
        :return: True если y1y2 < 0, иначе False
        """

        return self.start_point[1] * self.end_point[1] < 0

    def y_axis_intersection(self):
        """
        Определяет пересечение отрезком координатной оси Y
        :return: True если x1x2 < 0, иначе False
        """

        return self.start_point[0] * self.end_point[0] < 0
        

data = [Segment((2, 3), (4, 5)).length,
        Segment((1, 1), (1, 8)).length,
        Segment((0, 0), (0, 1)).length,
        Segment((15, 1), (18, 8)).length,
        Segment((-2, -3), (4, 5)).x_axis_intersection,
        Segment((-2, -3), (-4, -2)).x_axis_intersection,
        Segment((0, -3), (4, 5)).x_axis_intersection,
        Segment((2, 3), (4, 5)).y_axis_intersection,
        Segment((-2, -3), (4, 5)).y_axis_intersection,
        Segment((-2, 3), (4, 0)).y_axis_intersection
        ]


test_data = [2.83, 7.0, 1.0, 7.62, True, False, True, False, True, True]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')