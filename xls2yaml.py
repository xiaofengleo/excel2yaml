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



columns = input('please input the columns you want to grab contents from,\n each column separated by a comma, \n Both captial and small letters are fine. \n Like F,I \n')
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
        {  'date': 'yyyy-mm-dd',
           'version': 1.0,
            'creator':
               {'name': 'foo',
                'email':'foo'
               },#end creator
            'infrastructure':
               {'acronym':'foo',
                'name':'foo',
                'website':'foo',
                'domain':['foo','foo'],#list
                'URL/IRI of dataset':'foo',
                'URL of discovery portal':'foo'
               },#end infrastructure
            'repositories':[],#end repository
           'data':
               {  'type_name':[],
                   'format_name':'foo',
                   'metadata_types_in':[],
                   'registered_data':[],
                   'search_on_data':'foo'
                },#end data
           'metadata':
               {'schema':[],
                'URL':'foo',
                'name':'foo',
                'provenance_fields':[],
                'machine_readable':'foo',
                'categories_defined':'foo',
                'PIDs_included':'foo',
                'primary_storage':'foo',
                'export_format':[]
                },#end metadata
           'search_engine':'foo',
           'exchange':[],
           'local_search':'foo',
           'external_search':[],
           'access_policy':'foo',
           'metadata_longevity':'foo',
           'machine_actionable': 'foo',
           'IRI_of_machine': 'foo',
           'vocabularies':[],# list
            'data_management_plans':
                {'specific_DMO_tools': 'foo',
                 'data_publishing':[],
                 'compliance': 'foo'
                 },#end data management
            'data processing':
                {'special_data':[],
             'workflow': [],
                 'distributed_workflows': [],
                 'other_analysis':[],
                 'data_products':[]
                 },#end data processing
            'fairness':
               {'data_findability': 
                    {'data_findable':'foo',
                    'gaps': []
                     },
                'data_accessibility': 
                    {'data_accessible':'foo',
                     'gaps':[]
                     },
                'data_interoperability': 
                     {'data_interoperable':'foo',
                      'gaps':[]
                      },
                'data_re-usability': 
                     {'data_reusable':'foo',
                       'gaps':[] 
                     }
              }#end fairness
        }#end survey
     }#end data


#by setting hearder = 1, we skip the first row
excelContent = pd.read_excel ('atmosphere.xlsx','ACTRIS',header = 1, encoding =sys.getfilesystemencoding()) 
df = pd.DataFrame(excelContent)


