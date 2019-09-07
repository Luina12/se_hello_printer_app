import unittest
from hello_world import app
from hello_world.formater import SUPPORTED

XML_EXP = "<greetings><name>Bartosz</name><msg>Hello World!</msg></greetings>"


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        ','.join(SUPPORTED) in rv.data

    def test_msg_with_output(self):
        rv = self.app.get('/?output=json')
        self.assertEquals('{ "imie":"Alicja", "mgs":"Hello World!"}', rv.data)

    def test_msg_with_name(self):
        imie = 'Alicja'
        rv = self.app.get('/?imie=' + imie + '&output=PLAIN')
        self.assertEquals('{ "imie":"Alicja", "mgs":"Hello World!"}', rv.data)
