# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 13:19:44 2017

@author: Sahir Noor Ali

@Code: Tone Analyzer

@Pre-Req: Make sure that the WDC SDK is installed before the code is executed.
          The following command on the command prompt will ensure it:
              
              pip install --upgrade watson-developer-cloud
              
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#--------------------------------------------------------------
#Imports
#--------------------------------------------------------------

#The ToneAnalyzer class from WDC
from watson_developer_cloud import ToneAnalyzerV3

#Pandas for data handling
import pandas as pd

#Time class to measure the time taken
import time
#--------------------------------------------------------------

#Read the data
data = pd.read_csv('Reviews.csv')

#Make a copy of 100 rows for smaller testing
small_data = data.head(100).copy()

#To view the documentation
#print(help(ToneAnalyzerV3))

#-------------------------------------------------------------------------
#Instantiate TA Object with your Credentials
#-------------------------------------------------------------------------
tone_analyzer = ToneAnalyzerV3(
    username='ABC',
    password='XYZ',
    version='2016-05-19',
    url = 'https://gateway.watsonplatform.net/tone-analyzer/api')
#-------------------------------------------------------------------------

#Get the current time on the clock
time_start = time.clock()

#------------------------------------------------------------------------
#Iterate Over All the Reviews and Append the Result:
#------------------------------------------------------------------------    
for index, review in small_data['Text'].iteritems():
    
    #Pass a single review to TA (one by one):
    json_output = tone_analyzer.tone(review, content_type='text/plain')    
    
    #Traverse the heirarchy of result
    for i in json_output['document_tone']['tone_categories']:
        for j in i['tones']:
            #Append the attributes to the data
            small_data.set_value(index, j['tone_name'], j['score']) 
#------------------------------------------------------------------------

#Get the current time again and subract from 
#previous to measure the time taken        
time_end = time.clock() - time_start

#Print the time taken
print(time_end)

#Save the enriched data to another CSV File
small_data.to_csv('OutputTA.csv')

