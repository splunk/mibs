#
# PySNMP MIB module CISCO-GPRS-ISGSN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-GPRS-ISGSN-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:23 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
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
mibBuilder.exportSymbols("CISCO-GPRS-ISGSN-MIB", cgprsIsgsnTxOctetCountToTnode=cgprsIsgsnTxOctetCountToTnode, ciscoGprsIsgsnConformances=ciscoGprsIsgsnConformances, cgprsIsgsnTxPacketCountToTnode=cgprsIsgsnTxPacketCountToTnode, ciscoGprsIsgsnMIBObjects=ciscoGprsIsgsnMIBObjects, cgprsIsgsnRxOctetCountFromTnode=cgprsIsgsnRxOctetCountFromTnode, cgprsIsgsnStatsGroup=cgprsIsgsnStatsGroup, cgprsIsgsnErrorCountRxFromTnode=cgprsIsgsnErrorCountRxFromTnode, cgprsIsgsnCompliance1=cgprsIsgsnCompliance1, cgprsIsgsnCompliances=cgprsIsgsnCompliances, cgprsIsgsnErrorCountRxToTnode=cgprsIsgsnErrorCountRxToTnode, cgprsIsgsnRxPacketCountFromTnode=cgprsIsgsnRxPacketCountFromTnode, ciscoGprsIsgsnMIB=ciscoGprsIsgsnMIB, PYSNMP_MODULE_ID=ciscoGprsIsgsnMIB, ciscoGprsIsgsnStats=ciscoGprsIsgsnStats, cgprsIsgsnGroups=cgprsIsgsnGroups)
