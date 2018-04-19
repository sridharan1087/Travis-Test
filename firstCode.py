import nltk
import logging.config
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import yaml,re,traceback

with open('config.yml','rt') as f:
    config = yaml.safe_load(f.read())
    
logging.config.dictConfig(config)
logger = logging.getLogger('unitTest')


def messageProcessing(message,pattern,stopWords):
    try:
        pmrId = re.search(pattern,message)
        if pmrId is not None:
            tokenization = word_tokenize(message)
            filterWords = [w for w in tokenization if not w in stopWords]
            posTag = nltk.pos_tag(filterWords)
            lst = [i for i,j in posTag if j=='NNP']
            logger.info('companyName {}'.format(' '.join(lst)))
            lst = []
        else:
            logger.error('Cannot Extract PMR ID',exc_info = True)
    except Exception as e:
        logger.error('Error {}'.format(e),exc_info=True)


def extractCompanyName(message):
    logger.info('Extracting company name from messages')
    try:
        if message:
            pattern = '\d{5}.\d{3}.\d{3}'
            stopWords = stopwords.words('english')
            stopWords.extend(['Came','PM', 'GMT','PMR','-PMR','Today'])
            if "\n" or "\t" in message:
                messages = message.split('\n')
                for msg in messages:
                    messageProcessing(msg, pattern, stopWords)
            else:
                messageProcessing(message, pattern, stopWords)
        return(True)


    except Exception as e:
        print('Exception',e)
        return(False)


    
