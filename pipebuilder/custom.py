
from .core import Command
from . import util
from .util import config

ROBEXPATH = 'none'#config.get('Binaries', 'ROBEXPATH')
TENSORFLOWPYTHON = config.get('Binaries', 'TENSORFLOWPYTHON')
NEURONBE = config.get('Binaries', 'NEURONBE')
nCEREBRO = config.get('Binaries', 'nCEREBRO')

class RobexCommand(Command):
    def __init__(self, comment, **kwargs):
        """
        Command to run ROBEX (robust brain extraction tool)

        Keyword arguments:
        ------------------
        input, output: input and brain-extracted output
        out_mask: output mask (binary image) marking where the brain is
        """
        self.cmd = ROBEXPATH + '/runROBEX.sh %(input)s %(output)s %(out_mask)s'
        self.outfiles = [kwargs['output'], kwargs['out_mask']]
        Command.__init__(self, comment, **kwargs)


class NeuronBECommand(Command):
    def __init__(self, comment, **kwargs):
        """
        Command to run ROBEX (robust brain extraction tool)

        Keyword arguments:
        ------------------
        input, output: input and brain-extracted output
        out_mask: output mask (binary image) marking where the brain is
        """
        self.cmd = TENSORFLOWPYTHON + ' -u ' + NEURONBE + ' -i %(input)s -o %(out_mask)s -b %(output)s -n %(out_intres)s -g %(out_gmwm_mask)s -r %(out_refined_mask)s'
        self.outfiles = [kwargs['out_intres'], kwargs['out_mask']]
        Command.__init__(self, comment, **kwargs)

class nCerebroCommand(Command):
    def __init__(self, comment, **kwargs):
        """
        Command to run ROBEX (robust brain extraction tool)

        Keyword arguments:
        ------------------
        input, output: input and brain-extracted output
        out_mask: output mask (binary image) marking where the brain is
        """
        self.cmd = TENSORFLOWPYTHON + ' -u ' + nCEREBRO + ' %(input)s %(output)s'
        Command.__init__(self, comment, **kwargs)

class IntresCommand(Command):
    def __init__(self, comment, **kwargs):
        """
        Command to run ROBEX (robust brain extraction tool)

        Keyword arguments:
        ------------------
        input, output: input and brain-extracted output
        out_mask: output mask (binary image) marking where the brain is
        """
        self.cmd = TENSORFLOWPYTHON + ' -u ' + INTRES + ' %(input)s %(output)s %(maskFile)s '
        self.outfiles = [kwargs['output']]
        Command.__init__(self, comment, **kwargs)

class FSLBinariseCommand(Command):
    def __init__(self, comment, **kwargs):
        """
	Command to run ROBEX (robust brain extraction tool)

        Keyword arguments:
        ------------------
        input, output: input and brain-extracted output
        out_mask: output mask (binary image) marking where the brain is
        """
	self.cmd = 'fslmaths %(input)s -thr %(threshold)s -bin %(output)s'
        self.outfiles = [kwargs['output']]
        Command.__init__(self, comment, **kwargs)

