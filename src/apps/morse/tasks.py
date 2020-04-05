import string
from celery import shared_task
import logging

logger = logging.getLogger(__name__)

@shared_task
def queue_messege(msg):
    print("This Morse Code Messege added to Queue ... \n msg={}".format(msg))
    logger.log("added to Queue ... \n msg={}".format(msg))
    pass