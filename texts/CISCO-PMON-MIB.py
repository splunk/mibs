#
# PySNMP MIB module CISCO-PMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-PMON-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:13 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoInterfaceIndexList, = mibBuilder.importSymbols("CISCO-TC", "CiscoInterfaceIndexList")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, MibIdentifier, NotificationType, Unsigned32, ObjectIdentity, IpAddress, iso, TimeTicks, Counter32, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "ObjectIdentity", "IpAddress", "iso", "TimeTicks", "Counter32", "ModuleIdentity", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPmonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 779))
ciscoPmonMIB.setRevisions(('2012-01-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPmonMIB.setRevisionsDescriptions(('Latest version of this MIB module.',))
if mibBuilder.loadTexts: ciscoPmonMIB.setLastUpdated('201201030000Z')
if mibBuilder.loadTexts: ciscoPmonMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPmonMIB.setContactInfo('Cisco Systems\n            Customer Service\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n            Tel: +1 800 553-NETS\n            E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoPmonMIB.setDescription('This MIB module is for providing the port monitoring\n         information.')
ciscoPmonMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 779, 0))
ciscoPmonMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 779, 1))
ciscoPmonMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 779, 2))
ciscoPmonStatsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 779, 1, 1))
ciscoPmonPortGroupStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 779, 1, 1, 1), )
if mibBuilder.loadTexts: ciscoPmonPortGroupStatsTable.setStatus('current')
if mibBuilder.loadTexts: ciscoPmonPortGroupStatsTable.setDescription('Contains statistics information for the physical modules\n         and port groups.')
ciscoPmonPortGroupStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 779, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-PMON-MIB", "ciscoPmonPortGroupStatsType"), (0, "CISCO-PMON-MIB", "ciscoPmonPortGroupIndex"))
if mibBuilder.loadTexts: ciscoPmonPortGroupStatsEntry.setStatus('current')
if mibBuilder.loadTexts: ciscoPmonPortGroupStatsEntry.setDescription('Each entry contains the statistics information for a\n         a specific physical module as indicated by the value of\n         entPhysicalIndex, statistics type, and a port group.')
ciscoPmonPortGroupStatsType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 779, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("errPktsFromPort", 1), ("errPktsToXbar", 2), ("errPktsFromXbar", 3))))
if mibBuilder.loadTexts: ciscoPmonPortGroupStatsType.setStatus('current')
if mibBuilder.loadTexts: ciscoPmonPortGroupStatsType.setDescription("Indicates the type of statistics. This object has three\n         defined values:\n         \n\n         - 'errPktsFromPort', which indicates a counter of error packets\n         received from a port;\n\n         - 'errPktsToXbar', which indicates a counter of error packets\n         sent to XBAR;\n\n         - 'errPktsFromXbar', which indicates a counter of error packets\n         received from XBAR.")
ciscoPmonPortGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 779, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: ciscoPmonPortGroupIndex.setStatus('current')
if mibBuilder.loadTexts: ciscoPmonPortGroupIndex.setDescription('A unique value assigned to a specific port group for a\n        given module and statistics type.')
ciscoPmonPortGroupIfIndexList = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 779, 1, 1, 1, 1, 3), CiscoInterfaceIndexList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoPmonPortGroupIfIndexList.setStatus('current')
if mibBuilder.loadTexts: ciscoPmonPortGroupIfIndexList.setDescription('Contains ifIndex values for the list of the ports in\n        the port group.')
ciscoPmonPortGroupStatsValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 779, 1, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoPmonPortGroupStatsValue.setStatus('current')
if mibBuilder.loadTexts: ciscoPmonPortGroupStatsValue.setDescription('The statistics value counted on this module, statistics type,\n        port group.')
ciscoPmonMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 779, 2, 1))
ciscoPmonMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 779, 2, 2))
ciscoPmonMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 779, 2, 1, 1)).setObjects(("CISCO-PMON-MIB", "ciscoPmonPortGroupStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPmonMIBCompliance = ciscoPmonMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoPmonMIBCompliance.setDescription('The compliance statement for entities implementing the\n         Port Monitor MIB.')
ciscoPmonPortGroupStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 779, 2, 2, 1)).setObjects(("CISCO-PMON-MIB", "ciscoPmonPortGroupIfIndexList"), ("CISCO-PMON-MIB", "ciscoPmonPortGroupStatsValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPmonPortGroupStatsGroup = ciscoPmonPortGroupStatsGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoPmonPortGroupStatsGroup.setDescription('A collection of objects that provides port group statistics\n        information.')
mibBuilder.exportSymbols("CISCO-PMON-MIB", ciscoPmonPortGroupStatsValue=ciscoPmonPortGroupStatsValue, ciscoPmonMIBGroups=ciscoPmonMIBGroups, ciscoPmonMIBNotifs=ciscoPmonMIBNotifs, ciscoPmonPortGroupStatsTable=ciscoPmonPortGroupStatsTable, ciscoPmonPortGroupStatsGroup=ciscoPmonPortGroupStatsGroup, ciscoPmonMIBObjects=ciscoPmonMIBObjects, ciscoPmonPortGroupStatsEntry=ciscoPmonPortGroupStatsEntry, ciscoPmonStatsMIBObjects=ciscoPmonStatsMIBObjects, ciscoPmonPortGroupStatsType=ciscoPmonPortGroupStatsType, ciscoPmonMIBCompliance=ciscoPmonMIBCompliance, ciscoPmonMIB=ciscoPmonMIB, ciscoPmonMIBConformance=ciscoPmonMIBConformance, ciscoPmonPortGroupIfIndexList=ciscoPmonPortGroupIfIndexList, PYSNMP_MODULE_ID=ciscoPmonMIB, ciscoPmonPortGroupIndex=ciscoPmonPortGroupIndex, ciscoPmonMIBCompliances=ciscoPmonMIBCompliances)
