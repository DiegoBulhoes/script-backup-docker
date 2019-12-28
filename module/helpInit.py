"""
This module has the purpose of having the help functions of the tool.
"""

import argparse


class HelpInit:
    def __init__(self, parser, backup, restore):
        self.backup = backup
        self.restore = restore
        self.parseMain = parser
        super()

    def filterTheChoice(self, choice):
        """
            Back up all containers that are in the same environment

            :Example:
            >>> filterTheChoice(''container=None, pathBackup='./bk', routine='full')

            :param backupFilePath: Location to store the directory that will contain the container backup
            :type backupFilePath: :class:`argparse.Namespace`
        """
        if choice.routine == 'restore':
            self.restore.restoreImage(choice.pathBackup)
        elif choice.routine == 'backup':
            self.backup.createBackupOfSpecificContainer(
                choice.container, choice.pathBackup)
        elif choice.routine == 'full':
            self.backup.backupOfAllContainers(choice.pathBackup)

    def help(self):
        """
            Create a help regarding the use of this tool for user
        """
        self.parseMain.add_argument(
            '-r',
            '--routine',
            dest='routine',
            choices=[
                'backup',
                'restore',
                'full'],
            default='full')
        self.parseMain.add_argument(
            '-c', '--container', help='Container identifier')
        self.parseMain.add_argument(
            '-p', '--pathBackup', help='Path the backup', default='./')

        self.filterTheChoice(self.parseMain.parse_args())
