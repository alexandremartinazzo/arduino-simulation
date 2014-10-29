# -*- coding: UTF-8 -*-
# Python Script
import sys
from os.path import splitext, basename

import pysimulavr
from ex_utils import SimulavrAdapter

if __name__ == "__main__":

    proc, elffile = sys.argv[1].split(":")
    # creates a list of observed variables (parsed from arguments)
    try:
        var_list = sys.argv[2].split(',')
    except IndexError:
        print 'indicate a list of comma-separated variables: var1,var2,var3'
        sys.exit(1)

    print 'monitored variables: %s' % var_list

    simulator = SimulavrAdapter()
    simulator.dmanSingleDeviceApplication()
    device = simulator.loadDevice(proc, elffile)
    # ~16MHz
    device.SetClockFreq(62)

    simulator.dmanStart()
    print "simulation start: (t=%dns)" % simulator.getCurrentTime()
    for word in var_list:
        print "\tvalue '%s' = %d" % (word, simulator.getWordByName(device, word))

    simulator.doRun(simulator.getCurrentTime() + 7000000)
    print "device time: %d ns" % simulator.getCurrentTime()
    for word in var_list:
        print "\tvalue '%s' = %d" % (word, simulator.getWordByName(device, word))

    simulator.doRun(simulator.getCurrentTime() + 5000000)
    print "device time: %d ns" % simulator.getCurrentTime()
    for word in var_list:
        print "\tvalue '%s' = %d" % (word, simulator.getWordByName(device, word))

    simulator.doRun(simulator.getCurrentTime() + 2000000)
    print "device time: %d ns" % simulator.getCurrentTime()
    for word in var_list:
        print "\tvalue '%s' = %d" % (word, simulator.getWordByName(device, word))

    simulator.doRun(simulator.getCurrentTime() + 2000000)
    print "device time: %d ns" % simulator.getCurrentTime()
    for word in var_list:
        print "\tvalue '%s' = %d" % (word, simulator.getWordByName(device, word))

    simulator.doRun(simulator.getCurrentTime() + 1000000)
    print "simulation end: (t=%dns)" % simulator.getCurrentTime()
    for word in var_list:
        print "\tvalue '%s' = %d" % (word, simulator.getWordByName(device, word))

    simulator.dmanStop()
    del device
