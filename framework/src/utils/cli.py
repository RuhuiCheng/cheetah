import subprocess
import logging
logger = logging.getLogger(__name__)

def run(cmd):
    logger.info('cmd {0}'.format(cmd))
    subprocess.call(cmd, shell=True)

def check_run(cmd):
    logger.info('cmd {0}'.format(cmd))
    subprocess.check_call(cmd, shell=True)