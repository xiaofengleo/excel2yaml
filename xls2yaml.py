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



columns = input('please input the columns you want to grab contents from,\n currently only one column is grabbed per run.\n')
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
               },
            'infrastructure':
               {'acronym':'foo',
                'name':'foo',
                'website':'foo',
                'domain':['foo','foo'],#list
                'URL/IRI of dataset':'foo',
                'URL of discovery portal':'foo'
               },
            'repositories':
               {'URL':'foo',
                 'name':'foo',
                 'kind':'foo',
                 'system':'foo',
                 'landingpage':'foo',
                 'assigned':'foo',
                 'provider':'foo',
                 'include_metadata':'foo',
                 'certification':['foo','foo'],
                 'policies':['foo','foo'],
                 'registries':['foo','foo'],
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
                    'data_license_in_use':'foo',
                    'data_license_iri':'foo',
                    'metadata_openly':'foo'
                     }
                },#end repository
           'data':
               {  'type_name':'foo',
                   'format_name':'foo',
                   'metadata_types_in':['foo','foo'],
                   'registered_data':['foo','foo'],
                   'search_on_data':'foo'
                },#end data
           'metadata':
               {'schema':['foo','foo'],
                'URL':'foo',
                'name':'foo',
                'provenance_fields':['foo','foo'],
                'machine_readable':'foo',
                'categories_defined':'foo',
                'PIDs_included':'foo',
                'primary_storage':'foo',
                'export_format':'foo'
                },#end metadata
           'search_engine':'foo',
           'exchange':'foo',
           'local_search':'foo',
           'external_search':'foo',
           'access_policy':'foo',
           'metadata_longevity':'foo',
           'machine_actionable': 'foo',
           'IRI_of_machine': 'foo',
           'vocabularies':# list
               {
               'IRI': 'foo',
               'name': 'foo',      
               'type': 'foo',
               'topic': 'foo',
               'specification language': 'foo'
                },#end vocabulary
            'data_management_plans':
                {'specific_DMO_tools': 'foo',
                 'data_publishing':['foo','foo'],
                 'compliance': 'foo'
                 },#end data management
            'data processing':
                {'special_data':['foo','foo'],
             'workflow': ['foo','foo'],
                 'distributed_workflows': ['foo','foo'],
                 'other_analysis':['foo','foo'],
                 'data_products':['foo','foo']
                 },#end data processing
            'fairness':
               {'data_findability': 
                    {'data_findable':'foo',
                    'gaps': ['foo','foo']
                     },
                'data_accessibility': 
                    {'data_accessible':'foo',
                     'gaps':['foo','foo']
                     },
                'data_interoperability': 
                     {'data_interoperable':'foo',
                      'gaps':['foo','foo']
                      },
                'data_re-usability': 
                     {'data_reusable':'foo',
                       'gaps':['foo','foo'] 
                     }
              }#end fairness
        }#end survey
     }#end data


#by setting hearder = 1, we skip the first row
excelContent = pd.read_excel ('atmosphere.xlsx','ACTRIS',header = 1, encoding =sys.getfilesystemencoding()) 
df = pd.DataFrame(excelContent)


