#
# PySNMP MIB module CISCO-AAL5-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-AAL5-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:24 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
aal5VccEntry, = mibBuilder.importSymbols("ATM-MIB", "aal5VccEntry")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoAal5MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 66))
ciscoAal5MIB.setRevisions(('2003-09-22 00:00', '2002-10-17 00:00', '1996-11-15 00:00',))
if mibBuilder.loadTexts: ciscoAal5MIB.setLastUpdated('200309220000Z')
if mibBuilder.loadTexts: ciscoAal5MIB.setOrganization('Cisco Systems, Inc.')
ciscoAal5MIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 66, 1))
cAal5Connections = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1))
cAal5VccTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1), )
if mibBuilder.loadTexts: cAal5VccTable.setStatus('current')
cAal5VccEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1), )
aal5VccEntry.registerAugmentions(("CISCO-AAL5-MIB", "cAal5VccEntry"))
cAal5VccEntry.setIndexNames(*aal5VccEntry.getIndexNames())
if mibBuilder.loadTexts: cAal5VccEntry.setStatus('current')
cAal5VccInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 1), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccInPkts.setStatus('current')
cAal5VccOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 2), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccOutPkts.setStatus('current')
cAal5VccInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 3), Counter32()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccInOctets.setStatus('current')
cAal5VccOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 4), Counter32()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccOutOctets.setStatus('current')
cAal5VccInDroppedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 5), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccInDroppedPkts.setStatus('current')
cAal5VccOutDroppedPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 6), Counter32()).setUnits('packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccOutDroppedPkts.setStatus('current')
cAal5VccInDroppedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 7), Counter32()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccInDroppedOctets.setStatus('current')
cAal5VccOutDroppedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 8), Counter32()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccOutDroppedOctets.setStatus('current')
cAal5VccHCInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccHCInPkts.setStatus('current')
cAal5VccHCOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccHCOutPkts.setStatus('current')
cAal5VccHCInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccHCInOctets.setStatus('current')
cAal5VccHCOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cAal5VccHCOutOctets.setStatus('current')
ciscoAal5MIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 66, 3))
ciscoAal5MIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 66, 3, 1))
ciscoAal5MIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 66, 3, 2))
ciscoAal5MIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 66, 3, 1, 1)).setObjects(("CISCO-AAL5-MIB", "ciscoAal5MIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAal5MIBCompliance = ciscoAal5MIBCompliance.setStatus('deprecated')
ciscoAal5MIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 66, 3, 1, 2)).setObjects(("CISCO-AAL5-MIB", "ciscoAal5MIBGroup"), ("CISCO-AAL5-MIB", "ciscoAal5VcStatsExtMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAal5MIBComplianceRev1 = ciscoAal5MIBComplianceRev1.setStatus('deprecated')
ciscoAal5MIBComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 66, 3, 1, 3)).setObjects(("CISCO-AAL5-MIB", "ciscoAal5MIBGroup"), ("CISCO-AAL5-MIB", "ciscoAal5VcStatsExtMIBGroup"), ("CISCO-AAL5-MIB", "ciscoAal5MIBHCGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAal5MIBComplianceRev2 = ciscoAal5MIBComplianceRev2.setStatus('current')
ciscoAal5MIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 66, 3, 2, 1)).setObjects(("CISCO-AAL5-MIB", "cAal5VccInPkts"), ("CISCO-AAL5-MIB", "cAal5VccOutPkts"), ("CISCO-AAL5-MIB", "cAal5VccInOctets"), ("CISCO-AAL5-MIB", "cAal5VccOutOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAal5MIBGroup = ciscoAal5MIBGroup.setStatus('current')
ciscoAal5VcStatsExtMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 66, 3, 2, 2)).setObjects(("CISCO-AAL5-MIB", "cAal5VccInDroppedPkts"), ("CISCO-AAL5-MIB", "cAal5VccOutDroppedPkts"), ("CISCO-AAL5-MIB", "cAal5VccInDroppedOctets"), ("CISCO-AAL5-MIB", "cAal5VccOutDroppedOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAal5VcStatsExtMIBGroup = ciscoAal5VcStatsExtMIBGroup.setStatus('current')
ciscoAal5MIBHCGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 66, 3, 2, 3)).setObjects(("CISCO-AAL5-MIB", "cAal5VccHCInPkts"), ("CISCO-AAL5-MIB", "cAal5VccHCOutPkts"), ("CISCO-AAL5-MIB", "cAal5VccHCInOctets"), ("CISCO-AAL5-MIB", "cAal5VccHCOutOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAal5MIBHCGroup = ciscoAal5MIBHCGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-AAL5-MIB", cAal5VccHCOutOctets=cAal5VccHCOutOctets, cAal5VccOutPkts=cAal5VccOutPkts, cAal5VccInDroppedPkts=cAal5VccInDroppedPkts, cAal5VccTable=cAal5VccTable, cAal5VccEntry=cAal5VccEntry, cAal5VccHCInPkts=cAal5VccHCInPkts, cAal5VccHCOutPkts=cAal5VccHCOutPkts, ciscoAal5MIBConformance=ciscoAal5MIBConformance, ciscoAal5MIBComplianceRev1=ciscoAal5MIBComplianceRev1, PYSNMP_MODULE_ID=ciscoAal5MIB, cAal5VccOutDroppedPkts=cAal5VccOutDroppedPkts, cAal5VccHCInOctets=cAal5VccHCInOctets, ciscoAal5MIBGroup=ciscoAal5MIBGroup, cAal5VccOutDroppedOctets=cAal5VccOutDroppedOctets, cAal5VccOutOctets=cAal5VccOutOctets, ciscoAal5MIBComplianceRev2=ciscoAal5MIBComplianceRev2, cAal5Connections=cAal5Connections, cAal5VccInOctets=cAal5VccInOctets, ciscoAal5MIB=ciscoAal5MIB, cAal5VccInPkts=cAal5VccInPkts, ciscoAal5VcStatsExtMIBGroup=ciscoAal5VcStatsExtMIBGroup, ciscoAal5MIBCompliance=ciscoAal5MIBCompliance, ciscoAal5MIBObjects=ciscoAal5MIBObjects, ciscoAal5MIBHCGroup=ciscoAal5MIBHCGroup, ciscoAal5MIBGroups=ciscoAal5MIBGroups, ciscoAal5MIBCompliances=ciscoAal5MIBCompliances, cAal5VccInDroppedOctets=cAal5VccInDroppedOctets)
