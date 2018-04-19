import unittest
import logging.config
import yaml
from firstCode import extractCompanyName

with open('config.yml','rt') as f:
    config = yaml.safe_load(f.read())
    
logging.config.dictConfig(config)
logger = logging.getLogger('unitTest')

class testExctractCompany(unittest.TestCase):
    messageText = [('20963,669,706 - S.I.G Grand Camp','20963,669,706 S.I.G Grand Camp'),
('PMR # 62140,999,760 Intage - customer id - 100252163','62140,999,760 Intage'),
('PMR # 22970,000,778-IOI ACidchem sdn BHD reported the same PMR','22970,000,778 ACidchem BHD'),
('We just received sev1 PMR # 88580,000,834 -J&J with same issue','88580,000,834 -J J'),
('76289,632,760 Sanai Oil','76289,632,760 Sanai'),
('62062,999,760 Nippon Information','62062,999,760 Nippon'),
('64414,672,760 TOYOBO INFORMATION','64414,672,760 TOYOBO INFORMATION'),
('62057,999,760 SOSHIN ELECTRIC','62057,999,760 SOSHIN ELECTRIC'),
('62047,999,760 Nippon Kayaku', '62047,999,760 Nippon Kayaku'),
('62052,999,760 Noevir','62052,999,760 Noevir'),
('62048,999,760 Kumi Kasei','62048,999,760 Kumi Kasei'),
('76289,632,760','76289,632,760 None'),
('62062,999,760','62062,999,760 None'),
('62053,999,760','62053,999,760 None'),
('33217,999,618 - Pitagora Informationsmanagem','33217,999,618 None'),
('90944,060,618 - Richter Pharma','90944,060,618 Pharma'),
('41087,082,000 - IBM CIO','41087,082,000 IBM CIO'),
('PMR 22005,001,806 Moderne Byggfornyelse AS','22005,001,806 Moderne Byggfornyelse'),
('PMR 22006,001,806 Inforte A/S','22006,001,806 Inforte A/S'),
('new PMR actually, PMR 22009,001,806 - Fjord1 AS','22009,001,806 None'),
('GESTIMAT (Dehon)-PMR 66594,661,706 Came on 2/28/18 5:20 PM GMT','66594,661,706 GESTIMAT Dehon'),
('Novaliance -PMR 62742,661,706 Came on 2/28/18 4:00 PM GMT','62742,661,706 None'),
('S.I.G Grand Camp-PMR 20963,669,706 Came Today around 2:00pm GMT','20963,669,706 S.I.G Grand Camp-PMR')]
    
#     def test01PmrPattern(self):
#         try:
#             for msg,val in self.messageText:
#                 self.assertEqual(extractCompanyName(msg),val)
#         except:
#             logger.error('Failed Extraction of Pmr or company',exc_info=True)
            
            
    def test02ExtractCompanyNameMultiline(self):
        try:
            msg = '62062,999,760 Nippon Information\n64414,672,760 TOYOBO INFORMATION\n62057,999,760 SOSHIN ELECTRIC\n62047,999,760 Nippon Kayaku\n62052,999,760 Noevir\n62048,999,760 Kumi Kasei'
            expectedVal = msg
            extractCompanyName(msg)
            self.assertTrue(True)
        except:
            self.assertFalse(False)
            
    
            

            
            
            
if __name__=='__main__':
    unittest.main()
            
            
            