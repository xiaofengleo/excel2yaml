##
## author: Xiaofeng Liao, Zhiming Zhao, Barbara Magagna
##         University of Amsterdam
## date: 22 Aug, 2019
##

##
import yaml
from pandas import *
import pandas as pd
import sys
from pandas import ExcelWriter
from pandas import ExcelFile
import io




#mapping from excel column to index
Letter2Number = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8,
                 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16,
                 'R':17,'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24,
                 'Z':25,'AA':26,'AB':27,'AC':28,'AD':29,'AE':30,'AF':31,'AG':32,
                 'AH':33,'AI':34,'AJ':35,'AK':36,'AL':37,'AM':38,'AN':39,'AO':40,
                 'AP':41,'AQ':42,'AR':43,'AS':44,'AT':45,'AU':46,'AV':47,'AW':48,
                 'AX':49,'AY':50,'AZ':51}



columns = input('please input the columns where each repository is,\n each column separated by a comma, \n Both captial and small letters are fine. \n Like F,I \n')
cols = columns.strip().split(',')
UCols = []
for col in cols:
    Ucol = col.strip().upper()
    UCols.append(Ucol)
#print(UCols)
colNumHeads = []
for col in UCols:
    colNumHeads.append(Letter2Number[col])
#print(colNumHeads)

#dictionary to hold the yaml structure


data = {'survey':
        {
        'date': 'yyyy-mm-dd',
         'version': 1.0,
         'creator':
               {'name': 'foo',
                'email':'foo'
               }#end creator
        },#end survey
        'infrastructure':
        {
        'acronym':'foo',
         'name':'foo',
         'website':'foo',
         'domain':[],#list
         'URL/IRI of dataset':'foo',
         'URL of discovery portal':'foo',
         'repositories':[]
        }#end infrastructure
     }#end


#hearder = 0, indicates the first row is header
excelContent = pd.read_excel ('actris.xlsx','ACTRIS',header = 0, encoding =sys.getfilesystemencoding()) 
df = pd.DataFrame(excelContent)


my_itr = iter(colNumHeads)

