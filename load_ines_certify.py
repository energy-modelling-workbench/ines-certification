import sys
import json
import spinedb_api as api

inescertify = sys.argv[1]
collection = sys.argv[2]

with open(inescertify) as f:
	iodb = json.load(f)

with api.DatabaseMapping(collection) as target_db:
    api.import_data(target_db,**iodb)
    target_db.commit_session("import data")