# Python Week Of Code, Namibia 2019

Django’s unit tests use Python's unittest,
the same library that we use in the previous section.

## Task for Instructor

1. Add

   ```
   from django.test import TestCase, Client

   from .models import Post

   c = Client()

   # Create your tests here.
   class PostTestCase(TestCase):
       def setUp(self):
           post = Post.objects.create(
               title="Welcome",
               text="This is your first website."
           )

       def test_index_client(self):
           response = c.get('/')
           self.assertEqual(
               response.status_code,
               200
           )
   ```

   to [blog/tests.py](blog/tests.py).
2. Run

   ```
   python manage.py test
   ```
3. Change the function `test_index_client()` to

   ```
       def test_index_client(self):
           url_path = '/'
           response = c.get(url_path)
           self.assertEqual(
               response.status_code,
               200,
               "when accessing {}".format(url_path)
           )
           self.assertEqual(
               response.context['posts'],
               [],
               "when accessing {}".format(url_path)
           )
   ```

   in [blog/tests.py](blog/tests.py).
4. Run

   ```
   python manage.py test
   ```
5. Add the following function

   ```
       def test_post_client(self):
           url_path = '/blog/welcome/'
           response = c.get(url_path)
           self.assertEqual(
               response.status_code,
               404,
               "when accessing {}".format(url_path)
           )
   ```

   to [blog/tests.py](blog/tests.py).
6. Run

   ```
   python manage.py test
   ```
7. Add the following function

   ```
       def test_post_form_client(self):
           url_path = '/blog/'
           response = c.get(url_path)
           self.assertEqual(
               response.status_code,
               200,
               "when accessing {}".format(url_path)
           )
   ```

   to [blog/tests.py](blog/tests.py).
   And run

   ```
   python manage.py test
   ```
8. Change the function `test_index_client()` to

   ```
       def test_post_form_client(self):
           url_path = '/blog/'
           response = c.get(url_path)
           self.assertEqual(
               response.status_code,
               200,
               "when accessing {}".format(url_path)
           )
           response = c.post(
               url_path,
               {
                   'title': "Testing your website",
                   'text': "Write tests is import to avoid unhappy users",
               }
           )
           self.assertEqual(
               response.status_code,
               200,
               "when posting to {}".format(url_path)
           )
   ```

   in [blog/tests.py](blog/tests.py).
   And run

   ```
   python manage.py test
   ```
9. Change the function `test_index_client()` to

   ```
       def test_post_form_client(self):
           url_path = '/blog/'
           response = c.get(url_path)
           self.assertEqual(
               response.status_code,
               200,
               "when accessing {}".format(url_path)
           )
           response = c.post(
               url_path,
               {
                   'title': "Testing your website",
                   'text': "Write tests is import to avoid unhappy users",
               }
           )
           self.assertRedirects(
               response,
               '/blog/Testing%20your%20website/',
               msg_prefix="when posting to {}".format(url_path)
           )
   ```

   in [blog/tests.py](blog/tests.py).
   And run

   ```
   python manage.py test
   ```

## Tasks for Learners

1. Fix the website so that all tests pass.