import nltk
import logging

logging.basicConfig(format='(asctime)s (message)s (name)s',level=logging.DEBUG)
logger = logging.getLogger('firstCode')

def name(firstName):
    logging.info('running the firstCode {}'.format(firstName))
    return(firstName)

    