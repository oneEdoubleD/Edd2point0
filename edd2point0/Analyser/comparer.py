class Comparer():

    @staticmethod
    def compare_logs(logfile_1: 'Log', logfile_2: 'Log'):
        """Find the delta of events between two Log objects

        Args:
            logfile_1: A log object to be compared with
            logfile_2: A log object to compare

        Returns:
            A dictionary with the following keys: ErrorDelta, InfoDelta, DebugDelta, NoticeDelta
        """
        old_logfile_data = logfile_1.count_logs()
        new_logfile_data = logfile_2.count_logs()

        return { 'ErrorDelta': (old_logfile_data.get('Errors') - new_logfile_data.get('Errors')),
                 'InfoDelta': (old_logfile_data.get('Info') - new_logfile_data.get('Info')),
                 'DebugDelta': (old_logfile_data.get('Debug') - new_logfile_data.get('Debug')),
                 'NoticeDelta': (old_logfile_data.get('Notice') - new_logfile_data.get('Notice')) }

    @staticmethod
    def diff(logfile_1: 'Log', logfile_2: 'Log'):
        """Diff two Log objects

        Args:
            logfile_1: A Log object to be compared with
            logfile_2: A Log object to compare

        Returns:
            An array of strings containing each log found in logfile_2 that doesn't exist in logfile_1
        """
        logfile_1_logs = logfile_1.get_logs()
        logfile_2_logs = logfile_2.get_logs()

        new_logs = []

        logfile_1_logs_hash_table = dict()
        for i in range(len(logfile_1_logs)):
            logfile_1_logs_hash_table[logfile_1_logs[i]] = 1

        for i in range(len(logfile_2_logs)):
            if logfile_2_logs[i] not in logfile_1_logs_hash_table.keys():
                new_logs.append(logfile_2_logs[i])
        
        return new_logs

    @staticmethod
    def diff_errors(logfile_1: 'Log', logfile_2: 'Log'):
        """Diff two Log objects for errors

        Args:
            logfile_1: A Log object to be compared with
            logfile_2: A Log object to compare

        Returns:
            An array of strings containing each error log found in logfile_2 that doesn't exist in logfile_1
        """
        logfile_1_errors = logfile_1.find_errors()
        logfile_2_errors = logfile_2.find_errors()

        new_error_logs = []

        logfile_1_errors_hash_table = dict()
        for i in range(len(logfile_1)):
            logfile_1_errors_hash_table[logfile_1_errors[i]] = 1

        for i in range(len(logfile_2_errors)):
            if logfile_2_errors[i] not in logfile_1_errors_hash_table.keys():
                new_error_logs.append(logfile_2_errors[i])
        
        return new_error_logs
