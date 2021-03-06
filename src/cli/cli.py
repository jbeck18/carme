import click
from .commands import new, save, package, git, lab, build, notebook, cmd, ssh, start, stop, cleanup, convert
#from .commands.packages import samppack

# create a sample list of packages. Could pull from config.
packages = ['samppack']


@click.group()
@click.version_option()
def carme():
    pass


# commands from external files ie the commands folder must be manually
# imported then added to the group.
carme.add_command(lab)
carme.add_command(new)
carme.add_command(save)
carme.add_command(package)
carme.add_command(git)
carme.add_command(build)
carme.add_command(notebook)
carme.add_command(cmd)
carme.add_command(ssh)
carme.add_command(start)
carme.add_command(stop)
carme.add_command(cleanup)
carme.add_command(convert)
