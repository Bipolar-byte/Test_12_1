import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

# Я думаю не стоит обяснять что это код по заданию
    # class RunnerTest(unittest.TestCase):
    #    def test_walk(self):
    #
    #        runner = Runner("Test Walker")
    #
    #        for _ in range(10):
    #            runner.walk()
    #
    #        self.assertEqual(runner.distance, 50)
    #
    #    def test_run(self):
    #
    #        runner = Runner("Test Runner")
    #
    #        for _ in range(10):
    #            runner.run()
    #
    #       self.assertEqual(runner.distance, 100)
    #
    #    def test_challenge(self):
    #        runner1 = Runner("Runner1")
    #       runner2 = Runner("Runner2")
    #
    #       for _ in range(10):
    #            runner1.run()
    #            runner2.walk()
    #
    #       self.assertNotEqual(runner1.distance, runner2.distance)
    #
    # а ЭТО КОД с ОШИБКОЙ!!!!!
    
    class RunnerTest(unittest.TestCase):
        def test_walk(self):
            runner = Runner("Test Walker")

            for _ in range(10):
                runner.walk()

            self.assertEqual(runner.distance, 40)

        def test_run(self):
            runner = Runner("Test Runner")

            for _ in range(10):
                runner.run()

            self.assertEqual(runner.distance, 100)

        def test_challenge(self):
            runner1 = Runner("Runner1")
            runner2 = Runner("Runner2")

            for _ in range(10):
                runner1.run()
                runner2.walk()

            self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()
