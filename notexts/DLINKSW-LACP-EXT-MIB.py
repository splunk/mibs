#
# PySNMP MIB module DLINKSW-LACP-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dlink/DLINKSW-LACP-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:46 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, TimeTicks, ModuleIdentity, NotificationType, ObjectIdentity, Unsigned32, MibIdentifier, Gauge32, Counter32, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "TimeTicks", "ModuleIdentity", "NotificationType", "ObjectIdentity", "Unsigned32", "MibIdentifier", "Gauge32", "Counter32", "Counter64", "IpAddress")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
dlinkSwLacpExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 14, 4))
dlinkSwLacpExtMIB.setRevisions(('2013-01-18 00:00',))
if mibBuilder.loadTexts: dlinkSwLacpExtMIB.setLastUpdated('201301180000Z')
if mibBuilder.loadTexts: dlinkSwLacpExtMIB.setOrganization('D-Link Corp.')
dLacpExtMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 4, 0))
dLacpExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 4, 1))
dLacpExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 4, 2))
dLacpExtLoadBalanceAlgorithm = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("dstIp", 1), ("dstMac", 2), ("srcDstIp", 3), ("srcDstMac", 4), ("srcIp", 5), ("srcMac", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dLacpExtLoadBalanceAlgorithm.setStatus('current')
dLacpExtGroupTable = MibTable((1, 3, 6, 1, 4, 1, 171, 14, 4, 1, 2), )
if mibBuilder.loadTexts: dLacpExtGroupTable.setStatus('current')
dLacpExtGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 14, 4, 1, 2, 1), ).setIndexNames((0, "DLINKSW-LACP-EXT-MIB", "dLacpExtGroupChannelNo"))
if mibBuilder.loadTexts: dLacpExtGroupEntry.setStatus('current')
dLacpExtGroupChannelNo = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 4, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: dLacpExtGroupChannelNo.setStatus('current')
dLacpExtGroupIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 4, 1, 2, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dLacpExtGroupIfIndex.setStatus('current')
dLacpExtGroupType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 4, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("lacp", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dLacpExtGroupType.setStatus('current')
dLacpExtGroupMemberPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 4, 1, 2, 1, 4), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dLacpExtGroupMemberPorts.setStatus('current')
dLacpExtGroupActiveMemberPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 4, 1, 2, 1, 5), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dLacpExtGroupActiveMemberPorts.setStatus('current')
dLacpExtGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 4, 1, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dLacpExtGroupRowStatus.setStatus('current')
dLacpExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 4, 2, 1))
dLacpExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 14, 4, 2, 1, 1)).setObjects(("DLINKSW-LACP-EXT-MIB", "dLacpExtAlgGroup"), ("DLINKSW-LACP-EXT-MIB", "dLacpExtChannelGrpInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dLacpExtCompliance = dLacpExtCompliance.setStatus('current')
dLacpExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 4, 2, 2))
dLacpExtAlgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 4, 2, 2, 1)).setObjects(("DLINKSW-LACP-EXT-MIB", "dLacpExtLoadBalanceAlgorithm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dLacpExtAlgGroup = dLacpExtAlgGroup.setStatus('current')
dLacpExtChannelGrpInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 4, 2, 2, 2)).setObjects(("DLINKSW-LACP-EXT-MIB", "dLacpExtGroupIfIndex"), ("DLINKSW-LACP-EXT-MIB", "dLacpExtGroupType"), ("DLINKSW-LACP-EXT-MIB", "dLacpExtGroupMemberPorts"), ("DLINKSW-LACP-EXT-MIB", "dLacpExtGroupActiveMemberPorts"), ("DLINKSW-LACP-EXT-MIB", "dLacpExtGroupRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dLacpExtChannelGrpInfoGroup = dLacpExtChannelGrpInfoGroup.setStatus('current')
mibBuilder.exportSymbols("DLINKSW-LACP-EXT-MIB", dLacpExtGroupEntry=dLacpExtGroupEntry, dlinkSwLacpExtMIB=dlinkSwLacpExtMIB, dLacpExtGroupIfIndex=dLacpExtGroupIfIndex, dLacpExtGroupChannelNo=dLacpExtGroupChannelNo, dLacpExtCompliances=dLacpExtCompliances, dLacpExtGroupActiveMemberPorts=dLacpExtGroupActiveMemberPorts, dLacpExtGroupTable=dLacpExtGroupTable, dLacpExtAlgGroup=dLacpExtAlgGroup, dLacpExtGroups=dLacpExtGroups, dLacpExtChannelGrpInfoGroup=dLacpExtChannelGrpInfoGroup, dLacpExtMIBNotifications=dLacpExtMIBNotifications, dLacpExtLoadBalanceAlgorithm=dLacpExtLoadBalanceAlgorithm, dLacpExtGroupType=dLacpExtGroupType, dLacpExtCompliance=dLacpExtCompliance, dLacpExtMIBConformance=dLacpExtMIBConformance, dLacpExtMIBObjects=dLacpExtMIBObjects, dLacpExtGroupRowStatus=dLacpExtGroupRowStatus, PYSNMP_MODULE_ID=dlinkSwLacpExtMIB, dLacpExtGroupMemberPorts=dLacpExtGroupMemberPorts)
