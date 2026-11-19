#
# PySNMP MIB module CISCO-CDSTV-BWMGR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-CDSTV-BWMGR-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:42 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
TimeIntervalSec, = mibBuilder.importSymbols("CISCO-TC", "TimeIntervalSec")
InetAddressType, InetPortNumber, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetPortNumber", "InetAddress")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Gauge32, ModuleIdentity, Integer32, Bits, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Integer32", "Bits", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "Counter32")
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
mibBuilder.exportSymbols("CISCO-CDSTV-BWMGR-MIB", cdstvBWMgrAddress=cdstvBWMgrAddress, ciscoCdstvBWMgrMIBGroups=ciscoCdstvBWMgrMIBGroups, ciscoCdstvBWMgrMIBMainObjectGroup=ciscoCdstvBWMgrMIBMainObjectGroup, PYSNMP_MODULE_ID=ciscoCdstvBwmgrMIB, cdstvBWMgrDatabaseThreadPool=cdstvBWMgrDatabaseThreadPool, cdstvBWMgrPort=cdstvBWMgrPort, ciscoCdstvBWMgrMIBCompliance=ciscoCdstvBWMgrMIBCompliance, cdstvBWMgrServerThreadPool=cdstvBWMgrServerThreadPool, ciscoCdstvBWMgrMIBConform=ciscoCdstvBWMgrMIBConform, cdstvBWMgrSyncAlarm=cdstvBWMgrSyncAlarm, ciscoCdstvBWMgrMIBNotifs=ciscoCdstvBWMgrMIBNotifs, cdstvBWMgrSyncThreadPool=cdstvBWMgrSyncThreadPool, ciscoCdstvBwmgrMIB=ciscoCdstvBwmgrMIB, cdstvBWMgrAddressType=cdstvBWMgrAddressType, ciscoCdstvBWMgrMIBCompliances=ciscoCdstvBWMgrMIBCompliances, ciscoCdstvBWMgrMIBObjects=ciscoCdstvBWMgrMIBObjects)
