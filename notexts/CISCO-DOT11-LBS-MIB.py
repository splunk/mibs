#
# PySNMP MIB module CISCO-DOT11-LBS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DOT11-LBS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetPortNumber, InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber", "InetAddress", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
TruthValue, TextualConvention, DisplayString, MacAddress, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString", "MacAddress", "RowStatus")
ciscoDot11LbsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 454))
ciscoDot11LbsMIB.setRevisions(('2004-11-17 00:00',))
if mibBuilder.loadTexts: ciscoDot11LbsMIB.setLastUpdated('200411170000Z')
if mibBuilder.loadTexts: ciscoDot11LbsMIB.setOrganization('Cisco System Inc.')
ciscoDot11LbsMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 454, 0))
ciscoDot11LbsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 454, 1))
ciscoDot11LbsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 454, 2))
ciscoDot11LbsConfigInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1))
ciscoDot11LbsStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 2))
class Cdot11LbsTrackMethodType(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("rssi", 0))

class Cdot11LbsPsPacketType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("extended", 1), ("short", 2))

cdot11LbsProfileTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1), )
if mibBuilder.loadTexts: cdot11LbsProfileTable.setStatus('current')
cdot11LbsProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-DOT11-LBS-MIB", "cdot11LbsProfileName"))
if mibBuilder.loadTexts: cdot11LbsProfileEntry.setStatus('current')
cdot11LbsProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 16)))
if mibBuilder.loadTexts: cdot11LbsProfileName.setStatus('current')
cdot11LbsServerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 2), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11LbsServerAddressType.setStatus('current')
cdot11LbsServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11LbsServerAddress.setStatus('current')
cdot11LbsServerUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 4), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11LbsServerUdpPort.setStatus('current')
cdot11LbsTrackMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 5), Cdot11LbsTrackMethodType().clone(namedValues=NamedValues(("rssi", 0)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11LbsTrackMethod.setStatus('current')
cdot11LbsPsPacketType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 6), Cdot11LbsPsPacketType().clone('extended')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11LbsPsPacketType.setStatus('current')
cdot11LbsTrackMulticast = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 7), MacAddress().clone(hexValue="014096000010")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11LbsTrackMulticast.setStatus('current')
cdot11LbsMatchChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 8), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11LbsMatchChannel.setStatus('current')
cdot11LbsProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11LbsProfileRowStatus.setStatus('current')
cdot11LbsProfInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 2), )
if mibBuilder.loadTexts: cdot11LbsProfInterfaceTable.setStatus('current')
cdot11LbsProfInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-DOT11-LBS-MIB", "cdot11LbsProfileName"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cdot11LbsProfInterfaceEntry.setStatus('current')
cdot11LbsProfInterfaceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 2, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11LbsProfInterfaceRowStatus.setStatus('current')
ciscoDot11LbsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 454, 2, 1))
ciscoDot11LbsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 454, 2, 2))
ciscoDot11LbsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 454, 2, 1, 1)).setObjects(("CISCO-DOT11-LBS-MIB", "ciscoDot11LbsConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11LbsMIBCompliance = ciscoDot11LbsMIBCompliance.setStatus('current')
ciscoDot11LbsConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 454, 2, 2, 1)).setObjects(("CISCO-DOT11-LBS-MIB", "cdot11LbsServerAddressType"), ("CISCO-DOT11-LBS-MIB", "cdot11LbsServerAddress"), ("CISCO-DOT11-LBS-MIB", "cdot11LbsServerUdpPort"), ("CISCO-DOT11-LBS-MIB", "cdot11LbsTrackMethod"), ("CISCO-DOT11-LBS-MIB", "cdot11LbsPsPacketType"), ("CISCO-DOT11-LBS-MIB", "cdot11LbsTrackMulticast"), ("CISCO-DOT11-LBS-MIB", "cdot11LbsMatchChannel"), ("CISCO-DOT11-LBS-MIB", "cdot11LbsProfileRowStatus"), ("CISCO-DOT11-LBS-MIB", "cdot11LbsProfInterfaceRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11LbsConfigGroup = ciscoDot11LbsConfigGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DOT11-LBS-MIB", ciscoDot11LbsMIBCompliances=ciscoDot11LbsMIBCompliances, cdot11LbsTrackMulticast=cdot11LbsTrackMulticast, cdot11LbsProfInterfaceRowStatus=cdot11LbsProfInterfaceRowStatus, cdot11LbsProfileTable=cdot11LbsProfileTable, Cdot11LbsPsPacketType=Cdot11LbsPsPacketType, PYSNMP_MODULE_ID=ciscoDot11LbsMIB, cdot11LbsProfInterfaceEntry=cdot11LbsProfInterfaceEntry, cdot11LbsTrackMethod=cdot11LbsTrackMethod, cdot11LbsServerAddress=cdot11LbsServerAddress, cdot11LbsServerAddressType=cdot11LbsServerAddressType, ciscoDot11LbsStatistics=ciscoDot11LbsStatistics, cdot11LbsProfileName=cdot11LbsProfileName, cdot11LbsProfInterfaceTable=cdot11LbsProfInterfaceTable, ciscoDot11LbsConfigGroup=ciscoDot11LbsConfigGroup, ciscoDot11LbsMIBGroups=ciscoDot11LbsMIBGroups, cdot11LbsProfileRowStatus=cdot11LbsProfileRowStatus, cdot11LbsServerUdpPort=cdot11LbsServerUdpPort, cdot11LbsProfileEntry=cdot11LbsProfileEntry, ciscoDot11LbsMIBObjects=ciscoDot11LbsMIBObjects, Cdot11LbsTrackMethodType=Cdot11LbsTrackMethodType, ciscoDot11LbsMIBConformance=ciscoDot11LbsMIBConformance, ciscoDot11LbsMIB=ciscoDot11LbsMIB, ciscoDot11LbsMIBCompliance=ciscoDot11LbsMIBCompliance, ciscoDot11LbsConfigInfo=ciscoDot11LbsConfigInfo, cdot11LbsMatchChannel=cdot11LbsMatchChannel, ciscoDot11LbsMIBNotifs=ciscoDot11LbsMIBNotifs, cdot11LbsPsPacketType=cdot11LbsPsPacketType)
