#
# Copyright 2012 Kenichi Sato <ksato9700@gmail.com>
#

import sys
import couchdb
import plistlib
import json

class Tomberg:
    def __init__(self, couchdb_host):
        self.server = couchdb.Server(couchdb_host)
        self.stages = self.server['stages']

    def read_plist(self, filename):
        self.plist = plistlib.readPlist(filename)

    def write_to_db(self):
        stage_id, _ = self.stages.save({'title':self.plist['title']})
        db = self.server.create('scenes-' + stage_id)
        for s in self.plist['scenes']:
            db.save(s)
        db["_design/scenes"] = {
            "language": "javascript",
            "views": {
                "all": {
                    "map":"function(doc) {emit(null, doc);}"
                    }
                }
            }
        #print json.dumps(self.plist, indent=4)

if __name__ == '__main__':
    tb = Tomberg(sys.argv[1])
    tb.read_plist(sys.argv[2])
    tb.write_to_db()
    
