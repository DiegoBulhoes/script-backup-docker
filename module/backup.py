"""
This module has the purpose of having backup functions.
"""

import subprocess as ps
from . import Util as u


class Backup:
    def __init__(self):
        super()

    def createBackupOfSpecificContainer(self, container, backupFilePath):
        """
            Create a backup of a specific container

            :Example:
            >>> createBackupOfSpecificContainer()

            :param container: List containing basic ocontainer information
            :type container: list
            :param backupFilePath: Location to store the directory that will contain the container backup
            :type backupFilePath: String
        """
        containerInfo = ps.check_output(['docker', 'ps', '-f id={}'.format(
            container), '--format={{.Names}},{{.Image}},{{.ID}}']).decode().split('\n')
        containerInfo.pop()
        containerInfo = containerInfo[0].lower().split(',')
        u.createBackupDirectory(backupFilePath, containerInfo)
        self.backupContainer(containerInfo, backupFilePath)

    def backupContainer(self, container, backupPath):
        """
            Back up container according to parameters passed

            :Example:
            >>> backupContainer()

            :param container: List containing basic ocontainer information
            :type container: list
            :param backupFilePath: Location to store the directory that will contain the container backup
            :type backupFilePath: String
        """
        nameImageTemp = u.createBackupFileName(container)
        ps.run(['docker', 'commit', container[2],
                nameImageTemp], check=False)
        backupPath = u.createBackupFilePath(
            backupPath, nameImageTemp)
        ps.run(["docker", "save", nameImageTemp, '-o', backupPath], check=False)
        ps.run(['docker', 'image', 'rm', nameImageTemp], check=False)

    def backupOfAllContainers(self, backupFilePath):
        """
            Back up all containers that are in the same environment

            :Example:
            >>> backupOfAllContainers()

            :param backupFilePath: Location to store the directory that will contain the container backup
            :type backupFilePath: String
        """
        containerInfoList = u.createContainerInformationList()
        u.createBulkDirectoryStructure(
            backupFilePath, containerInfoList)
        for infoContainer in containerInfoList:
            self.backupContainer(infoContainer, backupFilePath)
