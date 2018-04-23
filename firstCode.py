import nltk,random
import logging.config
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import yaml,re,traceback
from cassandra.cluster import Cluster
from cassandra.query import BatchStatement
from cassandra import ConsistencyLevel

with open('config.yml','rt') as f:
    config = yaml.safe_load(f.read())
    
logging.config.dictConfig(config)
logger = logging.getLogger('unitTest')

cluster = Cluster(['35.200.242.129'])
session = cluster.connect('incident')
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
            companyName = ' '.join(lst)
            return({'PmrId':message[pmrId.start():pmrId.end()],'companyName':companyName})    
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
            batch = BatchStatement(consistency_level=ConsistencyLevel.QUORUM)
            insertPmrAndCompanyCql = session.prepare('INSERT INTO incidentbot (id,number,customername,created_by,timestamp) VALUES (?, ?, ?, ?, ?)')
            stopWords.extend(['Came','PM', 'GMT','PMR','-PMR','Today'])
            if "\n" or "\t" in message:
                messages = message.split('\n')
                for msg in messages:
                    a = messageProcessing(msg, pattern, stopWords)
                    a['incidentId'] = random.randint(100000,200000)
                    a['createdBy'] = 'Ajay' 
                    a['time'] = 10
                    logger.info('Company Name and Pmr Id {}'.format(a))
                    try:
                        batch.add(insertPmrAndCompanyCql,(str(a['incidentId']),str(a['PmrId']),a['companyName'],a['createdBy'],str(a['time'])))
                        logging.info('Added in to batch INSERT')
                    except Exception as e:
                        logger.error(e,exc_info=True)
                session.execute(batch)
            else:
                messageProcessing(message, pattern, stopWords)
                session.execute('INSERT INTO incidentbot (id,number,customername,created_by,timestamp) VALUES (%s, %s, %s, %s, %s)',[str(a['incidentId']),str(a['PmrId']),a['companyName'],a['createdBy'],str(a['time'])])
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
            
            
#extractCompanyName('S.I.G Grand Camp-PMR 20963,665,706 Came Today around 2:00pm GMT')        
#extractCompanyName('62062,999,760 Nippon Information\n64414,672,760 TOYOBO INFORMATION\n62057,999,760 SOSHIN ELECTRIC\n62047,999,760 Nippon Kayaku\n62052,999,760 Noevir\n62048,999,760 Kumi Kasei')

    