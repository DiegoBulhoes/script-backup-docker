"""
Script designed for the purpose of performing container backups in a service configuration study environment.

Site  : https://github.com/DiegoBulhoes/script-backup-docker
Autor : Diego Bulhoes

History:
  v1.0 2019-12-28, Diego Bulhoes:
      -- Initial version of program running without error handling
"""
import argparse
from module.restore import Restore
from module.helpInit import HelpInit
from module.backup import Backup


if __name__ == "__main__":
    user = HelpInit(argparse.ArgumentParser(), Backup(), Restore())
    user.help()