for col in colNumHeads:   
    data['survey']['date'] = df.iat[0,col]# 0 starts from the row the 'date' is on
    data['survey']['version'] = df.iat[1,col]
    data['survey']['creator']['name'] = df.iat[2,col]
    data['survey']['creator']['email'] = df.iat[3,col]
    data['survey']['infrastructure']['acronym'] = df.iat[4,col]
    data['survey']['infrastructure']['name'] = df.iat[5,col]
    data['survey']['infrastructure']['website'] = df.iat[6,col]
    data['survey']['infrastructure']['domain'] = df.iat[7,col]
    data['survey']['infrastructure']['URL/IRI of dataset'] = df.iat[8,col]
    data['survey']['infrastructure']['URL of discovery portal'] = df.iat[9,col]
               
    data['survey']['repositories']['URL'] = df.iat[10,col]
    data['survey']['repositories']['name'] = df.iat[11,col]
    data['survey']['repositories']['kind'] = df.iat[12,col]
    data['survey']['repositories']['system'] = df.iat[19,col]#??
    data['survey']['repositories']['landingpage'] = df.iat[20,col]
    data['survey']['repositories']['assigned'] = df.iat[21,col]
    data['survey']['repositories']['provider'] = df.iat[22,col]
    data['survey']['repositories']['include_metadata'] = df.iat[23,col]
    data['survey']['repositories']['certification'] = df.iat[24,col]
    data['survey']['repositories']['policies'] = df.iat[25,col]
    data['survey']['repositories']['registries'] = df.iat[26,col]
    data['survey']['repositories']['persistency'] = df.iat[27,col]
    data['survey']['repositories']['access_mechanism']['authentication'] = df.iat[28,col]
    data['survey']['repositories']['access_mechanism']['access_protocol'] = df.iat[29,col]
    data['survey']['repositories']['access_mechanism']['access_without'] = df.iat[30,col]
    data['survey']['repositories']['access_mechanism']['own_user_database'] = df.iat[31,col]
    data['survey']['repositories']['access_mechanism']['ORCID'] = df.iat[32,col]
    data['survey']['repositories']['access_mechanism']['major_access'] = df.iat[33,col]
    data['survey']['repositories']['access_mechanism']['authorization'] = df.iat[34,col]
    data['survey']['repositories']['access_mechanism']['authorization_for_accessing_content'] = df.iat[35,col]
    data['survey']['repositories']['access_mechanism']['data_license_in_use'] = df.iat[36,col]
    data['survey']['repositories']['access_mechanism']['data_license_iri'] = df.iat[37,col]
    data['survey']['repositories']['access_mechanism']['metadata_openly'] = df.iat[38,col]

    data['survey']['data']['type_name'] = df.iat[39,col]
    data['survey']['data']['format_name'] = df.iat[40,col]
    data['survey']['data']['metadata_types_in'] = df.iat[41,col]
    data['survey']['data']['registered_data'] = df.iat[42,col]
    data['survey']['data']['search_on_data'] = df.iat[43,col]


    #data['survey']['metadata']['schema'] = df.iat[43,col]
    data['survey']['metadata']['URL'] = df.iat[45,col]
    data['survey']['metadata']['name'] = df.iat[46,col]
    data['survey']['metadata']['provenance_fields'] = df.iat[47,col]
    data['survey']['metadata']['machine_readable'] = df.iat[48,col]
    data['survey']['metadata']['categories_defined'] = df.iat[49,col]
    data['survey']['metadata']['PIDs_included'] = df.iat[50,col]
    data['survey']['metadata']['primary_storage'] = df.iat[51,col]
    data['survey']['metadata']['export_format'] = df.iat[52,col]

    data['survey']['search_engine'] = df.iat[54,col]
    data['survey']['exchange'] = df.iat[55,col]
    data['survey']['local_search'] = df.iat[56,col]
    data['survey']['external_search'] = df.iat[57,col]
    data['survey']['access_policy'] = df.iat[58,col]
    data['survey']['metadata_longevity'] = df.iat[59,col]
    data['survey']['machine_actionable'] = df.iat[60,col]
    data['survey']['IRI_of_machine'] = df.iat[61,col]

    data['survey']['vocabularies']['IRI'] = df.iat[65,col]
    data['survey']['vocabularies']['name'] =df.iat[66,col]
    data['survey']['vocabularies']['type'] = df.iat[67,col]
    data['survey']['vocabularies']['topic'] = df.iat[68,col]
    data['survey']['vocabularies']['specification language'] = df.iat[70,col]


    data['survey']['data_management_plans']['specific_DMO_tools'] =  df.iat[71,col]
    data['survey']['data_management_plans']['data_publishing'] = df.iat[72,col]
    data['survey']['data_management_plans']['compliance'] = df.iat[73,col]


    data['survey']['data processing']['special_data'] = df.iat[74,col]
    data['survey']['data processing']['workflow'] = df.iat[75,col]
    data['survey']['data processing']['distributed_workflows'] = df.iat[76,col]
    data['survey']['data processing']['other_analysis'] = df.iat[77,col]
    data['survey']['data processing']['data_products'] = df.iat[78,col]

    data['survey']['fairness']['data_findability']['data_findable'] = df.iat[79,col]
    data['survey']['fairness']['data_findability']['gaps'] = df.iat[80,col]

    data['survey']['fairness']['data_accessibility']['data_accessible'] = df.iat[81,col]
    data['survey']['fairness']['data_accessibility']['gaps'] = df.iat[82,col]
            
    data['survey']['fairness']['data_interoperability']['data_interoperable'] = df.iat[83,col]
    data['survey']['fairness']['data_interoperability']['gaps'] = df.iat[84,col]

    data['survey']['fairness']['data_re-usability']['data_reusable'] = df.iat[85,col]
    data['survey']['fairness']['data_re-usability']['gaps'] = df.iat[86,col]

print(data)




outfile = open('data.txt','w',encoding = sys.getfilesystemencoding())
yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True, sort_keys=False)

