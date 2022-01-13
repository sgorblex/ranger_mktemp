import os.path
import ranger.api.commands
from subprocess import PIPE


class tempd(ranger.api.commands.Command):
    """
    :tempd

    cd into temporary directory (made with mktemp -d)
    """

    def execute(self):
        cmd = self.fm.execute_command("mktemp -d", stdout=PIPE)
        stdout, _ = cmd.communicate()
        if cmd.returncode != 0:
            return

        made_dir = stdout.decode("utf-8").strip()

        if not os.path.isdir(made_dir):
            return
        self.fm.cd(made_dir)
