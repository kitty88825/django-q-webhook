import requests

from django_q.tasks import async_task

from .models import Article


def task_session_hook(article):
    async_task(
        'news.functions.post_endpoint',
        article,
        task_name=f'POST {article}',
        hook='news.functions.check_hook_status',
        group=f'{article.webhook.name}',
    )


def post_endpoint(article):
    response = requests.get(article.webhook.endpoint)
    return response

def check_hook_status(task):
    if task.success:
        pass
