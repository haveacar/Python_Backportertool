import unittest
import os
from controls import Backporter, find_file_in_root_then_dirs


class TestControls(unittest.TestCase):

    def setUp(self):
        # Setup code for creating test files
        self.test_file_name = 'test_file.txt'
        with open(self.test_file_name, 'w') as file:
            file.write('Test line 1\nTest line 2\n')

        self.before_file = 'before_file.txt'
        self.after_file = 'after_file.txt'
        self.target_file = 'target_file.txt'

        with open(self.before_file, 'w') as file:
            file.write('Line 1\nLine 2\n')

        with open(self.after_file, 'w') as file:
            file.write('Line 1\nModified Line 2\n')

        with open(self.target_file, 'w') as file:
            file.write('Line 1\nLine 2\n')

    def test_find_file_in_root_then_dirs(self):
        found_path = find_file_in_root_then_dirs(self.test_file_name)
        self.assertIsNotNone(found_path)
        self.assertTrue(os.path.exists(found_path))

    def test_backporter_initialization(self):
        backporter = Backporter(self.before_file, self.after_file, self.target_file)
        self.assertIsNotNone(backporter)

    def test_read_file(self):
        backporter = Backporter(self.before_file, self.after_file, self.target_file)
        content = backporter._read_file(self.test_file_name)
        self.assertEqual(content, ['Test line 1\n', 'Test line 2\n'])

    def test_write_file(self):
        backporter = Backporter(self.before_file, self.after_file, self.target_file)
        test_data = ['Line 1\n', 'Line 2\n']
        output_file = 'output.txt'
        backporter.write_file(output_file, test_data)
        with open(output_file, 'r') as file:
            content = file.readlines()
        self.assertEqual(content, test_data)

    def test_event_logging(self):
        backporter = Backporter(self.before_file, self.after_file, self.target_file)
        backporter.event("Test Event")
        self.assertIn("Test Event", backporter._logs[-1])

    def tearDown(self):
        # Teardown code to remove test files
        os.remove(self.test_file_name)
        os.remove(self.before_file)
        os.remove(self.after_file)
        os.remove(self.target_file)
        if os.path.exists('output.txt'):
            os.remove('output.txt')


if __name__ == '__main__':
    unittest.main()
