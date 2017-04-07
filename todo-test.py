import unittest
from todo import Database

class Testtodo(unittest.TestCase):

    def test_open_db(self):
        db = Database()
        # db.open_db()
        self.assertEqual(db.open_db(
            'todo-db.txt', 'r'), 
        
            [[1, '0', 'Walk the dog'],
             [2, '1', 'Buy milk'], 
             [3, '1', 'Do homework']])

if __name__ == '__main__':
    unittest.main()







    # def test_view(self):
    #     db = Database()
    #     self.assertEqual(db.view()," 1 [ ] ['Walk the dog']\n 2 [X] ['Buy milk']\n 3 [X] ['Do homework'] \n")
