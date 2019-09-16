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


#by setting hearder = 1, we skip the first row
excelContent = pd.read_excel ('actris.xlsx','ACTRIS',header = 0, encoding =sys.getfilesystemencoding()) 
df = pd.DataFrame(excelContent)

print(df.iat[0,0])
print(df.iat[1,0])
print(df.iat[2,0])
print(df.iat[3,0])
print(df.iat[4,0])
print(df.iat[5,0])
print(df.iat[6,0])
print()
print(df.iat[0,3])
print(df.iat[1,3])
print(df.iat[2,3])
print(df.iat[3,3])
print(df.iat[4,3])
print(df.iat[5,3])

print(df.columns)


my_itr = iter(colNumHeads)

for col in colNumHeads:
    print(col)
    nextcol = colNumHeads[colNumHeads.index(col)-len(colNumHeads)+1]
    print(col, nextcol)
    print(df.iat[0,col])
    print(df.iat[1,col])
    data['survey']['date'] = df.iat[0,col]# 0 corresponding to the 3rd row in the excel sheet
    data['survey']['version'] = df.iat[1,col]
    data['survey']['creator']['name'] = df.iat[2,col]
    data['survey']['creator']['email'] = df.iat[3,col]
    data['infrastructure']['acronym'] = df.iat[4,col]
    data['infrastructure']['name'] = df.iat[5,col]
    data['infrastructure']['website'] = df.iat[6,col]
    data['infrastructure']['domain'] = df.iat[7,col]
    data['infrastructure']['URL/IRI of dataset'] = df.iat[8,col]
    data['infrastructure']['URL of discovery portal'] = df.iat[9,col]
    
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
    repository['URL'] = df.iat[10,col]
    repository['name'] = df.iat[11,col]
    if(col< nextcol):
        for index in range(col,nextcol):
            repository['kind'].append(df.iat[12,index])
    repository['allocation'] = df.iat[13,col]
    if(col< nextcol):
        for index in range(col,nextcol):
            repository['software'].append(df.iat[15,index])
    one_indentifier = {'kind':'foo',
                    'system':'foo',
                    'landing page':'foo',
                    'assigned':'foo',
                    'provider':'foo',
                    'includes metadata schema':[]
                     }
    one_indentifier['kind'] = df.iat[17,col]#??
    one_indentifier['system'] = df.iat[19,col]#??
    one_indentifier['landing page'] = df.iat[20,col]
    one_indentifier['assigned'] = df.iat[21,col]
    one_indentifier['provider'] = df.iat[22,col]
    if(col< nextcol):
        for index in range(col,nextcol):
            one_indentifier['includes metadata schema'].append(df.iat[23,index])
    repository['identifier'].append(one_indentifier)
    if(col< nextcol):
        for index in range(col,nextcol):
            repository['certification methods'].append(df.iat[24,index])
            print(df.iat[24,index])
            repository['policies'].append(df.iat[25,index])
            print(df.iat[25,index])
            repository['registries'].append(df.iat[26,index])
    #print(repository)        
    repository['persistency-guaranty'] = df.iat[27,col]
    repository['access mechanisms']['authentication method'] = df.iat[28,col]
    repository['access mechanisms']['access protocol URL'] = df.iat[29,col]
    repository['access mechanisms']['access without costs'] = df.iat[30,col]
    repository['access mechanisms']['own user database maintained'] = df.iat[31,col]
    repository['access mechanisms']['person identification system'] = df.iat[32,col]
    repository['access mechanisms']['major access technology supported'] = df.iat[33,col]
    repository['access mechanisms']['authorization technique'] = df.iat[34,col]
    repository['access mechanisms']['authorization for accessing content needed'] = df.iat[35,col]
    if(col< nextcol):
        for index in range(col,nextcol):
            repository['access mechanisms']['data licenses in use'].append(df.iat[36,index])
    repository['access mechanisms']['data license IRI'] = df.iat[37,col]
    repository['access mechanisms']['metadata openly available'] = df.iat[38,col]

    one_preferredformat = {'format name':'foo',
                       'metadata types in data headers':[]
                   }
    one_data = {'type name':[],
                'preferred formats':[],
                'registered data schema':[],
                'search on data':'foo'
                }#end data
    
    one_preferredformat['format name'] = df.iat[40,col]
    if(col< nextcol):
        for index in range(col,nextcol):
            one_preferredformat['metadata types in data headers'].append(df.iat[41,index])

    if(col< nextcol):
        for index in range(col,nextcol):
            one_data['type name'].append(df.iat[39,index])
    one_data['preferred formats'].append(one_preferredformat)
    if(col< nextcol):
        for index in range(col,nextcol):
            one_data['registered data schema'].append(df.iat[42,index])
    one_data['search on data'] = df.iat[43,col]
    repository['data'].append(one_data)


    one_schema = {'URL':'foo',
                  'name':'foo',
                  'provenance fields included':[]
                }

    #data[ësurveyí]['metadata']['schema'] = df.iat[43,col]
    one_schema['URL'] = df.iat[45,col]
    one_schema['name'] = df.iat[46,col]
    if(col< nextcol):
        for index in range(col,nextcol):
            one_schema['provenance fields included'].append(df.iat[47,index])
    repository['metadata']['schema'].append(one_schema)
    repository['metadata']['machine readable provenance'] = df.iat[48,col]
    repository['metadata']['categories defined in registries'] = df.iat[49,col]
    repository['metadata']['PIDs included'] = df.iat[50,col]
    repository['metadata']['primary storage format'] = df.iat[51,col]
    if(col< nextcol):
        for index in range(col,nextcol):
            repository['metadata']['export formats supported'].append(df.iat[52,index])

    repository['metadata']['search engine indexing'] = df.iat[54,col]
    if(col< nextcol):
        for index in range(col,nextcol):
            repository['metadata']['exchange/harvesting methods'].append(df.iat[55,index])
    repository['metadata']['local search engine URL'] = df.iat[56,col]
    if(col< nextcol):
        for index in range(col,nextcol):
            repository['metadata']['external search engine types supported'].append(df.iat[57,index])
    repository['metadata']['access policy statements included'] = df.iat[58,col]
    repository['metadata']['metadata longevity plan URL'] = df.iat[59,col]
    repository['metadata']['machine actionable'] = df.iat[60,col]
    repository['metadata']['IRI of machine readable metadata of dataset'] = df.iat[61,col]

    vocabulary={
               'IRI': 'foo',
               'name': 'foo',      
               'type': 'foo',
               'topic': 'foo',
               'specification language': 'foo'
                }
    vocabulary['IRI'] = df.iat[65,col]
    vocabulary['name'] =df.iat[66,col]
    vocabulary['type'] = df.iat[67,col]
    vocabulary['topic'] = df.iat[68,col]
    vocabulary['specification language'] = df.iat[70,col]
    repository['vocabularies'].append(vocabulary)

    repository['data management plans']['specific DMP tools used'] =  df.iat[71,col]
    if(col< nextcol):
        for index in range(col,nextcol):
            repository['data management plans']['data publishing steps applied'].append(df.iat[72,index])
    repository['data management plans']['compliance validation service'] = df.iat[73,col]


    if(col< nextcol):
        for index in range(col,nextcol):
            repository['data processing']['special data processing steps applied'].append(df.iat[74,index])
            repository['data processing']['workflow frameworks applied'].append(df.iat[75,index])
            repository['data processing']['distributed workflows tools used'].append(df.iat[76,index])
            repository['data processing']['other analysis services offered'].append(df.iat[77,index])
            repository['data processing']['data products offered'].append(df.iat[78,index])

    repository['fairness']['data findability']['data findable'] = df.iat[79,col]
    if(col< nextcol):
        for index in range(col,nextcol):
            repository['fairness']['data findability']['gaps'].append(df.iat[80,index])

    repository['fairness']['data accessibility']['data accessible'] = df.iat[81,col]
    if(col< nextcol):
        for index in range(col,nextcol):
            repository['fairness']['data accessibility']['gaps'].append(df.iat[82,index])
            
    repository['fairness']['data interoperability']['data interoperable'] = df.iat[83,col]
    if(col< nextcol):
        for index in range(col,nextcol):
            repository['fairness']['data interoperability']['gaps'].append(df.iat[84,index])

    repository['fairness']['data re-usability']['data reusable'] = df.iat[85,col]
    if(col< nextcol):
        for index in range(col,nextcol):
            repository['fairness']['data re-usability']['gaps'].append(df.iat[86,index])
    #print(repository)
    data['infrastructure']['repositories'].append(repository)

print(data)

outfile = open('data.txt','w',encoding = sys.getfilesystemencoding())
yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True, sort_keys=False)
