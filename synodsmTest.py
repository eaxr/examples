from synology_dsm import SynologyDSM
import json
import sys


class SynoZBX():
    def __init__(self, host, port, user, pasw):
        self.host = host
        self.port = port
        self.user = user
        self.pasw = pasw

    def auth(self):
        api = SynologyDSM(self.host, self.port, self.user, self.pasw)
        api.storage.update()

    def get(self):
        api = SynologyDSM(self.host, self.port, self.user, self.pasw)
        api.storage.update()
        data = [{}]

        for disk_id in api.storage.disks_ids:
            data[0][str(api.storage.disk_name(disk_id))] = str(api.storage.disk_smart_status(disk_id))
        return json.dumps(data)

def main():
    js = SynoZBX(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    print(js.get())

if __name__ == "__main__":
    main()
