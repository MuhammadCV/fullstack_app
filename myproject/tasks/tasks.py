# myproject/tasks/tasks.py

from celery import Celery, shared_task
from django.core.mail import send_mail
import logging

app = Celery('tasks', broker='redis://127.0.0.1:6379/0', backend='redis://127.0.0.1:6379/0')

logger = logging.getLogger(__name__)

@shared_task(bind=True)
def send_task_notification(self, task_title):
    try:
        # Prepare the email content
        subject = 'New Task Created'
        message = f"A new task has been created: {task_title}"
        recipient_list = ['boboevm832000@gmail.com']  # Replace with recipient's email address

        # Send the email
        send_mail(subject, message, 'unistar20172010@gmail.com', recipient_list)

        logger.info(f"Email sent successfully for task: {task_title}")
        return f"Notification sent for task: {task_title}"
    except Exception as e:
        logger.error(f"Error sending notification for task {task_title}: {e}")
        self.retry(exc=e)
