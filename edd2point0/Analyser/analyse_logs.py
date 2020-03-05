import os


class Logs():

    _file_path = None

    def __init__(self, file_path):
        self._file_path = file_path

    def _lines_that_contain(self, string):
        with open(self._file_path) as logs:
            return [line for line in logs if string in line]

    def get_logs(self):
        with open(self._file_path) as logs:
            return [line for line in logs]

    def find_errors(self):
        return self._lines_that_contain('Error')

    def find_info(self):
        return self._lines_that_contain('Info')

    def find_debug(self):
        return self._lines_that_contain('Debug')

    def find_notice(self):
        return self._lines_that_contain('Notice')

    def count_logs(self):
        return { 'Errors': len(self.find_errors()),
                 'Info': len(self.find_info()),
                 'Debug': len(self.find_debug()),
                 'Notice': len(self.find_notice())}
