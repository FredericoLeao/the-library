from rest_framework.test import APITestCase


class TestLibraryAPI(APITestCase):
    def test_books_api(self):
        # create authors
        author_data = {'name': 'Robert C. Martin'}
        res = self.client.post('/api/authors/', author_data)
        self.assertEqual(res.status_code, 201)
        author_data = {'name': 'Carlo Rovelli'}
        res = self.client.post('/api/authors/', author_data)
        author_data = {'name': 'Sidarta Ribeiro'}
        res = self.client.post('/api/authors/', author_data)
        author_data = {'name': 'Jules Verne'}
        res = self.client.post('/api/authors/', author_data)
        # list authors
        res = self.client.get('/api/authors/')
        self.assertEqual(len(res.json()), 4)
        # retrieve author
        anyauthor_id = res.json()[0]['id']
        someauthor_id = res.json()[1]['id'] # for later use
        otherauthor_id = res.json()[2]['id'] # for later use
        res = self.client.get(f'/api/authors/{anyauthor_id}/')
        self.assertEqual(res.json()['id'], anyauthor_id)
        # delete author
        res = self.client.delete(f'/api/authors/{anyauthor_id}/')
        self.assertEqual(res.status_code, 204)
        res = self.client.get('/api/authors/')
        self.assertEqual(len(res.json()), 3)
        # update author
        author_update = {'name': 'José Eduardo Agualusa'}
        res = self.client.put(f'/api/authors/{someauthor_id}/', author_update)
        self.assertEqual(res.json()['name'], 'José Eduardo Agualusa')


        # create categories
        category_data = {'name': 'Software Engineering'}
        res = self.client.post('/api/categories/', category_data)
        self.assertEqual(res.status_code, 201)
        category_data = {'name': 'Astronomy'}
        res = self.client.post('/api/categories/', category_data)
        category_data = {'name': 'Science Fiction'}
        res = self.client.post('/api/categories/', category_data)
        category_data = {'name': 'Computing History'}
        res = self.client.post('/api/categories/', category_data)
        category_data = {'name': 'Time And Relative Dimension in Space'}
        res = self.client.post('/api/categories/', category_data)
        # list categories
        res = self.client.get('/api/categories/')
        self.assertEqual(len(res.json()), 5)
        # retrieve category
        anycategory_id = res.json()[0]['id'] 
        somecategory_id = res.json()[1]['id'] # for later use
        othercategory_id = res.json()[2]['id'] # for later use
        res = self.client.get(f'/api/categories/{anycategory_id}/')
        self.assertEqual(res.json()['id'], anycategory_id)
        # delete category
        res = self.client.delete(f'/api/categories/{anycategory_id}/')
        self.assertEqual(res.status_code, 204)
        res = self.client.get('/api/categories/')
        self.assertEqual(len(res.json()), 4)
        # update category
        category_update = {'name': 'Economics'}
        res = self.client.put(f'/api/categories/{somecategory_id}/', category_update)
        self.assertEqual(res.json()['name'], 'Economics')

        # create books
        image_base64 = (
            'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z/C/HgAGgwJ/lK3Q6wAAAABJRU5ErkJggg==')
        book_data = {
            'name': 'Clean Code',
            'authors': [someauthor_id],
            'categories': [somecategory_id],
            'cover': image_base64
        }
        res = self.client.post('/api/books/', book_data)
        self.assertEqual(res.status_code, 201)
        book_data = {
            'name': 'The Oracle of Night',
            'authors': [someauthor_id],
            'categories': [somecategory_id],
        }
        self.client.post('/api/books/', book_data)
        book_data = {
            'name': 'Journey To The Center of The Earth',
            'authors': [otherauthor_id],
            'categories': [othercategory_id],
            'isbn': '978-85-943-1815-2'
        }
        self.client.post('/api/books/', book_data)
        # list books
        res = self.client.get('/api/books/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.json()), 3)
        anybook_id = res.json()[0]['id']
        somebook_id = res.json()[1]['id']
        otherbook_id = res.json()[2]['id']
        # retrieve book
        res = self.client.get(f'/api/books/{anybook_id}/')
        self.assertEqual(res.json()['id'], anybook_id)
        # delete book
        res = self.client.delete(f'/api/books/{anybook_id}/')
        self.assertEqual(res.status_code, 204)
        res = self.client.get('/api/books/')
        self.assertEqual(len(res.json()), 2)
        # update book
        patch_book = {
            'description': 'adding description for some book...'
        }
        res = self.client.patch(f'/api/books/{somebook_id}/', patch_book)
        self.assertEqual(res.json()['description'],
                         'adding description for some book...')
        # update book with new image
        patch_book = {
            'cover': 'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mO8f19+DwAHHQKbe6hzCQAAAABJRU5ErkJggg=='
        }
        res = self.client.patch(f'/api/books/{otherbook_id}/', patch_book)
        self.assertTrue('.png' in res.json()['cover'])
