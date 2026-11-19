#
# PySNMP MIB module CISCO-PMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-PMON-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoInterfaceIndexList, = mibBuilder.importSymbols("CISCO-TC", "CiscoInterfaceIndexList")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPmonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 779))
ciscoPmonMIB.setRevisions(('2012-01-03 00:00',))
if mibBuilder.loadTexts: ciscoPmonMIB.setLastUpdated('201201030000Z')
if mibBuilder.loadTexts: ciscoPmonMIB.setOrganization('Cisco Systems, Inc.')
ciscoPmonMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 779, 0))
ciscoPmonMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 779, 1))
ciscoPmonMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 779, 2))
ciscoPmonStatsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 779, 1, 1))
ciscoPmonPortGroupStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 779, 1, 1, 1), )
if mibBuilder.loadTexts: ciscoPmonPortGroupStatsTable.setStatus('current')
ciscoPmonPortGroupStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 779, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-PMON-MIB", "ciscoPmonPortGroupStatsType"), (0, "CISCO-PMON-MIB", "ciscoPmonPortGroupIndex"))
if mibBuilder.loadTexts: ciscoPmonPortGroupStatsEntry.setStatus('current')
ciscoPmonPortGroupStatsType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 779, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("errPktsFromPort", 1), ("errPktsToXbar", 2), ("errPktsFromXbar", 3))))
if mibBuilder.loadTexts: ciscoPmonPortGroupStatsType.setStatus('current')
ciscoPmonPortGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 779, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: ciscoPmonPortGroupIndex.setStatus('current')
ciscoPmonPortGroupIfIndexList = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 779, 1, 1, 1, 1, 3), CiscoInterfaceIndexList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoPmonPortGroupIfIndexList.setStatus('current')
ciscoPmonPortGroupStatsValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 779, 1, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoPmonPortGroupStatsValue.setStatus('current')
ciscoPmonMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 779, 2, 1))
ciscoPmonMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 779, 2, 2))
ciscoPmonMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 779, 2, 1, 1)).setObjects(("CISCO-PMON-MIB", "ciscoPmonPortGroupStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPmonMIBCompliance = ciscoPmonMIBCompliance.setStatus('current')
ciscoPmonPortGroupStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 779, 2, 2, 1)).setObjects(("CISCO-PMON-MIB", "ciscoPmonPortGroupIfIndexList"), ("CISCO-PMON-MIB", "ciscoPmonPortGroupStatsValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPmonPortGroupStatsGroup = ciscoPmonPortGroupStatsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-PMON-MIB", ciscoPmonPortGroupStatsEntry=ciscoPmonPortGroupStatsEntry, ciscoPmonPortGroupStatsGroup=ciscoPmonPortGroupStatsGroup, ciscoPmonPortGroupStatsTable=ciscoPmonPortGroupStatsTable, ciscoPmonMIBNotifs=ciscoPmonMIBNotifs, ciscoPmonStatsMIBObjects=ciscoPmonStatsMIBObjects, ciscoPmonMIB=ciscoPmonMIB, ciscoPmonPortGroupIndex=ciscoPmonPortGroupIndex, ciscoPmonMIBGroups=ciscoPmonMIBGroups, ciscoPmonMIBCompliances=ciscoPmonMIBCompliances, ciscoPmonMIBObjects=ciscoPmonMIBObjects, ciscoPmonMIBConformance=ciscoPmonMIBConformance, ciscoPmonMIBCompliance=ciscoPmonMIBCompliance, PYSNMP_MODULE_ID=ciscoPmonMIB, ciscoPmonPortGroupIfIndexList=ciscoPmonPortGroupIfIndexList, ciscoPmonPortGroupStatsValue=ciscoPmonPortGroupStatsValue, ciscoPmonPortGroupStatsType=ciscoPmonPortGroupStatsType)
