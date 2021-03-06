'''
Module for issuing alerts.
Examples:
    alert.notice  sys.everython 'things are going great'
    alert.warning disk.hardware 'the VAX drive ${value} is wobbling'
    alert.error   turboencabular.wanshaft '${key} is {value:.1f} mm from failure'
'''

import logging
import salt.ext.monitor.client

log = logging.getLogger(__name__)

def _alert(level, category, msg):
    '''
    Send the alert to the alert service.
    '''
    __opts__['master_uri'] = 'tcp://{}:{}'.format(__opts__['alert_master'],
                                                  __opts__['alert.port'])
    host = __opts__.get('id', 'unknown')
    aclient = salt.ext.monitor.client.AlertClient(__opts__)
    aclient.alert(host, level, category, msg)
    return [host, level, category, msg]

def notice(category, msg):
    '''
    Send a 'notice' alert.
    category = arbitrary alert category string, e.g. 'disk.sata.error'.
    msg = the alert message string, e.g. '/dev/sdb23 spindle is on fire'
    '''
    return _alert("NOTICE", category, msg)

def warning(category, msg):
    '''
    Send a 'warning' alert.
    category = arbitrary alert category string, e.g. 'disk.sata.error'.
    msg = the alert message string, e.g. '/dev/sdb23 spindle is on fire'
    '''
    return _alert("WARNING", category, msg)

def error(category, msg):
    '''
    Send an 'error' alert.
    category = arbitrary alert category string, e.g. 'disk.sata.error'.
    msg = the alert message string, e.g. '/dev/sdb23 spindle is on fire'
    '''
    return _alert("ERROR", category, msg)

def critical(category, msg):
    '''
    Send a 'critical' alert.
    category = arbitrary alert category string, e.g. 'disk.sata.error'.
    msg = the alert message string, e.g. '/dev/sdb23 spindle is on fire'
    '''
    return _alert("FATAL", category, msg)

def fatal(category, msg):
    '''
    Send a 'fatal' alert.
    category = arbitrary alert category string, e.g. 'disk.sata.error'.
    msg = the alert message string, e.g. '/dev/sdb23 spindle is on fire'
    '''
    return _alert("FATAL", category, msg)
