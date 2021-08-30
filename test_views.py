from src import create_app
from src import views
from unittest.mock import patch
import unittest
import json

class VisitTest(unittest.TestCase):

    app = create_app(True)

    def test_visits_api(self):
        tester = VisitTest.app.test_client(self)
        response = tester.get('/visits/page/1')
        status_code = response.status_code
        self.assertEqual(status_code, 200)

    @patch('src.views.get_visit_data')
    def test_visits_api_data(self, mock_function):
        """
        mocking return value of the Visit Single Record, 
        thus it won't be depending upon database
        """
        mock_function.return_value= {
            'id': 1,
            'start_date': 'Mon, 31 Aug 2021 10:10:10 GMT',
            'end_date': 'Mon, 01 Sep 2021 11:10:10 GMT',
            'instructions': 'test'
        }
        tester = VisitTest.app.test_client(self)
        response = tester.get('/visit/1')
        actual = json.loads(response.data)
        expected_data = {
            'end_date': 'Mon, 01 Sep 2021 11:10:10 GMT', 
            'id': 1, 
            'instructions': 'test', 
            'start_date': 'Mon, 31 Aug 2021 10:10:10 GMT'
        }
        self.assertEqual(expected_data, actual)

if __name__ == "__main__":
    unittest.main()