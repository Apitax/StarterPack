from apitax.flow.Project import Project as BaseProject


class Project(BaseProject):
    def isDev(self):
        return False

    def isDebug(self):
        return True

    def setup(self):
        from apitaxcore.models.State import State
        State.paths['root'] = '/app'
        State.paths['config'] = State.paths['root'] + '/app/config.txt'
        #State.paths['log'] = None

    def loadDrivers(self):
        from apitaxcore.drivers.Drivers import Drivers
        from apitaxdrivers.Github import GithubDriver
        Drivers.add("github", GithubDriver())
