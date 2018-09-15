import unittest
from app import db
from app.models import Posts,User,Comments

class UserModelTest(unittest.TestCase):

  

    def setUp(self):
        self.new_user = User(user_name='dennis',email='dennisveer27@gmail.com',password_secure='12345')

    def test_password_setter(self):
        self.assertTrue(self.new_user.password_secure is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):

            self.new_user.password

    
    def save_account(self):
        db.session.add(self.new_user)
        db.session.commit()
        self.asserTrue(len(user.id) > 0)

    
if __name__ == '__main__':
    unittest.main()
