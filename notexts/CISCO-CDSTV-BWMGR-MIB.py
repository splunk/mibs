#
# PySNMP MIB module CISCO-CDSTV-BWMGR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-CDSTV-BWMGR-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
TimeIntervalSec, = mibBuilder.importSymbols("CISCO-TC", "TimeIntervalSec")
InetPortNumber, InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddress", "InetAddressType")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCdstvBwmgrMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 749))
ciscoCdstvBwmgrMIB.setRevisions(('2010-06-24 00:00',))
if mibBuilder.loadTexts: ciscoCdstvBwmgrMIB.setLastUpdated('201006240000Z')
if mibBuilder.loadTexts: ciscoCdstvBwmgrMIB.setOrganization('Cisco Systems, Inc.')
ciscoCdstvBWMgrMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 749, 0))
ciscoCdstvBWMgrMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 749, 1))
ciscoCdstvBWMgrMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 749, 2))
ciscoCdstvBWMgrMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 749, 2, 1))
cdstvBWMgrAddressType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 749, 1, 1), InetAddressType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvBWMgrAddressType.setStatus('current')
cdstvBWMgrAddress = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 749, 1, 2), InetAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvBWMgrAddress.setStatus('current')
cdstvBWMgrPort = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 749, 1, 3), InetPortNumber().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(7791)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvBWMgrPort.setStatus('current')
cdstvBWMgrDatabaseThreadPool = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 749, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvBWMgrDatabaseThreadPool.setStatus('current')
cdstvBWMgrServerThreadPool = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 749, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvBWMgrServerThreadPool.setStatus('current')
cdstvBWMgrSyncThreadPool = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 749, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvBWMgrSyncThreadPool.setStatus('current')
cdstvBWMgrSyncAlarm = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 749, 1, 7), TimeIntervalSec().subtype(subtypeSpec=ValueRangeConstraint(2400, 4294967295)).clone(864000)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdstvBWMgrSyncAlarm.setStatus('current')
ciscoCdstvBWMgrMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 749, 2, 2))
ciscoCdstvBWMgrMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 749, 2, 1, 1)).setObjects(("CISCO-CDSTV-BWMGR-MIB", "ciscoCdstvBWMgrMIBMainObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvBWMgrMIBCompliance = ciscoCdstvBWMgrMIBCompliance.setStatus('current')
ciscoCdstvBWMgrMIBMainObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 749, 2, 2, 1)).setObjects(("CISCO-CDSTV-BWMGR-MIB", "cdstvBWMgrAddress"), ("CISCO-CDSTV-BWMGR-MIB", "cdstvBWMgrPort"), ("CISCO-CDSTV-BWMGR-MIB", "cdstvBWMgrDatabaseThreadPool"), ("CISCO-CDSTV-BWMGR-MIB", "cdstvBWMgrServerThreadPool"), ("CISCO-CDSTV-BWMGR-MIB", "cdstvBWMgrSyncThreadPool"), ("CISCO-CDSTV-BWMGR-MIB", "cdstvBWMgrSyncAlarm"), ("CISCO-CDSTV-BWMGR-MIB", "cdstvBWMgrAddressType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCdstvBWMgrMIBMainObjectGroup = ciscoCdstvBWMgrMIBMainObjectGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-CDSTV-BWMGR-MIB", cdstvBWMgrSyncThreadPool=cdstvBWMgrSyncThreadPool, cdstvBWMgrSyncAlarm=cdstvBWMgrSyncAlarm, ciscoCdstvBWMgrMIBGroups=ciscoCdstvBWMgrMIBGroups, ciscoCdstvBWMgrMIBNotifs=ciscoCdstvBWMgrMIBNotifs, cdstvBWMgrAddressType=cdstvBWMgrAddressType, ciscoCdstvBWMgrMIBCompliance=ciscoCdstvBWMgrMIBCompliance, ciscoCdstvBWMgrMIBObjects=ciscoCdstvBWMgrMIBObjects, ciscoCdstvBWMgrMIBMainObjectGroup=ciscoCdstvBWMgrMIBMainObjectGroup, ciscoCdstvBWMgrMIBConform=ciscoCdstvBWMgrMIBConform, ciscoCdstvBWMgrMIBCompliances=ciscoCdstvBWMgrMIBCompliances, cdstvBWMgrServerThreadPool=cdstvBWMgrServerThreadPool, cdstvBWMgrAddress=cdstvBWMgrAddress, ciscoCdstvBwmgrMIB=ciscoCdstvBwmgrMIB, cdstvBWMgrPort=cdstvBWMgrPort, cdstvBWMgrDatabaseThreadPool=cdstvBWMgrDatabaseThreadPool, PYSNMP_MODULE_ID=ciscoCdstvBwmgrMIB)
