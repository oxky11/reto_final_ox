import unittest
from flask import json
from app import create_app, db
from app.models import Data


class TestDataRoutes(unittest.TestCase):

    def setUp(self):
        """Configuración antes de cada test."""
        self.app = create_app("development")
        self.client = self.app.test_client()
        self.app.testing = True

        with self.app.app_context():
            db.create_all()
            db.session.commit()

    def tearDown(self):
        """Limpieza después de cada test."""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_insert_data_success(self):
        """Probar la inserción de datos (POST)"""
        self.setUp()
        new_data = {"name": "New Data"}
        response = self.client.post('/data', json=new_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Data inserted successfully", response.get_data(as_text=True))
        self.tearDown()


    def test_insert_data_conflict(self):
        """Probar la inserción de datos cuando ya existe (POST)"""
        self.setUp()
        existing_data = {"name": "Existing Data"}

        with self.app.app_context():
            db.session.add(Data(name="Existing Data"))
            db.session.commit()

        response = self.client.post('/data', json=existing_data)
        self.assertEqual(response.status_code, 409)
        self.assertIn("Data already exists", response.get_data(as_text=True))
        self.tearDown()

    def test_get_all_data(self):
        """Probar la obtención de todos los datos (GET)"""
        self.setUp()
        with self.app.app_context():
            db.session.add(Data(name="Item 1"))
            db.session.add(Data(name="Item 2"))
            db.session.commit()

        response = self.client.get('/data')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['name'], "Item 1")
        self.assertEqual(data[1]['name'], "Item 2")
        self.tearDown()

    def test_delete_data_not_found(self):
        """Probar la eliminación de datos cuando no se encuentra el item (DELETE)"""
        self.setUp()
        response = self.client.delete('/data/999')  # ID que no existe
        self.assertEqual(response.status_code, 404)
        self.assertIn("Data not found", response.get_data(as_text=True))
        self.tearDown()

if __name__ == '__main__':
    unittest.main()