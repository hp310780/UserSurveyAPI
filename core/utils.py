import json


class BaseDAO(object):
    """ Potential Base class for API DAOs."""

    def __init__(self, DB):
        self.DB_FILE = DB
        with open(DB) as db:
            self.db = json.load(db)

    def _write(self, data):
        """Write updated data list as in-mem list and to file.

        Args:
            data (dict): Object to write to db.
        """
        self.db.append(data)

        with open(self.DB_FILE, 'w') as outfile:
            json.dump(self.db, outfile)

    def get(self):
        return self.db

    def _create_id(self):
        raise NotImplementedError

    def create(self, data):
        obj = data
        obj['id'] = self._create_id()
        self._write(obj)
        return obj
