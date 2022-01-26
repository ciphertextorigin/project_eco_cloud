import unittest
import app as tested_app
import json


class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        tested_app.app.config['TESTING'] = True
        self.app = tested_app.app.test_client()

    def test_home(self):
        r = self.app.get('/')
        self.assertEqual(r.data, b'Welcome to My Favourite Tree API')
        self.assertEqual(r.status_code, 200)

    def test_get_favourite_tree(self):
        r = self.app.get('/tree')
        # import pdb; pdb.set_trace()
        print(r.data)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.mimetype, 'application/json')
    


if __name__ == '__main__':
    unittest.main()