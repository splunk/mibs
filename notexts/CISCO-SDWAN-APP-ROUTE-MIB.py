#
# PySNMP MIB module CISCO-SDWAN-APP-ROUTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SDWAN-APP-ROUTE-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Gauge32, ModuleIdentity, Integer32, Bits, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Integer32", "Bits", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSdwanAppRouteMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 1001))
ciscoSdwanAppRouteMIB.setRevisions(('2021-01-26 00:00',))
if mibBuilder.loadTexts: ciscoSdwanAppRouteMIB.setLastUpdated('202101260000Z')
if mibBuilder.loadTexts: ciscoSdwanAppRouteMIB.setOrganization('Cisco Systems, Inc. ')
class UnsignedByte(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class UnsignedShort(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class String(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class InetAddressIP(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )
ciscoSdwanAppRouteMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1))
ciscoSdwanAppRouteMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 1001, 3))
appRouteStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2), )
if mibBuilder.loadTexts: appRouteStatisticsTable.setStatus('current')
appRouteStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1), ).setIndexNames((0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsSrcIp"), (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsDstIp"), (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsProto"), (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsSrcPort"), (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsDstPort"))
if mibBuilder.loadTexts: appRouteStatisticsEntry.setStatus('current')
appRouteStatisticsSrcIp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 1), InetAddressIP())
if mibBuilder.loadTexts: appRouteStatisticsSrcIp.setStatus('current')
appRouteStatisticsDstIp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 2), InetAddressIP())
if mibBuilder.loadTexts: appRouteStatisticsDstIp.setStatus('current')
appRouteStatisticsProto = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("gre", 1), ("ipsec", 2))))
if mibBuilder.loadTexts: appRouteStatisticsProto.setStatus('current')
appRouteStatisticsSrcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 4), UnsignedShort())
if mibBuilder.loadTexts: appRouteStatisticsSrcPort.setStatus('current')
appRouteStatisticsDstPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 5), UnsignedShort())
if mibBuilder.loadTexts: appRouteStatisticsDstPort.setStatus('current')
appRouteStatisticsRemoteSystemIp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 6), InetAddressIP()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsRemoteSystemIp.setStatus('current')
appRouteStatisticsLocalColor = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22))).clone(namedValues=NamedValues(("default", 1), ("mpls", 2), ("metroEthernet", 3), ("bizInternet", 4), ("publicInternet", 5), ("lte", 6), ("threeG", 7), ("red", 8), ("green", 9), ("blue", 10), ("gold", 11), ("silver", 12), ("bronze", 13), ("custom1", 14), ("custom2", 15), ("custom3", 16), ("private1", 17), ("private2", 18), ("private3", 19), ("private4", 20), ("private5", 21), ("private6", 22)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsLocalColor.setStatus('current')
appRouteStatisticsRemoteColor = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22))).clone(namedValues=NamedValues(("default", 1), ("mpls", 2), ("metroEthernet", 3), ("bizInternet", 4), ("publicInternet", 5), ("lte", 6), ("threeG", 7), ("red", 8), ("green", 9), ("blue", 10), ("gold", 11), ("silver", 12), ("bronze", 13), ("custom1", 14), ("custom2", 15), ("custom3", 16), ("private1", 17), ("private2", 18), ("private3", 19), ("private4", 20), ("private5", 21), ("private6", 22)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsRemoteColor.setStatus('current')
appRouteStatisticsMeanLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 9), UnsignedByte()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsMeanLoss.setStatus('current')
appRouteStatisticsMeanLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsMeanLatency.setStatus('current')
appRouteStatisticsMeanJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsMeanJitter.setStatus('current')
appRouteStatisticsIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 3), )
if mibBuilder.loadTexts: appRouteStatisticsIntervalTable.setStatus('current')
appRouteStatisticsIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 3, 1), ).setIndexNames((0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsSrcIp"), (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsDstIp"), (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsProto"), (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsSrcPort"), (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsDstPort"), (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsIntervalIndex"))
if mibBuilder.loadTexts: appRouteStatisticsIntervalEntry.setStatus('current')
appRouteStatisticsIntervalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 3, 1, 1), UnsignedByte())
if mibBuilder.loadTexts: appRouteStatisticsIntervalIndex.setStatus('current')
appRouteStatisticsIntervalTotalPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsIntervalTotalPackets.setStatus('current')
appRouteStatisticsIntervalLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsIntervalLoss.setStatus('current')
appRouteStatisticsIntervalAverageLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 3, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsIntervalAverageLatency.setStatus('current')
appRouteStatisticsIntervalAverageJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 3, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsIntervalAverageJitter.setStatus('current')
appRouteStatisticsIntervalTxDataPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 3, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsIntervalTxDataPkts.setStatus('current')
appRouteStatisticsIntervalRxDataPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 3, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsIntervalRxDataPkts.setStatus('current')
appRouteStatisticsIntervalIpv6TxDataPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 3, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsIntervalIpv6TxDataPkts.setStatus('current')
appRouteStatisticsIntervalIpv6RxDataPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 3, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsIntervalIpv6RxDataPkts.setStatus('current')
appRouteSlaClassTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 4), )
if mibBuilder.loadTexts: appRouteSlaClassTable.setStatus('current')
appRouteSlaClassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 4, 1), ).setIndexNames((0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteSlaClassIndex"))
if mibBuilder.loadTexts: appRouteSlaClassEntry.setStatus('current')
appRouteSlaClassIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 4, 1, 1), UnsignedByte())
if mibBuilder.loadTexts: appRouteSlaClassIndex.setStatus('current')
appRouteSlaClassName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 4, 1, 2), String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteSlaClassName.setStatus('current')
appRouteSlaClassLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 4, 1, 3), UnsignedByte()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteSlaClassLoss.setStatus('current')
appRouteSlaClassLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 4, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteSlaClassLatency.setStatus('current')
appRouteSlaClassJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 4, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteSlaClassJitter.setStatus('current')
ciscoSdwanAppRouteMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 1001, 3, 1))
ciscoSdwanAppRouteMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 1001, 3, 2))
ciscoSdwanAppRouteMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 1001, 3, 1, 1)).setObjects(("CISCO-SDWAN-APP-ROUTE-MIB", "cSdwanAppRouteStatisticsGroup"), ("CISCO-SDWAN-APP-ROUTE-MIB", "cSdwanAppRouteStatisticsIntervalGroup"), ("CISCO-SDWAN-APP-ROUTE-MIB", "cSdwanAppRouteSlaClassGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSdwanAppRouteMIBCompliance = ciscoSdwanAppRouteMIBCompliance.setStatus('current')
cSdwanAppRouteStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 1001, 3, 2, 1)).setObjects(("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsRemoteSystemIp"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsLocalColor"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsRemoteColor"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsMeanLoss"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsMeanLatency"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsMeanJitter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSdwanAppRouteStatisticsGroup = cSdwanAppRouteStatisticsGroup.setStatus('current')
cSdwanAppRouteStatisticsIntervalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 1001, 3, 2, 2)).setObjects(("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsIntervalTotalPackets"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsIntervalLoss"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsIntervalAverageLatency"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsIntervalAverageJitter"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsIntervalTxDataPkts"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsIntervalRxDataPkts"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsIntervalIpv6TxDataPkts"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsIntervalIpv6RxDataPkts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSdwanAppRouteStatisticsIntervalGroup = cSdwanAppRouteStatisticsIntervalGroup.setStatus('current')
cSdwanAppRouteSlaClassGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 1001, 3, 2, 3)).setObjects(("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteSlaClassName"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteSlaClassLoss"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteSlaClassLatency"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteSlaClassJitter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSdwanAppRouteSlaClassGroup = cSdwanAppRouteSlaClassGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SDWAN-APP-ROUTE-MIB", appRouteStatisticsIntervalTable=appRouteStatisticsIntervalTable, appRouteStatisticsIntervalIndex=appRouteStatisticsIntervalIndex, appRouteStatisticsIntervalAverageLatency=appRouteStatisticsIntervalAverageLatency, ciscoSdwanAppRouteMIBGroups=ciscoSdwanAppRouteMIBGroups, appRouteSlaClassLatency=appRouteSlaClassLatency, appRouteStatisticsMeanJitter=appRouteStatisticsMeanJitter, cSdwanAppRouteStatisticsIntervalGroup=cSdwanAppRouteStatisticsIntervalGroup, appRouteStatisticsEntry=appRouteStatisticsEntry, appRouteSlaClassLoss=appRouteSlaClassLoss, appRouteStatisticsSrcIp=appRouteStatisticsSrcIp, appRouteStatisticsLocalColor=appRouteStatisticsLocalColor, appRouteStatisticsProto=appRouteStatisticsProto, ciscoSdwanAppRouteMIBCompliance=ciscoSdwanAppRouteMIBCompliance, appRouteStatisticsSrcPort=appRouteStatisticsSrcPort, UnsignedShort=UnsignedShort, cSdwanAppRouteStatisticsGroup=cSdwanAppRouteStatisticsGroup, ciscoSdwanAppRouteMIBConform=ciscoSdwanAppRouteMIBConform, PYSNMP_MODULE_ID=ciscoSdwanAppRouteMIB, appRouteStatisticsIntervalIpv6RxDataPkts=appRouteStatisticsIntervalIpv6RxDataPkts, appRouteStatisticsIntervalIpv6TxDataPkts=appRouteStatisticsIntervalIpv6TxDataPkts, ciscoSdwanAppRouteMIBObjects=ciscoSdwanAppRouteMIBObjects, appRouteSlaClassName=appRouteSlaClassName, appRouteStatisticsIntervalEntry=appRouteStatisticsIntervalEntry, appRouteStatisticsIntervalTxDataPkts=appRouteStatisticsIntervalTxDataPkts, appRouteStatisticsIntervalRxDataPkts=appRouteStatisticsIntervalRxDataPkts, appRouteStatisticsMeanLoss=appRouteStatisticsMeanLoss, UnsignedByte=UnsignedByte, appRouteStatisticsIntervalTotalPackets=appRouteStatisticsIntervalTotalPackets, appRouteSlaClassIndex=appRouteSlaClassIndex, appRouteStatisticsDstPort=appRouteStatisticsDstPort, appRouteStatisticsDstIp=appRouteStatisticsDstIp, appRouteSlaClassEntry=appRouteSlaClassEntry, String=String, cSdwanAppRouteSlaClassGroup=cSdwanAppRouteSlaClassGroup, InetAddressIP=InetAddressIP, ciscoSdwanAppRouteMIB=ciscoSdwanAppRouteMIB, appRouteSlaClassTable=appRouteSlaClassTable, appRouteStatisticsRemoteSystemIp=appRouteStatisticsRemoteSystemIp, ciscoSdwanAppRouteMIBCompliances=ciscoSdwanAppRouteMIBCompliances, appRouteStatisticsTable=appRouteStatisticsTable, appRouteStatisticsIntervalAverageJitter=appRouteStatisticsIntervalAverageJitter, appRouteSlaClassJitter=appRouteSlaClassJitter, appRouteStatisticsIntervalLoss=appRouteStatisticsIntervalLoss, appRouteStatisticsRemoteColor=appRouteStatisticsRemoteColor, appRouteStatisticsMeanLatency=appRouteStatisticsMeanLatency)
