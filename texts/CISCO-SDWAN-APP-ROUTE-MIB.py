#
# PySNMP MIB module CISCO-SDWAN-APP-ROUTE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SDWAN-APP-ROUTE-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:06 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSdwanAppRouteMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 1001))
ciscoSdwanAppRouteMIB.setRevisions(('2021-01-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSdwanAppRouteMIB.setRevisionsDescriptions(('Cisco SDWAN AppRoute Revision 0.0',))
if mibBuilder.loadTexts: ciscoSdwanAppRouteMIB.setLastUpdated('202101260000Z')
if mibBuilder.loadTexts: ciscoSdwanAppRouteMIB.setOrganization('Cisco Systems, Inc. ')
if mibBuilder.loadTexts: ciscoSdwanAppRouteMIB.setContactInfo('       Cisco Systems\n                    Customer Service\n\n            Postal: 170 W Tasman Drive\n                    San Jose, CA  95134\n                    USA\n\n               Tel: +1 800 553-NETS\n\n            E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSdwanAppRouteMIB.setDescription('This module defines the data model for Cisco SDWAN\n             application-aware routing operational data')
class UnsignedByte(TextualConvention, Unsigned32):
    description = 'xs:unsignedByte'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class UnsignedShort(TextualConvention, Unsigned32):
    description = 'xs:unsignedShort'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class String(TextualConvention, OctetString):
    description = 'xs:string'
    status = 'current'
    displayHint = '1t'

class InetAddressIP(TextualConvention, OctetString):
    description = 'confd:inetAddressIP'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )
ciscoSdwanAppRouteMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1))
ciscoSdwanAppRouteMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 1001, 3))
appRouteStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2), )
if mibBuilder.loadTexts: appRouteStatisticsTable.setStatus('current')
if mibBuilder.loadTexts: appRouteStatisticsTable.setDescription('Statisticst table')
appRouteStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1), ).setIndexNames((0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsSrcIp"), (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsDstIp"), (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsProto"), (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsSrcPort"), (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsDstPort"))
if mibBuilder.loadTexts: appRouteStatisticsEntry.setStatus('current')
if mibBuilder.loadTexts: appRouteStatisticsEntry.setDescription('Statisticst table entry')
appRouteStatisticsSrcIp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 1), InetAddressIP())
if mibBuilder.loadTexts: appRouteStatisticsSrcIp.setStatus('current')
if mibBuilder.loadTexts: appRouteStatisticsSrcIp.setDescription('Local TLOC IP address')
appRouteStatisticsDstIp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 2), InetAddressIP())
if mibBuilder.loadTexts: appRouteStatisticsDstIp.setStatus('current')
if mibBuilder.loadTexts: appRouteStatisticsDstIp.setDescription('Remote TLOC IP address')
appRouteStatisticsProto = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("gre", 1), ("ipsec", 2))))
if mibBuilder.loadTexts: appRouteStatisticsProto.setStatus('current')
if mibBuilder.loadTexts: appRouteStatisticsProto.setDescription('Protocol or encap')
appRouteStatisticsSrcPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 4), UnsignedShort())
if mibBuilder.loadTexts: appRouteStatisticsSrcPort.setStatus('current')
if mibBuilder.loadTexts: appRouteStatisticsSrcPort.setDescription('Local port number')
appRouteStatisticsDstPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 5), UnsignedShort())
if mibBuilder.loadTexts: appRouteStatisticsDstPort.setStatus('current')
if mibBuilder.loadTexts: appRouteStatisticsDstPort.setDescription('Remote port number')
appRouteStatisticsRemoteSystemIp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 6), InetAddressIP()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsRemoteSystemIp.setStatus('current')
if mibBuilder.loadTexts: appRouteStatisticsRemoteSystemIp.setDescription('Remote system IP address')
appRouteStatisticsLocalColor = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22))).clone(namedValues=NamedValues(("default", 1), ("mpls", 2), ("metroEthernet", 3), ("bizInternet", 4), ("publicInternet", 5), ("lte", 6), ("threeG", 7), ("red", 8), ("green", 9), ("blue", 10), ("gold", 11), ("silver", 12), ("bronze", 13), ("custom1", 14), ("custom2", 15), ("custom3", 16), ("private1", 17), ("private2", 18), ("private3", 19), ("private4", 20), ("private5", 21), ("private6", 22)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsLocalColor.setStatus('current')
if mibBuilder.loadTexts: appRouteStatisticsLocalColor.setDescription('Local TLOC color')
appRouteStatisticsRemoteColor = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22))).clone(namedValues=NamedValues(("default", 1), ("mpls", 2), ("metroEthernet", 3), ("bizInternet", 4), ("publicInternet", 5), ("lte", 6), ("threeG", 7), ("red", 8), ("green", 9), ("blue", 10), ("gold", 11), ("silver", 12), ("bronze", 13), ("custom1", 14), ("custom2", 15), ("custom3", 16), ("private1", 17), ("private2", 18), ("private3", 19), ("private4", 20), ("private5", 21), ("private6", 22)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsRemoteColor.setStatus('current')
if mibBuilder.loadTexts: appRouteStatisticsRemoteColor.setDescription('Remote TLOC color')
appRouteStatisticsMeanLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 9), UnsignedByte()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsMeanLoss.setStatus('current')
if mibBuilder.loadTexts: appRouteStatisticsMeanLoss.setDescription('Average loss in percentage \n                 across all the polling intervals')
appRouteStatisticsMeanLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsMeanLatency.setStatus('current')
if mibBuilder.loadTexts: appRouteStatisticsMeanLatency.setDescription('Average latency across all the polling intervals')
appRouteStatisticsMeanJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 2, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsMeanJitter.setStatus('current')
if mibBuilder.loadTexts: appRouteStatisticsMeanJitter.setDescription('Average jitter across all polling intervals')
appRouteStatisticsIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 3), )
if mibBuilder.loadTexts: appRouteStatisticsIntervalTable.setStatus('current')
if mibBuilder.loadTexts: appRouteStatisticsIntervalTable.setDescription('Statistics interval table')
appRouteStatisticsIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 3, 1), ).setIndexNames((0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsSrcIp"), (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsDstIp"), (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsProto"), (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsSrcPort"), (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsDstPort"), (0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsIntervalIndex"))
if mibBuilder.loadTexts: appRouteStatisticsIntervalEntry.setStatus('current')
if mibBuilder.loadTexts: appRouteStatisticsIntervalEntry.setDescription('Statistics interval table entry')
appRouteStatisticsIntervalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 3, 1, 1), UnsignedByte())
if mibBuilder.loadTexts: appRouteStatisticsIntervalIndex.setStatus('current')
if mibBuilder.loadTexts: appRouteStatisticsIntervalIndex.setDescription('Polling interval index')
appRouteStatisticsIntervalTotalPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsIntervalTotalPackets.setStatus('current')
if mibBuilder.loadTexts: appRouteStatisticsIntervalTotalPackets.setDescription('Total packets sent')
appRouteStatisticsIntervalLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsIntervalLoss.setStatus('current')
if mibBuilder.loadTexts: appRouteStatisticsIntervalLoss.setDescription('Packets lost')
appRouteStatisticsIntervalAverageLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 3, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsIntervalAverageLatency.setStatus('current')
if mibBuilder.loadTexts: appRouteStatisticsIntervalAverageLatency.setDescription('Average latency')
appRouteStatisticsIntervalAverageJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 3, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsIntervalAverageJitter.setStatus('current')
if mibBuilder.loadTexts: appRouteStatisticsIntervalAverageJitter.setDescription('Average jitter')
appRouteStatisticsIntervalTxDataPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 3, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsIntervalTxDataPkts.setStatus('current')
if mibBuilder.loadTexts: appRouteStatisticsIntervalTxDataPkts.setDescription('Data packets transmitted')
appRouteStatisticsIntervalRxDataPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 3, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsIntervalRxDataPkts.setStatus('current')
if mibBuilder.loadTexts: appRouteStatisticsIntervalRxDataPkts.setDescription('Data packets received')
appRouteStatisticsIntervalIpv6TxDataPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 3, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsIntervalIpv6TxDataPkts.setStatus('current')
if mibBuilder.loadTexts: appRouteStatisticsIntervalIpv6TxDataPkts.setDescription('IPv6 Data packets transmitted')
appRouteStatisticsIntervalIpv6RxDataPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 3, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteStatisticsIntervalIpv6RxDataPkts.setStatus('current')
if mibBuilder.loadTexts: appRouteStatisticsIntervalIpv6RxDataPkts.setDescription('IPv6 Data packets received')
appRouteSlaClassTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 4), )
if mibBuilder.loadTexts: appRouteSlaClassTable.setStatus('current')
if mibBuilder.loadTexts: appRouteSlaClassTable.setDescription('SLA class table')
appRouteSlaClassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 4, 1), ).setIndexNames((0, "CISCO-SDWAN-APP-ROUTE-MIB", "appRouteSlaClassIndex"))
if mibBuilder.loadTexts: appRouteSlaClassEntry.setStatus('current')
if mibBuilder.loadTexts: appRouteSlaClassEntry.setDescription('SLA class table entry')
appRouteSlaClassIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 4, 1, 1), UnsignedByte())
if mibBuilder.loadTexts: appRouteSlaClassIndex.setStatus('current')
if mibBuilder.loadTexts: appRouteSlaClassIndex.setDescription('SLA class index')
appRouteSlaClassName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 4, 1, 2), String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteSlaClassName.setStatus('current')
if mibBuilder.loadTexts: appRouteSlaClassName.setDescription('Name of the SLA class')
appRouteSlaClassLoss = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 4, 1, 3), UnsignedByte()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteSlaClassLoss.setStatus('current')
if mibBuilder.loadTexts: appRouteSlaClassLoss.setDescription('Configured loss, in percentage')
appRouteSlaClassLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 4, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteSlaClassLatency.setStatus('current')
if mibBuilder.loadTexts: appRouteSlaClassLatency.setDescription('Configured latency, in milliseconds')
appRouteSlaClassJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 1001, 1, 4, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appRouteSlaClassJitter.setStatus('current')
if mibBuilder.loadTexts: appRouteSlaClassJitter.setDescription('Configured jitter, in milliseconds')
ciscoSdwanAppRouteMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 1001, 3, 1))
ciscoSdwanAppRouteMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 1001, 3, 2))
ciscoSdwanAppRouteMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 1001, 3, 1, 1)).setObjects(("CISCO-SDWAN-APP-ROUTE-MIB", "cSdwanAppRouteStatisticsGroup"), ("CISCO-SDWAN-APP-ROUTE-MIB", "cSdwanAppRouteStatisticsIntervalGroup"), ("CISCO-SDWAN-APP-ROUTE-MIB", "cSdwanAppRouteSlaClassGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSdwanAppRouteMIBCompliance = ciscoSdwanAppRouteMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoSdwanAppRouteMIBCompliance.setDescription('The compliance statement for the SNMP entities\n         that implement the ciscoSdwanAppRouteMIB module.')
cSdwanAppRouteStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 1001, 3, 2, 1)).setObjects(("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsRemoteSystemIp"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsLocalColor"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsRemoteColor"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsMeanLoss"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsMeanLatency"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsMeanJitter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSdwanAppRouteStatisticsGroup = cSdwanAppRouteStatisticsGroup.setStatus('current')
if mibBuilder.loadTexts: cSdwanAppRouteStatisticsGroup.setDescription('This is a collection of objects of AppRoute statistics.')
cSdwanAppRouteStatisticsIntervalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 1001, 3, 2, 2)).setObjects(("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsIntervalTotalPackets"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsIntervalLoss"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsIntervalAverageLatency"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsIntervalAverageJitter"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsIntervalTxDataPkts"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsIntervalRxDataPkts"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsIntervalIpv6TxDataPkts"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteStatisticsIntervalIpv6RxDataPkts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSdwanAppRouteStatisticsIntervalGroup = cSdwanAppRouteStatisticsIntervalGroup.setStatus('current')
if mibBuilder.loadTexts: cSdwanAppRouteStatisticsIntervalGroup.setDescription('This is a collection of objects of AppRoute\n         statistics interval.')
cSdwanAppRouteSlaClassGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 1001, 3, 2, 3)).setObjects(("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteSlaClassName"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteSlaClassLoss"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteSlaClassLatency"), ("CISCO-SDWAN-APP-ROUTE-MIB", "appRouteSlaClassJitter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cSdwanAppRouteSlaClassGroup = cSdwanAppRouteSlaClassGroup.setStatus('current')
if mibBuilder.loadTexts: cSdwanAppRouteSlaClassGroup.setDescription('This is a collection of objects of AppRoute SLA class.')
mibBuilder.exportSymbols("CISCO-SDWAN-APP-ROUTE-MIB", InetAddressIP=InetAddressIP, appRouteStatisticsLocalColor=appRouteStatisticsLocalColor, appRouteStatisticsMeanLoss=appRouteStatisticsMeanLoss, appRouteStatisticsIntervalLoss=appRouteStatisticsIntervalLoss, appRouteSlaClassName=appRouteSlaClassName, cSdwanAppRouteSlaClassGroup=cSdwanAppRouteSlaClassGroup, appRouteStatisticsIntervalIndex=appRouteStatisticsIntervalIndex, UnsignedShort=UnsignedShort, appRouteStatisticsEntry=appRouteStatisticsEntry, appRouteStatisticsIntervalIpv6RxDataPkts=appRouteStatisticsIntervalIpv6RxDataPkts, ciscoSdwanAppRouteMIBGroups=ciscoSdwanAppRouteMIBGroups, ciscoSdwanAppRouteMIBConform=ciscoSdwanAppRouteMIBConform, ciscoSdwanAppRouteMIBCompliance=ciscoSdwanAppRouteMIBCompliance, PYSNMP_MODULE_ID=ciscoSdwanAppRouteMIB, appRouteStatisticsIntervalTxDataPkts=appRouteStatisticsIntervalTxDataPkts, appRouteStatisticsProto=appRouteStatisticsProto, appRouteStatisticsSrcIp=appRouteStatisticsSrcIp, appRouteStatisticsMeanJitter=appRouteStatisticsMeanJitter, appRouteStatisticsRemoteColor=appRouteStatisticsRemoteColor, ciscoSdwanAppRouteMIB=ciscoSdwanAppRouteMIB, appRouteStatisticsIntervalRxDataPkts=appRouteStatisticsIntervalRxDataPkts, ciscoSdwanAppRouteMIBObjects=ciscoSdwanAppRouteMIBObjects, appRouteStatisticsIntervalTotalPackets=appRouteStatisticsIntervalTotalPackets, appRouteSlaClassLoss=appRouteSlaClassLoss, appRouteStatisticsIntervalEntry=appRouteStatisticsIntervalEntry, appRouteStatisticsTable=appRouteStatisticsTable, appRouteSlaClassEntry=appRouteSlaClassEntry, appRouteStatisticsRemoteSystemIp=appRouteStatisticsRemoteSystemIp, appRouteStatisticsSrcPort=appRouteStatisticsSrcPort, appRouteSlaClassIndex=appRouteSlaClassIndex, appRouteSlaClassLatency=appRouteSlaClassLatency, ciscoSdwanAppRouteMIBCompliances=ciscoSdwanAppRouteMIBCompliances, appRouteStatisticsMeanLatency=appRouteStatisticsMeanLatency, appRouteStatisticsIntervalAverageLatency=appRouteStatisticsIntervalAverageLatency, String=String, appRouteStatisticsDstPort=appRouteStatisticsDstPort, appRouteSlaClassTable=appRouteSlaClassTable, UnsignedByte=UnsignedByte, cSdwanAppRouteStatisticsIntervalGroup=cSdwanAppRouteStatisticsIntervalGroup, cSdwanAppRouteStatisticsGroup=cSdwanAppRouteStatisticsGroup, appRouteStatisticsIntervalAverageJitter=appRouteStatisticsIntervalAverageJitter, appRouteStatisticsIntervalTable=appRouteStatisticsIntervalTable, appRouteSlaClassJitter=appRouteSlaClassJitter, appRouteStatisticsIntervalIpv6TxDataPkts=appRouteStatisticsIntervalIpv6TxDataPkts, appRouteStatisticsDstIp=appRouteStatisticsDstIp)
