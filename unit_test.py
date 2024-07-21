import unittest
from math import pi
from calculate.main import Circle, Triangle, Rectangle, calculate_area


class TestFigures(unittest.TestCase):
    def test_circle_area(self):
        """Тест вычисления площади круга."""
        circle = Circle(3)
        self.assertAlmostEqual(circle.area_figure(), pi * 3**2)

    def test_circle_invalid_radius(self):
        """Тест на ввод неверного значения радиуса круга."""
        with self.assertRaises(ValueError):
            Circle(0)

    def test_triangle_area(self):
        """Тест вычисления площади треугольника."""
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area_figure(), 6)

    def test_triangle_invalid_sides(self):
        """Тест на проверку является ли фигура треугольником."""
        with self.assertRaises(ValueError):
            Triangle(1, 1, 3)

    def test_right_triangle(self):
        """Тест на проверку является ли треугольник прямоугольным."""
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.right_triangle())

    def test_calculate_area_circle(self):
        """Тест вычисления площади круга."""
        self.assertAlmostEqual(calculate_area(3), pi * 3**2)

    def test_calculate_area_rectangle(self):
        """Тест ошибки на вычисления площади по двум сторонам, без указания класса."""
        with self.assertRaises(NotImplementedError):
            calculate_area(1, 2)

    def test_calculate_area_triangle(self):
        """Тест вычисления площади по трем сторонам, без указания класса."""
        self.assertAlmostEqual(calculate_area(3, 4, 5), 6)

    def test_calculate_area_invalid(self):
        """Тест ошибки на неизвестную фигуру."""
        with self.assertRaises(NotImplementedError):
            calculate_area(1, 2, 3, 4)


if __name__ == "__main__":
    unittest.main()
