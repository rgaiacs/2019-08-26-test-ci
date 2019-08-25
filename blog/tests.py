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

    def test_post_client(self):
        url_path = '/blog/welcome/'
        response = c.get(url_path)
        self.assertEqual(
            response.status_code,
            404,
            "when accessing {}".format(url_path)
        )

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
