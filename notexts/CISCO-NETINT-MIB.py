#
# PySNMP MIB module CISCO-NETINT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-NETINT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoNetintMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 490))
ciscoNetintMIB.setRevisions(('2005-09-26 00:00',))
if mibBuilder.loadTexts: ciscoNetintMIB.setLastUpdated('200509260000Z')
if mibBuilder.loadTexts: ciscoNetintMIB.setOrganization('Cisco Systems, Inc.')
ciscoNetintMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 490, 0))
ciscoNetintMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 490, 1))
ciscoNetintMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 490, 2))
cniThrottle = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 490, 1, 1))
cniThrottleTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 490, 1, 1, 1), )
if mibBuilder.loadTexts: cniThrottleTable.setStatus('current')
cniThrottleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 490, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cniThrottleEntry.setStatus('current')
cniThrottleCount = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 490, 1, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cniThrottleCount.setStatus('current')
ciscoNetintMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 490, 2, 1))
ciscoNetintMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 490, 2, 2))
ciscoNetintMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 490, 2, 1, 1)).setObjects(("CISCO-NETINT-MIB", "ciscoThrottleGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNetintMIBCompliance = ciscoNetintMIBCompliance.setStatus('current')
ciscoThrottleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 490, 2, 2, 1)).setObjects(("CISCO-NETINT-MIB", "cniThrottleCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoThrottleGroup = ciscoThrottleGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-NETINT-MIB", ciscoNetintMIBNotifs=ciscoNetintMIBNotifs, cniThrottleCount=cniThrottleCount, ciscoNetintMIBGroups=ciscoNetintMIBGroups, cniThrottle=cniThrottle, PYSNMP_MODULE_ID=ciscoNetintMIB, ciscoNetintMIBConformance=ciscoNetintMIBConformance, ciscoThrottleGroup=ciscoThrottleGroup, ciscoNetintMIBObjects=ciscoNetintMIBObjects, cniThrottleTable=cniThrottleTable, cniThrottleEntry=cniThrottleEntry, ciscoNetintMIB=ciscoNetintMIB, ciscoNetintMIBCompliances=ciscoNetintMIBCompliances, ciscoNetintMIBCompliance=ciscoNetintMIBCompliance)