for col in colNumHeads:   
    data['survey']['date'] = df.iat[0,col]# 0 corresponding to the 3rd row in the excel sheet
    data['survey']['version'] = df.iat[1,col]
    data['survey']['creator']['name'] = df.iat[2,col]
    data['survey']['creator']['email'] = df.iat[3,col]
    data['survey']['infrastructure']['acronym'] = df.iat[4,col]
    data['survey']['infrastructure']['name'] = df.iat[5,col]
    data['survey']['infrastructure']['website'] = df.iat[6,col]
    data['survey']['infrastructure']['domain'] = df.iat[7,col]
    data['survey']['infrastructure']['URL/IRI of dataset'] = df.iat[8,col]
    data['survey']['infrastructure']['URL of discovery portal'] = df.iat[9,col]
    
    repository = {'URL':'foo',
                 'name':'foo',
                 'kind':[],
                 'system':'foo',
                 'landingpage':'foo',
                 'assigned':'foo',
                 'provider':'foo',
                 'include_metadata':[],
                 'certification':[],
                 'policies':[],
                 'registries':[],
                 'persistency':'foo',
                 'access_mechanism':
                   {'authentication':'foo',
                    'access_protocol':'foo',
                    'access_without':'foo',
                    'own_user_database':'foo',
                    'ORCID':'foo',
                    'major-access':'foo',
                    'authorization':'foo',
                    'authorization_for_accessing_content':'foo',
                    'data_license_in_use':[],
                    'data_license_iri':[],
                    'metadata_openly':'foo'
                     }
                }
    repository['URL'] = df.iat[10,col]
    repository['name'] = df.iat[11,col]
    repository['kind'].append(df.iat[12,col])
    repository['system'] = df.iat[19,col]#??
    repository['landingpage'] = df.iat[20,col]
    repository['assigned'] = df.iat[21,col]
    repository['provider'] = df.iat[22,col]
    repository['include_metadata'].append(df.iat[23,col])
    repository['certification'].append(df.iat[24,col])
    repository['policies'] .append(df.iat[25,col])
    repository['registries'].append(df.iat[26,col])
    repository['persistency'] = df.iat[27,col]
    repository['access_mechanism']['authentication'] = df.iat[28,col]
    repository['access_mechanism']['access_protocol'] = df.iat[29,col]
    repository['access_mechanism']['access_without'] = df.iat[30,col]
    repository['access_mechanism']['own_user_database'] = df.iat[31,col]
    repository['access_mechanism']['ORCID'] = df.iat[32,col]
    repository['access_mechanism']['major_access'] = df.iat[33,col]
    repository['access_mechanism']['authorization'] = df.iat[34,col]
    repository['access_mechanism']['authorization_for_accessing_content'] = df.iat[35,col]
    repository['access_mechanism']['data_license_in_use'].append(df.iat[36,col])
    repository['access_mechanism']['data_license_iri'].append(df.iat[37,col])
    repository['access_mechanism']['metadata_openly'] = df.iat[38,col]
    data['survey']['repositories'].append(repository)

    data['survey']['data']['type_name'].append(df.iat[39,col])
    data['survey']['data']['format_name'] = df.iat[40,col]
    data['survey']['data']['metadata_types_in'].append(df.iat[41,col])
    data['survey']['data']['registered_data'].append(df.iat[42,col])
    data['survey']['data']['search_on_data'] = df.iat[43,col]


    #data['survey']['metadata']['schema'] = df.iat[43,col]
    data['survey']['metadata']['URL'] = df.iat[45,col]
    data['survey']['metadata']['name'] = df.iat[46,col]
    data['survey']['metadata']['provenance_fields'].append(df.iat[47,col])
    data['survey']['metadata']['machine_readable'] = df.iat[48,col]
    data['survey']['metadata']['categories_defined'] = df.iat[49,col]
    data['survey']['metadata']['PIDs_included'] = df.iat[50,col]
    data['survey']['metadata']['primary_storage'] = df.iat[51,col]
    data['survey']['metadata']['export_format'].append(df.iat[52,col])

    data['survey']['search_engine'] = df.iat[54,col]
    data['survey']['exchange'].append(df.iat[55,col])
    data['survey']['local_search'] = df.iat[56,col]
    data['survey']['external_search'].append(df.iat[57,col])
    data['survey']['access_policy'] = df.iat[58,col]
    data['survey']['metadata_longevity'] = df.iat[59,col]
    data['survey']['machine_actionable'] = df.iat[60,col]
    data['survey']['IRI_of_machine'] = df.iat[61,col]

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
    data['survey']['vocabularies'].append(vocabulary)

    data['survey']['data_management_plans']['specific_DMO_tools'] =  df.iat[71,col]
    data['survey']['data_management_plans']['data_publishing'].append(df.iat[72,col])
    data['survey']['data_management_plans']['compliance'] = df.iat[73,col]


    data['survey']['data processing']['special_data'].append(df.iat[74,col])
    data['survey']['data processing']['workflow'].append(df.iat[75,col])
    data['survey']['data processing']['distributed_workflows'].append(df.iat[76,col])
    data['survey']['data processing']['other_analysis'].append(df.iat[77,col])
    data['survey']['data processing']['data_products'].append(df.iat[78,col])

    data['survey']['fairness']['data_findability']['data_findable'] = df.iat[79,col]
    data['survey']['fairness']['data_findability']['gaps'].append(df.iat[80,col])

    data['survey']['fairness']['data_accessibility']['data_accessible'] = df.iat[81,col]
    data['survey']['fairness']['data_accessibility']['gaps'].append(df.iat[82,col])
            
    data['survey']['fairness']['data_interoperability']['data_interoperable'] = df.iat[83,col]
    data['survey']['fairness']['data_interoperability']['gaps'].append(df.iat[84,col])

    data['survey']['fairness']['data_re-usability']['data_reusable'] = df.iat[85,col]
    data['survey']['fairness']['data_re-usability']['gaps'].append(df.iat[86,col])

#print(data)




outfile = open('data.txt','w',encoding = sys.getfilesystemencoding())
yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True, sort_keys=False)

