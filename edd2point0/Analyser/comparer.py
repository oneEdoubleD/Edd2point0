class Comparer():

    _old_logfile = None
    _new_logfile = None

    def __init__(self, old_logfile, new_logfile):
        self._old_logfile = old_logfile
        self._new_logfile = new_logfile

    def compare(self):
        old_logfile_data = self._old_logfile.count_logs()
        new_logfile_data = self._new_logfile.count_logs()

        return { 'ErrorDelta': (old_logfile_data.get('Errors') - new_logfile_data.get('Errors')),
                 'InfoDelta': (old_logfile_data.get('Info') - new_logfile_data.get('Info')),
                 'DebugDelta': (old_logfile_data.get('Debug') - new_logfile_data.get('Debug')),
                 'NoticeDelta': (old_logfile_data.get('Notice') - new_logfile_data.get('Notice')) }
    
    def find_all_new_logs(self):
        old_logs = self._old_logfile.get_logs()
        new_logs = self._new_logfile.get_logs()

        old_logs_hash_table = dict()
        for i in range(len(old_logs)):
            old_logs_hash_table[old_logs[i]] = 1

        for i in range(len(new_logs)):
            if new_logs[i] not in old_logs_hash_table.keys():
                print(new_logs[i], end=" ")
    
    def find_all_old_logs(self):
        old_logs = self._old_logfile.get_logs()
        new_logs = self._new_logfile.get_logs()

        new_logs_hash_table = dict()
        for i in range(len(new_logs)):
            new_logs_hash_table[new_logs[i]] = 1

        for i in range(len(old_logs)):
            if old_logs[i] not in new_logs_hash_table.keys():
                print(old_logs[i], end=" ")

    def find_new_errors(self):
        old_errors = self._old_logfile.find_errors()
        new_errors = self._new_logfile.find_errors()

        old_errors_hash_table = dict()
        for i in range(len(old_errors)):
            old_errors_hash_table[old_errors[i]] = 1

        for i in range(len(new_errors)):
            if new_errors[i] not in old_errors_hash_table.keys():
                print(new_errors[i], end=" ")
