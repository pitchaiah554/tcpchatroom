import unittest
from chat_client import Client

class TestChatRoom(unittest.TestCase):
     def setUp(self):
         self.cl = Client()

     def test_connection(self):
         self.assertEqual(self.cl.create_connection(), 'connected')


if __name__ == '__main__':
    unittest.main()