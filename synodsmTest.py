#!/usr/bin/env python3
# coding: utf-8

from synology_dsm import SynologyDSM
import json
import sys


class SynoZBX():
    def __init__(self, host, port, user, pasw):
        self.host = host
        self.port = port
        self.user = user
        self.pasw = pasw

    def auth(self, host, port, user, pasw):
        api = SynologyDSM(self.host, self.port, self.user, self.pasw)
        api.storage.update()
        return api

    def get(self, discovery):
        api = self.auth(self.host, self.port, self.user, self.pasw)
        data = []

        if discovery == "discovery":
            for num, disk_id in enumerate(api.storage.disks_ids):
                data.append({"{#DRIVENAME}":str(api.storage.disk_name(disk_id)),
                             "{#DRIVEID}":str(disk_id),
                             "{#DRIVENUMB}":str(num),
                             "{#DRIVESTATUS}":str(api.storage.disk_smart_status(disk_id))})
            return json.dumps(data)
        else:
            if str(api.storage.disk_smart_status(discovery)) == "normal":
                data = 1
            else: data = 0
            return data

def main():
    js = SynoZBX(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    print(js.get(sys.argv[5]))

if __name__ == "__main__":
    main()
