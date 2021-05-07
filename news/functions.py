import requests

from django_q.tasks import async_task
from django_q.models import Failure

from .models import Webhook


def post_endpoint(article):
    endpoint = Webhook.objects.values_list('endpoint', flat=True).get(id=article.webhook.id)
    response = requests.get(endpoint)

    return response


def check_result(task):
    if task.result.status_code is not requests.codes.ok:
        task.success = False
        task.save()


def task_post_webhook(article):
    opts = {
        'task_name': f'{article}',
        'group': f'{article.webhook.name}',
        'hook': 'news.functions.check_result',
    }
    async_task('news.functions.post_endpoint', article, q_options=opts)


def retry_fail_task():
    """Submit fail tasks back to the queue."""
    queryset = Failure.objects.all()
    for task in queryset:
        opts = {
            'task_name': f'{task.name}',
            'group': f'{task.group}',
            'hook': f'{task.hook}',
        }
        async_task(task.func, *task.args or (), q_options=opts, **task.kwargs or {})
        task.delete()
