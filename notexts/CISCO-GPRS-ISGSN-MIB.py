#
# PySNMP MIB module CISCO-GPRS-ISGSN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-GPRS-ISGSN-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoGprsIsgsnMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 9992))
if mibBuilder.loadTexts: ciscoGprsIsgsnMIB.setLastUpdated('9810150000Z')
if mibBuilder.loadTexts: ciscoGprsIsgsnMIB.setOrganization('Cisco Systems, Inc.')
ciscoGprsIsgsnMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9992, 1))
ciscoGprsIsgsnStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9992, 1, 1))
cgprsIsgsnRxPacketCountFromTnode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9992, 1, 1, 1), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgprsIsgsnRxPacketCountFromTnode.setStatus('current')
cgprsIsgsnTxPacketCountToTnode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9992, 1, 1, 2), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgprsIsgsnTxPacketCountToTnode.setStatus('current')
cgprsIsgsnRxOctetCountFromTnode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9992, 1, 1, 3), Counter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgprsIsgsnRxOctetCountFromTnode.setStatus('current')
cgprsIsgsnTxOctetCountToTnode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9992, 1, 1, 4), Counter32()).setUnits('bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgprsIsgsnTxOctetCountToTnode.setStatus('current')
cgprsIsgsnErrorCountRxFromTnode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9992, 1, 1, 5), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgprsIsgsnErrorCountRxFromTnode.setStatus('current')
cgprsIsgsnErrorCountRxToTnode = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 9992, 1, 1, 6), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cgprsIsgsnErrorCountRxToTnode.setStatus('current')
ciscoGprsIsgsnConformances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9992, 3))
cgprsIsgsnGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9992, 3, 1))
cgprsIsgsnCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9992, 3, 2))
cgprsIsgsnCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 9992, 3, 2, 1)).setObjects(("CISCO-GPRS-ISGSN-MIB", "cgprsIsgsnStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsIsgsnCompliance1 = cgprsIsgsnCompliance1.setStatus('current')
cgprsIsgsnStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9992, 3, 1, 1)).setObjects(("CISCO-GPRS-ISGSN-MIB", "cgprsIsgsnRxPacketCountFromTnode"), ("CISCO-GPRS-ISGSN-MIB", "cgprsIsgsnTxPacketCountToTnode"), ("CISCO-GPRS-ISGSN-MIB", "cgprsIsgsnRxOctetCountFromTnode"), ("CISCO-GPRS-ISGSN-MIB", "cgprsIsgsnTxOctetCountToTnode"), ("CISCO-GPRS-ISGSN-MIB", "cgprsIsgsnErrorCountRxFromTnode"), ("CISCO-GPRS-ISGSN-MIB", "cgprsIsgsnErrorCountRxToTnode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsIsgsnStatsGroup = cgprsIsgsnStatsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-GPRS-ISGSN-MIB", cgprsIsgsnCompliance1=cgprsIsgsnCompliance1, ciscoGprsIsgsnMIB=ciscoGprsIsgsnMIB, cgprsIsgsnCompliances=cgprsIsgsnCompliances, cgprsIsgsnErrorCountRxFromTnode=cgprsIsgsnErrorCountRxFromTnode, cgprsIsgsnErrorCountRxToTnode=cgprsIsgsnErrorCountRxToTnode, cgprsIsgsnStatsGroup=cgprsIsgsnStatsGroup, ciscoGprsIsgsnMIBObjects=ciscoGprsIsgsnMIBObjects, PYSNMP_MODULE_ID=ciscoGprsIsgsnMIB, cgprsIsgsnGroups=cgprsIsgsnGroups, ciscoGprsIsgsnConformances=ciscoGprsIsgsnConformances, cgprsIsgsnTxPacketCountToTnode=cgprsIsgsnTxPacketCountToTnode, cgprsIsgsnRxOctetCountFromTnode=cgprsIsgsnRxOctetCountFromTnode, cgprsIsgsnRxPacketCountFromTnode=cgprsIsgsnRxPacketCountFromTnode, ciscoGprsIsgsnStats=ciscoGprsIsgsnStats, cgprsIsgsnTxOctetCountToTnode=cgprsIsgsnTxOctetCountToTnode)
