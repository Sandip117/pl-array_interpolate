#
# array_interpolation ds ChRIS plugin app
#
# (c) 2022 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#

from chrisapp.base import ChrisApp
import SimpleITK as sitk
import numpy as np

import glob


Gstr_title = r"""
                                _       _                        _       _   _             
                               (_)     | |                      | |     | | (_)            
  __ _ _ __ _ __ __ _ _   _     _ _ __ | |_ ___ _ __ _ __   ___ | | __ _| |_ _  ___  _ __  
 / _` | '__| '__/ _` | | | |   | | '_ \| __/ _ \ '__| '_ \ / _ \| |/ _` | __| |/ _ \| '_ \ 
| (_| | |  | | | (_| | |_| |   | | | | | ||  __/ |  | |_) | (_) | | (_| | |_| | (_) | | | |
 \__,_|_|  |_|  \__,_|\__, |   |_|_| |_|\__\___|_|  | .__/ \___/|_|\__,_|\__|_|\___/|_| |_|
                       __/ |_____                   | |                                    
                      |___/______|                  |_|                                    
"""

Gstr_synopsis = """

(Edit this in-line help for app specifics. At a minimum, the 
flags below are supported -- in the case of DS apps, both
positional arguments <inputDir> and <outputDir>; for FS and TS apps
only <outputDir> -- and similarly for <in> <out> directories
where necessary.)

    NAME

       array_interpolation

    SYNOPSIS

        docker run --rm fnndsc/pl-array_interpolation array_interpolation                     \\
            [-h] [--help]                                               \\
            [--json]                                                    \\
            [--man]                                                     \\
            [--meta]                                                    \\
            [--savejson <DIR>]                                          \\
            [-v <level>] [--verbosity <level>]                          \\
            [--version]                                                 \\
            <inputDir>                                                  \\
            <outputDir> 

    BRIEF EXAMPLE

        * Bare bones execution

            docker run --rm -u $(id -u)                             \
                -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing      \
                fnndsc/pl-array_interpolation array_interpolation                        \
                /incoming /outgoing

    DESCRIPTION

        `array_interpolation` ...

    ARGS

        [-h] [--help]
        If specified, show help message and exit.
        
        [--json]
        If specified, show json representation of app and exit.
        
        [--man]
        If specified, print (this) man page and exit.

        [--meta]
        If specified, print plugin meta data and exit.
        
        [--savejson <DIR>] 
        If specified, save json representation file to DIR and exit. 
        
        [-v <level>] [--verbosity <level>]
        Verbosity level for app. Not used currently.
        
        [--version]
        If specified, print version number and exit. 
"""


class Array_interpolation(ChrisApp):
    """
    An app to ...
    """
    PACKAGE                 = __package__
    TITLE                   = 'A ChRIS plugin app'
    CATEGORY                = ''
    TYPE                    = 'ds'
    ICON                    = ''   # url of an icon image
    MIN_NUMBER_OF_WORKERS   = 1    # Override with the minimum number of workers as int
    MAX_NUMBER_OF_WORKERS   = 1    # Override with the maximum number of workers as int
    MIN_CPU_LIMIT           = 2000 # Override with millicore value as int (1000 millicores == 1 CPU core)
    MIN_MEMORY_LIMIT        = 8000  # Override with memory MegaByte (MB) limit as int
    MIN_GPU_LIMIT           = 0    # Override with the minimum number of GPUs as int
    MAX_GPU_LIMIT           = 0    # Override with the maximum number of GPUs as int

    # Use this dictionary structure to provide key-value output descriptive information
    # that may be useful for the next downstream plugin. For example:
    #
    # {
    #   "finalOutputFile":  "final/file.out",
    #   "viewer":           "genericTextViewer",
    # }
    #
    # The above dictionary is saved when plugin is called with a ``--saveoutputmeta``
    # flag. Note also that all file paths are relative to the system specified
    # output directory.
    OUTPUT_META_DICT = {}

    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
        Use self.add_argument to specify a new app argument.
        """
        self.add_argument(  '--inputFileFilter','-i',
                            dest         = 'inputFileFilter',
                            type         = str,
                            optional     = True,
                            help         = 'Input file filter',
                            default      = '**/*.nii.gz')

    def run(self, options):
        """
        Define the code to be run by this plugin app.
        """
        print(Gstr_title)
        print('Version: %s' % self.get_version())
        
        
        
        # read an input array
        
        input_file_path = ""
        str_glob = ""
        if len(options.inputFileFilter):
            str_glob = '%s/%s' % (options.inputdir, options.inputFileFilter)
        if len(str_glob):
            l_allHits = glob.glob(str_glob, recursive = True)
            if len(l_allHits): input_file_path = l_allHits[0]
            else:
                print("No valid input sequence text file was found!")
                sys.exit(1)
        print(input_file_path)        
        img = sitk.ReadImage(input_file_path)
        num_array =  sitk.GetArrayFromImage(img)    
        # Logging only
        ip = num_array
        print("Shape of input numpy:{} \n \
                      Data type of input numpy:{} \n \
                      Max value of input numpy:{} \n \
                      Unique elements are :{} \n \
                      Count of unique elements : {}" \
                      .format(ip.shape,ip.dtype,np.max(ip), np.unique(ip), len(np.unique(ip))))   
        
        # read the interpolation/reshaping choice
        
        # transform the array
        
        # store the array

    def show_man_page(self):
        """
        Print the app's man page.
        """
        print(Gstr_synopsis)
