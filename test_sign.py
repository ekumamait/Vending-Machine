import unittest
from signup import SignUp

class SignUpTest(unittest.TestCase):
    def setUp(self):
        self.signup = SignUp()

    def tearDown(self):
        pass    

    def test_signup_creation(self):
        self.assertIsInstance(self.signup, SignUp)

    def test_add_user(self):
        self.signup.add("jane doe","incorrect")
        self.assertEqual(len(self.signup.user_bio), 1)

    def test_return_password(self):
        self.signup.add("jane", "12345")
        self.assertEqual(self.signup.get_password("jane"), '12345')  

    def test_missing_key(self):
        with self.assertRaises(KeyError):
            self.signup.get_password("jone")

    def test_user_value(self):
        self.signup.add("jane", "12345")
        self.signup.add("james", "8765")
        self.signup.add("jim", "123")
        self.assertEqual(self.signup.get_user_bio(), 3)        

    @unittest.skip("WIP")
    def test_unknown_method(self):
        self.assertEqual(self.signup.some_method(), 1)