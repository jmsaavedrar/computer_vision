#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 2018
@author: jsaavedr

Description: A list of function to create tfrecords from a jfile
"""

import argparse
import sys
import os
import params
sys.path.insert(0, params.cnn_lib_location)

if __name__ == '__main__':                
    import cnnLib.data  as data
    import cnnLib.imgproc  as imgproc
    import cnnLib.configuration as conf
    parser = argparse.ArgumentParser(description = "Create a dataset for training an testing")
    """ pathname should include train.txt and test.txt, files that should declare the data that will be processed"""  
    parser.add_argument("-type", type = int, help = "<int> 0: only train, 1: only test, 2: both", required = True )
    parser.add_argument("-config", type = str, help = "<str> configuration file", required = True)
    parser.add_argument("-name", type=str, help=" name of section in the configuration file", required = True)        
    parser.add_argument("-imheight", type = int, help = "<int> size of the image", required = True)
    parser.add_argument("-imwidth", type = int, help = "<int> size of the image", required = False)    
    pargs = parser.parse_args() 
    imh = pargs.imheight
    imw = pargs.imwidth
    if imw is None:
        imw = pargs.imheight            
    configuration_file = pargs.config
    assert os.path.exists(configuration_file), "configuration file does not exist {}".format(configuration_file)   
    configuration = conf.ConfigurationFile(configuration_file, pargs.name)               
    data.create_tfrecords(configuration.get_data_dir(), pargs.type, (imh, imw), number_of_channels = configuration.get_number_of_channels(), processFun = imgproc.get_process_fun())
    print("tfrecords created for " + configuration.get_data_dir())