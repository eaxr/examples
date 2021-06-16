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
                data.append({"{#DRIVEID}":str(api.storage.disk_name(disk_id)),
                             "{#DRIVENUM}":str(num)})
        else:
            for disk_id in api.storage.disks_ids:
                if str(api.storage.disk_name(disk_id)) == discovery:
                    data.append({"{#DRIVESTATUS}":str(api.storage.disk_smart_status(disk_id))})

        return json.dumps(data)

def main():
    js = SynoZBX(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    print(js.get(sys.argv[5]))

if __name__ == "__main__":
    main()
