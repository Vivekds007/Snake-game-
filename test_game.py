import unittest
from game import Game

class TestSnakeGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_initial_conditions(self):
        self.assertEqual(self.game.points, 0)
        self.assertEqual(self.game.points_to_beat, 0)
        self.assertEqual(len(self.game.segments), 0)
        self.assertEqual(self.game.delay, 0.1)
        self.assertEqual(self.game.head.direction, "stop")

    def test_food_collision(self):
        self.game.head.goto(self.game.food.position())
        result = self.game.check_collisions()
        self.assertEqual(result, "food")
        self.assertEqual(self.game.points, 10)
        self.assertEqual(len(self.game.segments), 1)
    
    def test_border_collision(self):
        self.game.head.goto(300, 300)
        result = self.game.check_collisions()
        self.assertEqual(result, "border")
        self.assertEqual(self.game.points, 0)
        self.assertEqual(len(self.game.segments), 0)
        self.assertEqual(self.game.head.position(), (0, 0))
    
    def test_self_collision(self):
        segment = self.game.create_turtle("circle", "black", self.game.head.position())
        self.game.segments.append(segment)
        result = self.game.check_collisions()
        self.assertEqual(result, "self")
        self.assertEqual(self.game.points, 0)
        self.assertEqual(len(self.game.segments), 0)
        self.assertEqual(self.game.head.position(), (0, 0))

if __name__ == '__main__':
    unittest.main()
