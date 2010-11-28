import core.ConfigReader
import core.ClassLoader
import core.ParameterHelper
import core.PluginManager
import os

class CommandDispatcher:
    '''
    This class will invoke the specified command. It will read the project configuration and
    use the specified arguments to dispatch the correct command.
    '''
    
    def setParameters(self,params):
        self.__parameterHelper = core.ParameterHelper.ParameterHelper()
        # clear parameters from params that are set in the constructor
        self.__parameterHelper.clearParameters()
        self.__parameterHelper.setParameters(params)

    def __initPlugins(self):
        # we assume that the config has been read successfully by the constructor
        classLoader = core.ClassLoader.ClassLoader()
        pluginManager = core.PluginManager.PluginManager()

        plugins = self.__config.getValue('PLUGINS')
        for plugin in plugins:
            pluginClass=classLoader.findByPattern(plugin)
            pluginManager.registerPlugin(pluginClass)
        
    def __init__(self, projectDir, command):
        
        self.__projectDir = projectDir
        self.__configFile = projectDir + os.sep + 'project.conf'
        
        os.chdir (self.__projectDir)
        self.__config = core.ConfigReader.ConfigReader(self.__configFile)
        
        self.__initPlugins()
        