import requests
from requests.auth import HTTPBasicAuth
import json
import xlsxwriter


class JiraObjects:
    def __init__(self, object_type):
        self.object_type = object_type
        self.object_list = {}
        self.object_name_idx = {}
        self.object_type_idx = {}
        self.objects_without_comment = {}
        self.api_status = 0
        self.no_of_rec_read = 0
        self.no_of_bad_rec_reads = 0
        init_file = "init.json"
        #load login info from file
        with open(self.init_file, 'r') as openfile:
            json_object = json.load(openfile)
        self.base_url = json_object['base_url']
        self.username = json_object['username']
        self.token = json_object['token']
        self.headers = {"Accept": "application/json"}
        self.auth = HTTPBasicAuth(self.username, self.token)