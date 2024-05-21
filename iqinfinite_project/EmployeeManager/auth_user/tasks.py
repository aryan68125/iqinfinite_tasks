from __future__ import absolute_import , unicode_literals
from celery import shared_task
from celery.utils.log import get_task_logger
from auth_user.send_email import *
@shared_task(name='add')
def add(x, y):
    return x + y
logger  = get_task_logger(__name__)
@shared_task(name="send_email_task")
def send_email_task(subject, message, EMAIL_HOST_USER, recipient_list):
    logger.info("Mail sent")
    return send_email(subject, message, EMAIL_HOST_USER, recipient_list)
