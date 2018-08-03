from apitax.drivers.Drivers import Drivers


class Project:
    def __init__(self):
        pass
 
    def loadDrivers(self):
        #pass
        from apitaxdrivers.BasicGit import BasicGitDriver
        from apitaxdrivers.BasicAuth import BasicAuthDriver

        from apitaxdrivers.ApitaxTests import ApitaxTestsDriver
        from apitaxdrivers.commandtax.ApitaxTestsCommands import ApitaxTestsCommands
        from apitaxdrivers.ApitaxInfo import ApitaxInfoDriver
        from apitaxdrivers.commandtax.ApitaxInfoCommands import ApitaxInfoCommands
        
        from apitaxdrivers.Openstack import OpenstackDriver

        from apitaxdrivers.Github import GithubDriver
        
        from app.Vsrx import VsrxDriver
        
        #from apitaxdrivers.commandtax.AnsibleCommands import AnsibleCommands
        from app.AnsibleCommands import AnsibleCommands
        from apitaxdrivers.Ansible import AnsibleDriver
        
        Drivers.add("BasicGitDriver", BasicGitDriver())
        Drivers.add("BasicAuthDriver", BasicAuthDriver())
        Drivers.add("ApitaxTestsDriver", ApitaxTestsDriver())
        Drivers.add("ApitaxTestsCommands", ApitaxTestsCommands())
        Drivers.add("ApitaxInfoDriver", ApitaxInfoDriver())
        Drivers.add("ApitaxInfoCommands", ApitaxInfoCommands())
        Drivers.add("OpenstackDriver", OpenstackDriver())
        Drivers.add("GithubDriver", GithubDriver())
        
        Drivers.add("VsrxDriver", VsrxDriver())
        
        Drivers.add("AnsibleDriver", AnsibleDriver())
        Drivers.add("AnsibleCommands", AnsibleCommands())
        
#p = Project()
#p.loadDrivers()
        