for col in colNumHeads:
    #print(col)
    nextcol = colNumHeads[colNumHeads.index(col)-len(colNumHeads)+1]
    #print(col, nextcol)
    if(col < nextcol):
        i = 0 #i indicatic the starting row, because some excel files starts at different rows
        print(df.iat[0,col])
        print(df.iat[1,col])
        data['survey']['date'] = df.iat[i+1,col]#
        data['survey']['version'] = df.iat[i+2,col]
        data['survey']['creator']['name'] = df.iat[i+3,col]
        data['survey']['creator']['email'] = df.iat[i+1+3,col]
        data['infrastructure']['acronym'] = df.iat[i+1+4,col]
        data['infrastructure']['name'] = df.iat[i+1+5,col]
        data['infrastructure']['website'] = df.iat[i+1+6,col]
        data['infrastructure']['domain'] = df.iat[i+1+7,col]
        data['infrastructure']['URL/IRI of dataset'] = df.iat[i+1+8,col]
        data['infrastructure']['URL of discovery portal'] = df.iat[i+1+9,col]
        
        #to fill in infrastructure, some inner dict inside it should be defined and filled first recursively
        

        repository = {'URL':'foo',
                     'name':'foo',
                     'kind':[],
                     'allocation':'foo',
                     'software':[],
                     'identifier':[],
                     'certification methods':[],
                     'policies':[],
                     'registries':[],
                     'persistency-guaranty':'foo', 
                     'access mechanisms':
                       {'authentication method':'foo',
                        'access protocol URL':'foo',
                        'access without costs':'foo',
                        'own user database maintained':'foo',
                        'person identification system':'foo',
                        'major access technology supported':'foo',
                        'authorization technique':'foo',
                        'authorization for accessing content needed':'foo',
                        'data licenses in use':[],
                        'data license IRI':'foo',
                        'metadata openly available':'foo'
                         },
                     'data':[],
                     'metadata':
                       {'schema':[],
                        'machine readable provenance':'foo',
                        'categories defined in registries':'foo',
                        'PIDs included':'foo',
                        'primary storage format':'foo',
                        'export formats supported':[],
                        'search engine indexing':'foo',
                        'exchange/harvesting methods':[],
                        'local search engine URL':'foo',
                        'external search engine types supported':[],
                        'access policy statements included':'foo',
                        'metadata longevity plan URL':'foo',
                        'machine actionable': 'foo',
                        'IRI of machine readable metadata of dataset': 'foo'
                        },#end metadata
                     'vocabularies':[],# list
                     'data management plans':
                         {'specific DMP tools used': 'foo',
                          'data publishing steps applied':[],
                          'compliance validation service': 'foo'
                         },#end data management
                     'data processing':
                         {'special data processing steps applied':[],
                          'workflow frameworks applied': [],
                          'distributed workflows tools used': [],
                          'other analysis services offered':[],
                          'data products offered':[]
                         },#end data processing
                     'fairness':
                         {'data findability': 
                           {'data findable':'foo',
                            'gaps': []
                            },
                          'data accessibility': 
                           {'data accessible':'foo',
                            'gaps':[]
                            },
                          'data interoperability': 
                           {'data interoperable':'foo',
                            'gaps':[]
                            },
                          'data re-usability': 
                           {'data reusable':'foo',
                            'gaps':[] 
                           }
                          }#end fairness
                    }#end repository
        repository['URL'] = df.iat[i+1+10,col]
        repository['name'] = df.iat[i+1+11,col]
        for index in range(col,nextcol):
            repository['kind'].append(df.iat[i+1+12,index])
        repository['allocation'] = df.iat[i+1+13,col]
        for index in range(col,nextcol):
            repository['software'].append(df.iat[i+1+15,index])
        one_indentifier = {'kind':'foo',
                        'system':'foo',
                        'landing page':'foo',
                        'assigned':'foo',
                        'provider':'foo',
                        'includes metadata schema':[]
                         }
        one_indentifier['kind'] = df.iat[i+1+17,col]#??
        one_indentifier['system'] = df.iat[i+1+19,col]#??
        one_indentifier['landing page'] = df.iat[i+1+20,col]
        one_indentifier['assigned'] = df.iat[i+1+21,col]
        one_indentifier['provider'] = df.iat[i+1+22,col]
        for index in range(col,nextcol):
            one_indentifier['includes metadata schema'].append(df.iat[i+1+23,index])
        repository['identifier'].append(one_indentifier)

        for index in range(col,nextcol):
            repository['certification methods'].append(df.iat[i+1+24,index])
            #print(df.iat[24,index])
            repository['policies'].append(df.iat[i+1+25,index])
            #print(df.iat[25,index])
            repository['registries'].append(df.iat[i+1+26,index])
        #print(repository)        
        repository['persistency-guaranty'] = df.iat[i+1+27,col]
        repository['access mechanisms']['authentication method'] = df.iat[i+1+28,col]
        repository['access mechanisms']['access protocol URL'] = df.iat[i+1+29,col]
        repository['access mechanisms']['access without costs'] = df.iat[i+1+30,col]
        repository['access mechanisms']['own user database maintained'] = df.iat[i+1+31,col]
        repository['access mechanisms']['person identification system'] = df.iat[i+1+32,col]
        repository['access mechanisms']['major access technology supported'] = df.iat[i+1+33,col]
        repository['access mechanisms']['authorization technique'] = df.iat[i+1+34,col]
        repository['access mechanisms']['authorization for accessing content needed'] = df.iat[i+1+35,col]
        for index in range(col,nextcol):
            repository['access mechanisms']['data licenses in use'].append(df.iat[i+1+36,index])
        repository['access mechanisms']['data license IRI'] = df.iat[i+1+37,col]
        repository['access mechanisms']['metadata openly available'] = df.iat[i+1+38,col]

        one_preferredformat = {'format name':'foo',
                           'metadata types in data headers':[]
                       }
        one_data = {'type name':[],
                    'preferred formats':[],
                    'registered data schema':[],
                    'search on data':'foo'
                    }#end data
        
        one_preferredformat['format name'] = df.iat[i+1+40,col]
        for index in range(col,nextcol):
            one_preferredformat['metadata types in data headers'].append(df.iat[i+1+41,index])

        for index in range(col,nextcol):
            one_data['type name'].append(df.iat[i+1+39,index])
        one_data['preferred formats'].append(one_preferredformat)
        for index in range(col,nextcol):
            one_data['registered data schema'].append(df.iat[i+1+42,index])
        one_data['search on data'] = df.iat[i+1+43,col]
        repository['data'].append(one_data)


        one_schema = {'URL':'foo',
                      'name':'foo',
                      'provenance fields included':[]
                    }

        #data[ësurveyí]['metadata']['schema'] = df.iat[43,col]
        one_schema['URL'] = df.iat[i+1+45,col]
        one_schema['name'] = df.iat[i+1+46,col]
        for index in range(col,nextcol):
            one_schema['provenance fields included'].append(df.iat[i+1+47,index])
        repository['metadata']['schema'].append(one_schema)
        repository['metadata']['machine readable provenance'] = df.iat[i+1+48,col]
        repository['metadata']['categories defined in registries'] = df.iat[i+1+49,col]
        repository['metadata']['PIDs included'] = df.iat[i+1+50,col]
        repository['metadata']['primary storage format'] = df.iat[i+1+51,col]
        for index in range(col,nextcol):
            repository['metadata']['export formats supported'].append(df.iat[i+1+52,index])

        repository['metadata']['search engine indexing'] = df.iat[i+1+54,col]
        for index in range(col,nextcol):
            repository['metadata']['exchange/harvesting methods'].append(df.iat[i+1+55,index])
        repository['metadata']['local search engine URL'] = df.iat[i+1+56,col]
        for index in range(col,nextcol):
            repository['metadata']['external search engine types supported'].append(df.iat[i+1+57,index])
        repository['metadata']['access policy statements included'] = df.iat[i+1+58,col]
        repository['metadata']['metadata longevity plan URL'] = df.iat[i+1+59,col]
        repository['metadata']['machine actionable'] = df.iat[i+1+60,col]
        repository['metadata']['IRI of machine readable metadata of dataset'] = df.iat[i+1+61,col]

        vocabulary={
                   'IRI': 'foo',
                   'name': 'foo',      
                   'type': 'foo',
                   'topic': 'foo',
                   'specification language': 'foo'
                    }
        vocabulary['IRI'] = df.iat[i+1+65,col]
        vocabulary['name'] =df.iat[i+1+66,col]
        vocabulary['type'] = df.iat[i+1+67,col]
        vocabulary['topic'] = df.iat[i+1+68,col]
        vocabulary['specification language'] = df.iat[i+1+70,col]
        repository['vocabularies'].append(vocabulary)

        repository['data management plans']['specific DMP tools used'] =  df.iat[i+1+71,col]
        for index in range(col,nextcol):
            repository['data management plans']['data publishing steps applied'].append(df.iat[i+1+72,index])
        repository['data management plans']['compliance validation service'] = df.iat[i+1+73,col]


        for index in range(col,nextcol):
            repository['data processing']['special data processing steps applied'].append(df.iat[i+1+74,index])
            repository['data processing']['workflow frameworks applied'].append(df.iat[i+1+75,index])
            repository['data processing']['distributed workflows tools used'].append(df.iat[i+1+76,index])
            repository['data processing']['other analysis services offered'].append(df.iat[i+1+77,index])
            repository['data processing']['data products offered'].append(df.iat[i+1+78,index])

        repository['fairness']['data findability']['data findable'] = df.iat[i+1+79,col]
        for index in range(col,nextcol):
            repository['fairness']['data findability']['gaps'].append(df.iat[i+1+80,index])

        repository['fairness']['data accessibility']['data accessible'] = df.iat[i+1+81,col]
        for index in range(col,nextcol):
            repository['fairness']['data accessibility']['gaps'].append(df.iat[i+1+82,index])
                
        repository['fairness']['data interoperability']['data interoperable'] = df.iat[i+1+83,col]
        for index in range(col,nextcol):
            repository['fairness']['data interoperability']['gaps'].append(df.iat[i+1+84,index])

        repository['fairness']['data re-usability']['data reusable'] = df.iat[i+1+85,col]
        for index in range(col,nextcol):
            repository['fairness']['data re-usability']['gaps'].append(df.iat[i+1+86,index])
        #print(repository)
        data['infrastructure']['repositories'].append(repository)

print(data)

outfile = open('data.txt','w',encoding = sys.getfilesystemencoding())
yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True, sort_keys=False)
