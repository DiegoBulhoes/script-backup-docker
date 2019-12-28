"""
This module has the purpose of having the restore functions.
"""

import subprocess as ps


class Restore:
    def __init__(self):
        super()

    def restoreImage(self, pathImage):
        """
            Restore backup of format accepted by Docker "load" method

            :Example:
            >>> createBackupFilePath()
        """
        ps.run(['docker', 'load', '-i', pathImage], check=False)
