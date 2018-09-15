import unittest
from app import db
from app.models import Posts,User,Comments

class PostModelTest(unittest.TestCase):


   
        
    def setUp(self):
        self.user_denno = User(user_name = "denno", password="banana")
        self.new_post = Posts(title='a',post='b',category='d',posts=self.user_denno)
       

    def test_instance(self):
        self.assertEqual(self.new_post.title,'a')
        self.assertEqual(self.new_post.post,'b')
        self.assertEqual(self.new_post.category,'d')
    
    def test_save_post(self):
        self.new_post.save_post()
        self.assertTrue(len(Posts.query.all())>0)
    
    def test_get_post_by_id(self):

        self.new_post.save_post()
        got_post = Posts.get_post(1)
        self.assertTrue(len(got_post) > 0)


if __name__ == '__main__':
    unittest.main()
