import os


class Logs():

    _file_path = None

    def __init__(self, file_path: str):
        """Initialise a new Log object

        Args:
            file_path: Either a full or relative path to a log file
        """
        self._file_path = file_path

    def _lines_that_contain(self, search_word: str):
        """Find all the lines in the Log that contains a specific word

        Args:
            search_word: The target word you're looking for

        Returns:
            An array of strings
        """
        with open(self._file_path) as logs:
            return [line for line in logs if search_word in line]

    def get_logs(self):
        """Get all of the logs

        Returns:
            An array of strings
        """
        with open(self._file_path) as logs:
            return [line for line in logs]

    def find_errors(self):
        """Find every log line that contains 'Error'

        Returns:
            An array of strings
        """
        return self._lines_that_contain('Error')

    def find_info(self):
        """Find every log line that contains 'Info'

        Returns:
            An array of strings
        """
        return self._lines_that_contain('Info')

    def find_debug(self):
        """Find every log line that contains 'Debug'

        Returns:
            An array of strings
        """
        return self._lines_that_contain('Debug')

    def find_notice(self):
        """Find every log line that contains 'Notice'

        Returns:
            An array of strings
        """
        return self._lines_that_contain('Notice')

    def count_logs(self):
        """Aggregate the number of events in the Log

        Returns:
            A dictionary with the following keys: Errors, Info, Debug, Notice
        """
        return { 'Errors': len(self.find_errors()),
                 'Info': len(self.find_info()),
                 'Debug': len(self.find_debug()),
                 'Notice': len(self.find_notice())}
