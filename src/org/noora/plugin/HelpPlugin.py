from org.noora.plugin.Plugin import Plugin
from org.noora.output.ConsoleOutput import ConsoleOutput

class HelpPlugin(Plugin):

  def __init__(self, inputObject, outputObject):
    Plugin.__init__(self, inputObject, outputObject)
    
  def initialize(self):
    # overrule current output with console output
    self.setOutput(ConsoleOutput())
  
  def execute(self):
    msg = "here comes some help"
    self.getOutput().processOutput(msg)
