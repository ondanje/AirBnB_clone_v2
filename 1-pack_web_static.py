#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
from the contents of the web_static folder
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():

    try:
        """Create the versions folder if it doesn't exist"""
        local("mkdir -p versions")

        """Get the current date and time"""
        now = datetime.utcnow()

        """Format the date and time into a string"""
        date_time_str = now.strftime("%Y%m%d%H%M%S")

        """Create the archive file name"""
        archive_name = "web_static_{}.tgz".format(date_time_str)

        """Compress """
        local("tar -czvf versions/{} web_static".format(archive_name))
        return os.path.join("versions", archive_name)
    except Exception as e:
        print("Error during archive creation: {}".format(e))
        return None
