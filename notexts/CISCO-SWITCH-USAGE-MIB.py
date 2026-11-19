#
# PySNMP MIB module CISCO-SWITCH-USAGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SWITCH-USAGE-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSwitchUsageMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 201))
ciscoSwitchUsageMIB.setRevisions(('2001-05-02 00:00',))
if mibBuilder.loadTexts: ciscoSwitchUsageMIB.setLastUpdated('200105020000Z')
if mibBuilder.loadTexts: ciscoSwitchUsageMIB.setOrganization('Cisco Systems, Inc.')
ciscoSwitchUsageMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 201, 1))
ciscoSwitchUsageStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 201, 1, 1))
cswitchUsageStatTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 201, 1, 1, 1), )
if mibBuilder.loadTexts: cswitchUsageStatTable.setStatus('current')
cswitchUsageStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 201, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cswitchUsageStatEntry.setStatus('current')
cswitchUsageByIngrsIntfPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 201, 1, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cswitchUsageByIngrsIntfPkts.setStatus('current')
cswitchUsageByIngrsIntfHCPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 201, 1, 1, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cswitchUsageByIngrsIntfHCPkts.setStatus('current')
cswitchUsageByIngrsIntfOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 201, 1, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cswitchUsageByIngrsIntfOctets.setStatus('current')
cswitchUsageByIngrsIntfHCOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 201, 1, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cswitchUsageByIngrsIntfHCOctets.setStatus('current')
ciscoSwitchUsageMIBNotifyPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 201, 2))
ciscoSwitchUsageMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 201, 2, 0))
ciscoSwitchUsageMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 201, 3))
ciscoSwitchUsageMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 201, 3, 1))
ciscoSwitchUsageMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 201, 3, 2))
ciscoSwitchUsageMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 201, 3, 1, 1)).setObjects(("CISCO-SWITCH-USAGE-MIB", "ciscoSwitchUsageMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchUsageMIBCompliance = ciscoSwitchUsageMIBCompliance.setStatus('current')
ciscoSwitchUsageMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 201, 3, 2, 1)).setObjects(("CISCO-SWITCH-USAGE-MIB", "cswitchUsageByIngrsIntfPkts"), ("CISCO-SWITCH-USAGE-MIB", "cswitchUsageByIngrsIntfHCPkts"), ("CISCO-SWITCH-USAGE-MIB", "cswitchUsageByIngrsIntfOctets"), ("CISCO-SWITCH-USAGE-MIB", "cswitchUsageByIngrsIntfHCOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchUsageMIBGroup = ciscoSwitchUsageMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SWITCH-USAGE-MIB", ciscoSwitchUsageMIBGroups=ciscoSwitchUsageMIBGroups, ciscoSwitchUsageStats=ciscoSwitchUsageStats, cswitchUsageStatEntry=cswitchUsageStatEntry, cswitchUsageStatTable=cswitchUsageStatTable, ciscoSwitchUsageMIBGroup=ciscoSwitchUsageMIBGroup, ciscoSwitchUsageMIBConformance=ciscoSwitchUsageMIBConformance, cswitchUsageByIngrsIntfHCPkts=cswitchUsageByIngrsIntfHCPkts, ciscoSwitchUsageMIBNotifyPrefix=ciscoSwitchUsageMIBNotifyPrefix, ciscoSwitchUsageMIB=ciscoSwitchUsageMIB, cswitchUsageByIngrsIntfHCOctets=cswitchUsageByIngrsIntfHCOctets, ciscoSwitchUsageMIBObjects=ciscoSwitchUsageMIBObjects, PYSNMP_MODULE_ID=ciscoSwitchUsageMIB, ciscoSwitchUsageMIBCompliances=ciscoSwitchUsageMIBCompliances, ciscoSwitchUsageMIBNotifications=ciscoSwitchUsageMIBNotifications, cswitchUsageByIngrsIntfPkts=cswitchUsageByIngrsIntfPkts, cswitchUsageByIngrsIntfOctets=cswitchUsageByIngrsIntfOctets, ciscoSwitchUsageMIBCompliance=ciscoSwitchUsageMIBCompliance)
