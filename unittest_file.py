import unittest

class TestStringMethods(unittest.TestCase):
    """Unit tests for basic string operations."""

    def test_upper(self):
        """Test conversion to uppercase."""
        self.assertEqual('prasad'.upper(), 'PRASAD')

    def test_isupper(self):
        """Test uppercase string validation."""
        self.assertTrue('PRASAD'.isupper())
        self.assertFalse('prasad'.isupper())

    def test_split(self):
        """Test string splitting behavior."""
        text = 'Optimal XAI'
        self.assertEqual(text.split(), ['Optimal', 'XAI'])
        with self.assertRaises(TypeError):
            text.split(2)

if __name__ == '__main__':
    unittest.main(verbosity=2)
