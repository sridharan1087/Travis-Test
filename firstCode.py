import nltk
import logging.config
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import yaml,re,traceback

with open('config.yml','rt') as f:
    config = yaml.safe_load(f.read())
    
logging.config.dictConfig(config)
logger = logging.getLogger('unitTest')


# def name(firstName):
#     logging.info('running the firstCode {}'.format(firstName))
#     return(firstName)

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

#             if lst:
#                 companyName = (" ".join(lst))
#             else:
#                 companyName = None
#             print 'Company name: %s  pmrId: %s' % (companyName,pmrId)
#             return('{} {}'.format(pmrId,companyName))
#     except:
#             print 'Exception: %s' % (traceback.format_exc())
            
            
extractCompanyName('S.I.G Grand Camp-PMR 20963,665,706 Came Today around 2:00pm GMT')        
#extractCompanyName('62062,999,760 Nippon Information\n64414,672,760 TOYOBO INFORMATION\n62057,999,760 SOSHIN ELECTRIC\n62047,999,760 Nippon Kayaku\n62052,999,760 Noevir\n62048,999,760 Kumi Kasei')

    