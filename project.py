from apitax.drivers.Drivers import Drivers


class Project:
    def __init__(self):
        pass
 
    def loadDrivers(self):
        #pass
        from apitaxdrivers.plugins.BasicGit import BasicGitDriver
        from apitaxdrivers.plugins.BasicAuth import BasicAuthDriver

        from apitaxdrivers.plugins.ApitaxTests import ApitaxTestsDriver
        from apitaxdrivers.plugins.commandtax.ApitaxTestsCommands import ApitaxTestsCommands
        from apitaxdrivers.plugins.ApitaxInfo import ApitaxInfoDriver
        from apitaxdrivers.plugins.commandtax.ApitaxInfoCommands import ApitaxInfoCommands
        
        from apitaxdrivers.plugins.Openstack import OpenstackDriver

        from apitaxdrivers.plugins.Github import GithubDriver
        
        Drivers.add("BasicGitDriver", BasicGitDriver())
        Drivers.add("BasicAuthDriver", BasicAuthDriver())
        Drivers.add("ApitaxTestsDriver", ApitaxTestsDriver())
        Drivers.add("ApitaxTestsCommands", ApitaxTestsCommands())
        Drivers.add("ApitaxInfoDriver", ApitaxInfoDriver())
        Drivers.add("ApitaxInfoCommands", ApitaxInfoCommands())
        Drivers.add("OpenstackDriver", OpenstackDriver())
        Drivers.add("GithubDriver", GithubDriver())
        

