#
# PySNMP MIB module CISCO-TCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-TCP-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:24 2026
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
tcpConnEntry, = mibBuilder.importSymbols("TCP-MIB", "tcpConnEntry")
ciscoTcpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 6))
ciscoTcpMIB.setRevisions(('2001-11-12 00:00', '1996-12-03 00:00', '1994-07-21 00:00',))
if mibBuilder.loadTexts: ciscoTcpMIB.setLastUpdated('200111120000Z')
if mibBuilder.loadTexts: ciscoTcpMIB.setOrganization('Cisco Systems, Inc.')
ciscoTcpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 6, 1))
ciscoTcpConnTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1), )
if mibBuilder.loadTexts: ciscoTcpConnTable.setStatus('current')
ciscoTcpConnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1), )
tcpConnEntry.registerAugmentions(("CISCO-TCP-MIB", "ciscoTcpConnEntry"))
ciscoTcpConnEntry.setIndexNames(*tcpConnEntry.getIndexNames())
if mibBuilder.loadTexts: ciscoTcpConnEntry.setStatus('current')
ciscoTcpConnInBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoTcpConnInBytes.setStatus('current')
ciscoTcpConnOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoTcpConnOutBytes.setStatus('current')
ciscoTcpConnInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoTcpConnInPkts.setStatus('current')
ciscoTcpConnOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoTcpConnOutPkts.setStatus('current')
ciscoTcpConnElapsed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoTcpConnElapsed.setStatus('current')
ciscoTcpConnSRTT = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1, 6), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoTcpConnSRTT.setStatus('current')
ciscoTcpConnRetransPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoTcpConnRetransPkts.setStatus('current')
ciscoTcpConnFastRetransPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoTcpConnFastRetransPkts.setStatus('current')
ciscoTcpConnRto = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 6, 1, 1, 1, 9), Integer32()).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoTcpConnRto.setStatus('current')
ciscoTcpMIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 6, 2))
ciscoTcpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 6, 3))
ciscoTcpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 6, 3, 1))
ciscoTcpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 6, 3, 2))
ciscoTcpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 6, 3, 1, 1)).setObjects(("CISCO-TCP-MIB", "ciscoTcpMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpMIBCompliance = ciscoTcpMIBCompliance.setStatus('deprecated')
ciscoTcpMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 6, 3, 1, 2)).setObjects(("CISCO-TCP-MIB", "ciscoTcpMIBGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpMIBComplianceRev1 = ciscoTcpMIBComplianceRev1.setStatus('current')
ciscoTcpMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 6, 3, 2, 1)).setObjects(("CISCO-TCP-MIB", "ciscoTcpConnInBytes"), ("CISCO-TCP-MIB", "ciscoTcpConnOutBytes"), ("CISCO-TCP-MIB", "ciscoTcpConnInPkts"), ("CISCO-TCP-MIB", "ciscoTcpConnOutPkts"), ("CISCO-TCP-MIB", "ciscoTcpConnElapsed"), ("CISCO-TCP-MIB", "ciscoTcpConnSRTT"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpMIBGroup = ciscoTcpMIBGroup.setStatus('deprecated')
ciscoTcpMIBGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 6, 3, 2, 2)).setObjects(("CISCO-TCP-MIB", "ciscoTcpConnInBytes"), ("CISCO-TCP-MIB", "ciscoTcpConnOutBytes"), ("CISCO-TCP-MIB", "ciscoTcpConnInPkts"), ("CISCO-TCP-MIB", "ciscoTcpConnOutPkts"), ("CISCO-TCP-MIB", "ciscoTcpConnElapsed"), ("CISCO-TCP-MIB", "ciscoTcpConnSRTT"), ("CISCO-TCP-MIB", "ciscoTcpConnRto"), ("CISCO-TCP-MIB", "ciscoTcpConnRetransPkts"), ("CISCO-TCP-MIB", "ciscoTcpConnFastRetransPkts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTcpMIBGroupRev1 = ciscoTcpMIBGroupRev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-TCP-MIB", ciscoTcpMIBComplianceRev1=ciscoTcpMIBComplianceRev1, ciscoTcpMIB=ciscoTcpMIB, ciscoTcpConnTable=ciscoTcpConnTable, ciscoTcpConnElapsed=ciscoTcpConnElapsed, ciscoTcpMIBGroup=ciscoTcpMIBGroup, ciscoTcpConnRetransPkts=ciscoTcpConnRetransPkts, ciscoTcpConnOutPkts=ciscoTcpConnOutPkts, ciscoTcpMIBGroupRev1=ciscoTcpMIBGroupRev1, ciscoTcpMIBCompliances=ciscoTcpMIBCompliances, ciscoTcpMIBTraps=ciscoTcpMIBTraps, ciscoTcpConnEntry=ciscoTcpConnEntry, PYSNMP_MODULE_ID=ciscoTcpMIB, ciscoTcpConnRto=ciscoTcpConnRto, ciscoTcpConnOutBytes=ciscoTcpConnOutBytes, ciscoTcpMIBConformance=ciscoTcpMIBConformance, ciscoTcpConnSRTT=ciscoTcpConnSRTT, ciscoTcpMIBCompliance=ciscoTcpMIBCompliance, ciscoTcpConnInBytes=ciscoTcpConnInBytes, ciscoTcpMIBGroups=ciscoTcpMIBGroups, ciscoTcpMIBObjects=ciscoTcpMIBObjects, ciscoTcpConnFastRetransPkts=ciscoTcpConnFastRetransPkts, ciscoTcpConnInPkts=ciscoTcpConnInPkts)
