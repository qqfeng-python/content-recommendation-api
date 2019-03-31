from main import app
import json
from unittest import TestCase


class TestIntegrations(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_summary_related(self):
        response = self.app.post('/summary-related', json={
            "article_url": "http://www.physiciansnewsnetwork.com/ximed/study-hospital-physician-vertical-integration-has-little-impact-on-quality/article_257c41a0-3a11-11e9-952b-97cc981efd76.html",
            "user_id": 1,
            "processor_id": "language-processor-health"
        })

        self.assertEqual(response.status_code,
                         200)

        response = json.loads(response.data)

        self.assertGreater(len(response["related"]),
                           2)

    def test_explore(self):
        response = self.app.post('/explore', json={
            "article_url": "https://www.health.harvard.edu/blog/conflict-of-interest-in-medicine-2018100114940",
            "user_id": 1,
            "processor_id": "language-processor-health"
        })

        self.assertEqual(response.status_code,
                         200)

        response = json.loads(response.data)

        self.assertGreater(len(response["related"]),
                           2)

    def test_summary(self):
        response = self.app.post('/summary', json={
            "article_url": "https://www.health.harvard.edu/blog/conflict-of-interest-in-medicine-2018100114940",
            "user_id": 1,
            "processor_id": "language-processor-health"
        })

        self.assertEqual(response.status_code,
                         200)

        response = json.loads(response.data)

        self.assertGreater(len(response['initial'][0]["summary"].split()), 80)
