#!/usr/bin/python3
"""
Unit Test for BaseModel Class
"""
import unittest
from datetime import datetime
import models
import json
import os

User = models.user.User
BaseModel = models.base_model.BaseModel
FileStorage = models.file_storage.FileStorage
storage = models.storage
F = './dev/file.json'


class TestFileStorageDocs(unittest.TestCase):
    """Class for testing BaseModel docs"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('..... For FileStorage Class .....')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        expected = ("\nHandles I/O, writing and reading, of JSON for storage "
                    "of all class instances\n")
        actual = models.file_storage.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """... documentation for the class"""
        expected = 'handles long term storage of all class instances'
        actual = FileStorage.__doc__
        self.assertEqual(expected, actual)

    def test_doc_init(self):
        """... documentation for init function"""
        expected = 'instantiation of new FileStorage class instance'
        actual = FileStorage.__init__.__doc__
        self.assertEqual(expected, actual)

    def test_doc_all(self):
        """... documentation for all function"""
        expected = 'returns private attribute: __objects'
        actual = FileStorage.all.__doc__
        self.assertEqual(expected, actual)

    def test_doc_new(self):
        """... documentation for new function"""
        expected = ("sets / updates in __objects the obj with key <obj class "
                    "name>.id")
        actual = FileStorage.new.__doc__
        self.assertEqual(expected, actual)

    def test_doc_save(self):
        """... documentation for save function"""
        expected = 'serializes __objects to the JSON file (path: __file_path)'
        actual = FileStorage.save.__doc__
        self.assertEqual(expected, actual)

    def test_doc_reload(self):
        """... documentation for reload function"""
        expected = ("if file exists, deserializes JSON file to __objects, "
                    "else nothing")
        actual = FileStorage.reload.__doc__
        self.assertEqual(expected, actual)


class TestBmFsInstances(unittest.TestCase):
    """testing for class instances"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('...... Testing FileStorate ......')
        print('..... For FileStorage Class .....')
        print('.................................\n\n')

    def test_instantiation(self):
        """... checks proper FileStorage instantiation"""
        bm_obj = FileStorage()
        self.assertIsInstance(bm_obj, FileStorage)

    def test_storage_file_exists(self):
        """... checks proper FileStorage instantiation"""
        os.remove(F)
        bm_obj = BaseModel()
        bm_obj.save()
        self.assertTrue(os.path.isfile(F))

    def test_all(self):
        """... checks if all() function returns newly created instance"""
        bm_obj = BaseModel()
        bm_id = bm_obj.id
        all_obj = storage.all()
        actual = 0
        for k in all_obj.keys():
            if bm_id in k:
                actual = 1
        self.assertTrue(1 == actual)

    def test_obj_saved_to_file(self):
        """... checks proper FileStorage instantiation"""
        os.remove(F)
        bm_obj = BaseModel()
        bm_obj.save()
        bm_id = bm_obj.id
        actual = 0
        with open(F, mode='r', encoding='utf-8') as f_obj:
            storage_dict = json.load(f_obj)
        for k in storage_dict.keys():
            if bm_id in k:
                actual = 1
        self.assertTrue(1 == actual)

    def test_to_json(self):
        """... to_json should return serializable dict object"""
        my_model = BaseModel()
        my_model_json = my_model.to_json()
        actual = 1
        try:
            serialized = json.dumps(my_model_json)
        except:
            actual = 0
        self.assertTrue(1 == actual)

    def test_reload(self):
        """... checks proper usage of reload function"""
        os.remove(F)
        bm_obj = BaseModel()
        bm_obj.save()
        bm_id = bm_obj.id
        actual = 0
        new_storage = FileStorage()
        new_storage.reload()
        all_obj = new_storage.all()
        for k in all_obj.keys():
            if bm_id in k:
                actual = 1
        self.assertTrue(1 == actual)

    def test_save_reload_class(self):
        """... checks proper usage of class attribute in file storage"""
        os.remove(F)
        bm_obj = BaseModel()
        bm_obj.save()
        bm_id = bm_obj.id
        actual = 0
        new_storage = FileStorage()
        new_storage.reload()
        all_obj = new_storage.all()
        for k, v in all_obj.items():
            if bm_id in k:
                if type(v).__name__ == 'BaseModel':
                    actual = 1
        self.assertTrue(1 == actual)


class TestUserFsInstances(unittest.TestCase):
    """testing for class instances"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('...... Testing FileStorage ......')
        print('.......... User  Class ..........')
        print('.................................\n\n')

    def test_storage_file_exists(self):
        """... checks proper FileStorage instantiation"""
        os.remove(F)
        u_obj = User()
        u_obj.save()
        self.assertTrue(os.path.isfile(F))

    def test_all(self):
        """... checks if all() function returns newly created instance"""
        u_obj = User()
        u_id = u_obj.id
        all_obj = storage.all()
        actual = 0
        for k in all_obj.keys():
            if u_id in k:
                actual = 1
        self.assertTrue(1 == actual)

    def test_obj_saved_to_file(self):
        """... checks proper FileStorage instantiation"""
        os.remove(F)
        u_obj = User()
        u_obj.save()
        u_id = u_obj.id
        actual = 0
        with open(F, mode='r', encoding='utf-8') as f_obj:
            storage_dict = json.load(f_obj)
        for k in storage_dict.keys():
            if u_id in k:
                actual = 1
        self.assertTrue(1 == actual)

    def test_reload(self):
        """... checks proper usage of reload function"""
        os.remove(F)
        u_obj = BaseModel()
        u_obj.save()
        u_id = u_obj.id
        actual = 0
        new_storage = FileStorage()
        new_storage.reload()
        all_obj = new_storage.all()
        for k in all_obj.keys():
            if u_id in k:
                actual = 1
        self.assertTrue(1 == actual)


if __name__ == '__main__':
    unittest.main
