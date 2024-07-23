import unittest
from geometry.shapes import Circle, Triangle, calculate_area

class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.53981633974483)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0)

    def test_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.right_triangle_checking())

    def test_not_right_triangle(self):
        triangle = Triangle(3, 4, 6)
        self.assertFalse(triangle.right_triangle_checking())

    def test_calculate_area_circle(self):
        circle = Circle(5)
        self.assertAlmostEqual(calculate_area(circle), 78.53981633974483)

    def test_calculate_area_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(calculate_area(triangle), 6.0)

if __name__ == "__main__":
    unittest.main()
