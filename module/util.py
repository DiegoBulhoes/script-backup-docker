"""
Script designed for the purpose of performing container backups in a service configuration study environment.
"""

import datetime
import subprocess as ps


class Util:
    def __init__(self):
        super()

    @staticmethod
    def isRepositoryOfficial(containerInfo):
        """
            Checks if the image is in an official repository

            :Example:
            >>> Util.isRepositoryOfficial(['foo', 'foo /foo', '123456789123'])

            :param containerInfo: List containing the basic container information (image name, container name and ID)
            :type containerInfo: list
        """
        return containerInfo[1].find('/') > -1

    @staticmethod
    def getNameRepository(containerInfo):
        """
            Returns the image repository name

            :Example:
            >>> Util.getNameRepository(['portainer', 'portainer/portainer', '123456789123'])

            :param containerInfo: List containing the basic container information (image name, container name and ID)
            :type containerInfo: String
            :return: Container repository official name
            :rtype: String
        """
        return containerInfo[1].split('/')[0]

    @staticmethod
    def createBackupFileName(containerInfo):
        """
            Create a name for use in creating backup archive

            :Example:
            >>> Util.createBackupFileName(['portainer', 'portainer/portainer', '123456789123'])

            :param container: List containing the basic container information (image name, container name and ID)
            :type containerInfo: list
            :return: Returns a string representing the directory path.
            :rtype: string
        """
        now = datetime.datetime.now()
        name = '{}-{}-{}-{}-{}-{}-{}-{}-{}'.format(
            containerInfo[1],
            containerInfo[0],
            containerInfo[2],
            now.year,
            now.month,
            now.day,
            now.hour,
            now.minute,
            now.second)
        return name

    @staticmethod
    def createDirectory(path):
        """
            Create a directory according to the path passed by parameter

            :Example:
            >>> Util.createDirectory('./backup')

            :param path: Directory path that will be created
            :type path: String
        """
        ps.run(
            ["mkdir", path, '-p'], check=False)

    @staticmethod
    def createOfficialContainerPath(backupFilePath, dateToday, containerInfo):
        """
            create directory path that will contain the backup for official container

            :Example:
            >>> Util.createOfficialContainerPath('./backup','2000-12-13',['portainer', 'portainer/portainer', '123456789123'])

            :param backupFilePath: Location to store the directory that will contain the container backup
            :type backupFilePath: String
            :param dateToday: Date to use to compose backup storage directory path
            :type dateToday: datetime.date
            :param containerInfo: List containing the basic container information (image name, container name and ID)
            :type containerInfo: list

            :return: Path that will be saved from the container belonging to an official repository
            :rtype: string
        """
        path = '{}/{}/{}'.format(backupFilePath, str(dateToday),
                                 Util.getNameRepository(containerInfo))
        return path

    @staticmethod
    def createUnofficialContainerPath(backupFilePath, dateToday):
        """
            create directory path that will contain the backup for unofficial container

            :Example:
            >>> Util.createUnofficialContainerPath('./backup','2000-12-13')

            :param backupFilePath: Location to store the directory that will contain the container backup
            :type backupFilePath: String
            :param dateToday: Date to use to compose backup storage directory path
            :type dateToday: :class:`datetime.date`

            :return: Path that will be saved from the container belonging to an official repository
            :rtype: string
        """
        path = '{}/{}'.format(backupFilePath, str(dateToday))
        return path

    @staticmethod
    def createBackupDirectory(backupFilePath, containerInfo):
        """
            Creates the directory that will be stored the backups.

            :Example:
            >>> Util.createBackupDirectory('./backup','2000-12-13',['portainer', 'portainer/portainer', '123456789123'])

            :param backupFilePath: Location to store the directory that will contain the container backup
            :type backupFilePath: String
            :param containerInfo: List containing the basic container information (image name, container name and ID)
            :type containerInfo: list
        """
        if Util.isRepositoryOfficial(containerInfo):
            path = Util.createOfficialContainerPath(
                backupFilePath, datetime.date.today(), containerInfo)
            Util.createDirectory(path)

        path = Util.createUnofficialContainerPath(
            backupFilePath, datetime.date.today())
        Util.createDirectory(path)

    @staticmethod
    def createBulkDirectoryStructure(backupFilePath, containerInfoList):
        """
            Create directory structure where all backups will be stored

            :Example:
            >>> Util.createBackupDirectory('./backup','2000-12-13')

            :param backupFilePath: Location to store the directory that will contain the container backup
            :type backupFilePath: String
            :param containerInfo: List containing the basic container information (image name, container name and ID)
            :type containerInfo: list
        """
        for containerInfo in containerInfoList:
            Util.createBackupDirectory(
                backupFilePath, containerInfo)

    @staticmethod
    def createContainerInformationList():
        """
            Create a list that will contain the basic container information (image name, container name and ID)

            :Example:
            >>> Util.createContainerInformationList()
        """
        containerInfoList = ps.check_output(
            [
                'docker',
                'container',
                'ls',
                '--format={{.Names}},{{.Image}},{{.ID}}',
                '--all']).decode().split('\n')
        containerInfoList.pop()
        containerInfoList = list(x.lower().split(',')
                                 for x in containerInfoList)
        return containerInfoList

    @staticmethod
    def createBackupFilePath(backupFilePath, nameImageTemp):
        """
            Create a list that will contain the basic container information (image name, container name and ID)

            :Example:
            >>> Util.createBackupFilePath()

            :param backupFilePath: Location to store the directory that will contain the container backup
            :type backupFilePath: String
        """
        path = '{}/{}/{}.tar'.format(backupFilePath,
                                     datetime.date.today(), nameImageTemp)
        return path
