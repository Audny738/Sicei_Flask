from unittest import TestCase
import app


class TestApi(TestCase):

    _get_all_alumnos_mock_return = { "alumnos": [
        {"nombre": "Desiree Correa", "matricula": "16004107"},
        {"nombre": "Jane Doe", "matricula": "140053173"},
        {"nombre": "John Doe", "matricula": "170004317"},
    ]}
    
    
    def test_get_alumnos(self):
        response = app.get_alumnos()
        self.assertEquals(response, self._get_all_alumnos_mock_return)





