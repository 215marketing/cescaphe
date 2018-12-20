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
        #headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        data = {
            'grant_type': 'password',
            'client_id': '3MVG9g9rbsTkKnAXkruajj1p10vh7Rj0WNM6QyQ9aEhAxWxvjBCR3W.N8By4BJOlKm3bskH4PJWzEwp1WiLLg',
            'client_secret': '7037194655269788417',
            'username': 'alex.kravets@cescaphe.com',
            'password': 'ce5caphe2',
        }
        r = requests.post(url,data=data)
        _logger.error(r.text)
        responseData = json.loads(r.text)
        if responseData.access_token :
            token = responseData.access_token
        else :
            _logger.error("Connection failed")
            
        return token
    
    #sobjects : Contact / Account / Lead / Tasks
    @api.model
    def push_to_salesforce(self,token,sobjects,data):
        url = 'https://na73.salesforce.com/services/data/v42.0/sobjects/'+sobjects
        headers = {'content-type': 'application/json', 'Authorization:': 'Bearer '+token }
        
        r = requests.post(url,headers=headers,data=data)
        if r.success :
            id = r.id
        else :
            _logger.error("Salesforce push data failed : "+r.errors)
            
        return id
    
    #sobjects : Contact / Account / Lead / Tasks
    @api.model
    def get_to_salesforce(self,token,sobjects,id):
        url = 'https://na73.salesforce.com/services/data/v20.0/sobjects/'+sobjects+'/'+id
        headers = {'content-type': 'application/json', 'Authorization:': 'Bearer '+token }
        
        r = requests.get(url,headers=headers)
        if r :
            record = r
        else :
            _logger.error("Salesforce push data failed : "+r.errors)
            
        return record
    
