# -*- coding: utf-8 -*-

from odoo import models, fields, api
import requests
import logging
import json

_logger = logging.getLogger(__name__)

class cap_salesforce(models.Model):
    _name = 'cap_salesforce.cap_salesforce'
    _description = "Salesforce Synchronization"
    
    @api.model
    def connect_to_salesforce(self):
    #Get token from Salesforce
        url = 'https://login.salesforce.com/services/oauth2/token'
        token = None
        #headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        data = {
            'grant_type': 'password',
            'client_id': '3MVG9g9rbsTkKnAXkruajj1p10vh7Rj0WNM6QyQ9aEhAxWxvjBCR3W.N8By4BJOlKm3bskH4PJWzEwp1WiLLg',
            'client_secret': '7037194655269788417',
            'username': 'kerri.shields1@cescaphe.com',
            'password': 'ce5caphe2',
        }
        r = requests.post(url,data=data)
        _logger.error(r.text)
        responseData = json.loads(r.text)
        print (responseData)
        if 'error' in responseData:
            _logger.error("[cap_Salesforce] Connection failed")
        elif 'access_token' in responseData :
            token = responseData['access_token']
            _logger.error(token)
            
        return token
    
    #sobjects : Contact / Account / Lead / Tasks
    @api.model
    def push_to_salesforce(self,token,sobjects,data):
        id = None
        url = 'https://na73.salesforce.com/services/data/v42.0/sobjects/'+sobjects
        headers = {'content-type': 'application/json', 'Authorization': 'Bearer '+token }
        
        json_data = json.dumps(data)
        r = requests.post(url,headers=headers,data=json_data)
        _logger.error(r.text)
        responseData = json.loads(r.text)
        print (responseData)
        if 'error' in responseData:
            _logger.error("[cap_Salesforce] Salesforce push data failed : "+responseData['errors'])
        elif 'success' in responseData :
            id = responseData['id']
            
        return id
    
    #sobjects : Contact / Account / Lead / Tasks
    @api.model
    def get_to_salesforce(self,token,sobjects,id):
        record = None
        url = 'https://na73.salesforce.com/services/data/v20.0/sobjects/'+sobjects+'/'+id
        headers = {'content-type': 'application/json', 'Authorization': 'Bearer '+token }
        
        r = requests.get(url,headers=headers)
        _logger.error(r.text)
        responseData = json.loads(r.text)
        print (responseData)
        if 'error' in responseData:
            _logger.error("[cap_Salesforce] Salesforce get data failed : "+responseData['errors'])
        elif :
            record = responseData
            
        return record
    
    #sobjects : Contact / Account / Lead / Tasks
    @api.model
    def describe_object_salesforce(self,token,sobjects):
        url = 'https://na73.salesforce.com/services/data/v20.0/sobjects/'+sobjects+'/describe/'
        headers = {'content-type': 'application/json', 'Authorization': 'Bearer '+token }
        
        r = requests.get(url,headers=headers)
        _logger.error(r.text)
        responseData = json.loads(r.text)
        print (responseData)
        if 'error' in responseData:
            _logger.error("[cap_Salesforce] Salesforce dscribe object failed : "+responseData['errors'])
            
        return True
    
