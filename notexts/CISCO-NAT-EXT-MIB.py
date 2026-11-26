#
# PySNMP MIB module CISCO-NAT-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-NAT-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoNATExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 532))
ciscoNATExtMIB.setRevisions(('2006-06-05 00:00',))
if mibBuilder.loadTexts: ciscoNATExtMIB.setLastUpdated('200606050000Z')
if mibBuilder.loadTexts: ciscoNATExtMIB.setOrganization('Cisco Systems, Inc.')
ciscoNatExtMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 532, 0))
ciscoNatExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 532, 1))
ciscoNatExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 532, 2))
cneAddrTranslationStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 532, 1, 1), )
if mibBuilder.loadTexts: cneAddrTranslationStatsTable.setStatus('current')
cneAddrTranslationStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 532, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cneAddrTranslationStatsEntry.setStatus('current')
cneAddrTranslationNumActive = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 532, 1, 1, 1, 1), Gauge32()).setUnits('Number of address translation entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: cneAddrTranslationNumActive.setStatus('current')
cneAddrTranslationNumPeak = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 532, 1, 1, 1, 2), Unsigned32()).setUnits('Number of address translation entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: cneAddrTranslationNumPeak.setStatus('current')
cneAddrTranslation1min = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 532, 1, 1, 1, 3), Gauge32()).setUnits('Address translation entries per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cneAddrTranslation1min.setStatus('current')
cneAddrTranslation5min = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 532, 1, 1, 1, 4), Gauge32()).setUnits('Address translation entries per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: cneAddrTranslation5min.setStatus('current')
ciscoNatExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 532, 2, 1))
ciscoNatExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 532, 2, 2))
ciscoNatExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 532, 2, 1, 1)).setObjects(("CISCO-NAT-EXT-MIB", "ciscoNatExtAddrTransStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNatExtMIBCompliance = ciscoNatExtMIBCompliance.setStatus('current')
ciscoNatExtAddrTransStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 532, 2, 2, 1)).setObjects(("CISCO-NAT-EXT-MIB", "cneAddrTranslationNumActive"), ("CISCO-NAT-EXT-MIB", "cneAddrTranslationNumPeak"), ("CISCO-NAT-EXT-MIB", "cneAddrTranslation1min"), ("CISCO-NAT-EXT-MIB", "cneAddrTranslation5min"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNatExtAddrTransStatsGroup = ciscoNatExtAddrTransStatsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-NAT-EXT-MIB", ciscoNatExtMIBConformance=ciscoNatExtMIBConformance, ciscoNatExtMIBCompliance=ciscoNatExtMIBCompliance, ciscoNatExtAddrTransStatsGroup=ciscoNatExtAddrTransStatsGroup, cneAddrTranslation5min=cneAddrTranslation5min, cneAddrTranslation1min=cneAddrTranslation1min, cneAddrTranslationNumPeak=cneAddrTranslationNumPeak, ciscoNatExtMIBNotifs=ciscoNatExtMIBNotifs, ciscoNATExtMIB=ciscoNATExtMIB, PYSNMP_MODULE_ID=ciscoNATExtMIB, cneAddrTranslationStatsTable=cneAddrTranslationStatsTable, ciscoNatExtMIBObjects=ciscoNatExtMIBObjects, cneAddrTranslationStatsEntry=cneAddrTranslationStatsEntry, cneAddrTranslationNumActive=cneAddrTranslationNumActive, ciscoNatExtMIBCompliances=ciscoNatExtMIBCompliances, ciscoNatExtMIBGroups=ciscoNatExtMIBGroups)
