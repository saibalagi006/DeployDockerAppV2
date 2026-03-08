import unittest
from main import app, menu

class TestMain(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home_route_status(self):
        """Test that the home route returns a 200 status code."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_route_content(self):
        """Test that the home route renders the menu correctly."""
        response = self.app.get('/')
        self.assertIn(b'South Indian Food Menu', response.data)
        # Check for a few menu items
        self.assertIn(b'Idli', response.data)
        self.assertIn(b'Dosa', response.data)
        self.assertIn(b'Sambar', response.data)

    def test_menu_data_structure(self):
        """Test that the menu data is a list of dictionaries with expected keys."""
        self.assertIsInstance(menu, list)
        self.assertGreater(len(menu), 0)
        for item in menu:
            self.assertIn('name', item)
            self.assertIn('ingredients', item)
            self.assertIsInstance(item['name'], str)
            self.assertIsInstance(item['ingredients'], list)

    def test_menu_items_count(self):
        """Test that the menu has the expected number of items."""
        self.assertEqual(len(menu), 7)  # Based on the hardcoded menu