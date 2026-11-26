#
# PySNMP MIB module CISCOSB-UDLD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCOSB-UDLD-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
rndNotifications, switch001 = mibBuilder.importSymbols("CISCOSB-MIB", "rndNotifications", "switch001")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
TruthValue, TextualConvention, DisplayString, MacAddress, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString", "MacAddress", "RowStatus")
class UdldString(SnmpAdminString):
    status = 'current'

class UdldPortBidirectionalState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("shutdown", 1), ("idle", 2), ("detection", 3), ("undetermined", 4), ("bidirectional", 5))

class UdldNeighborCurrentState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("disabled", 1), ("enabled", 2), ("undefined", 3), ("bidirectional", 4))

class UdldGlobalMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("normal", 1), ("aggressive", 2), ("disabled", 3))

class UdldPortMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("normal", 1), ("aggressive", 2), ("disabled", 3), ("default", 4))

rlUdld = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218))
rlUdld.setRevisions(('2012-08-01 00:00',))
if mibBuilder.loadTexts: rlUdld.setLastUpdated('201208010000Z')
if mibBuilder.loadTexts: rlUdld.setOrganization('Cisco Systems, Inc.')
rlUdldPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 1), )
if mibBuilder.loadTexts: rlUdldPortTable.setStatus('current')
rlUdldPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 1, 1), ).setIndexNames((0, "CISCOSB-UDLD-MIB", "rlUdldPortIfIndex"))
if mibBuilder.loadTexts: rlUdldPortEntry.setStatus('current')
rlUdldPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rlUdldPortIfIndex.setStatus('current')
rlUdldPortAdminMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 1, 1, 2), UdldPortMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlUdldPortAdminMode.setStatus('current')
rlUdldPortOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 1, 1, 3), UdldPortMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldPortOperMode.setStatus('current')
rlUdldPortDefaultConfiguration = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldPortDefaultConfiguration.setStatus('current')
rlUdldBidirectionalState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 1, 1, 5), UdldPortBidirectionalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldBidirectionalState.setStatus('current')
rlUdldNumberOfDetectedNeighbors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldNumberOfDetectedNeighbors.setStatus('current')
rlUdldNeighborTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2), )
if mibBuilder.loadTexts: rlUdldNeighborTable.setStatus('current')
rlUdldNeighborEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2, 1), ).setIndexNames((0, "CISCOSB-UDLD-MIB", "rlUdldNeighborPortIfIndex"), (0, "CISCOSB-UDLD-MIB", "rlUdldNeighborDeviceID"), (0, "CISCOSB-UDLD-MIB", "rlUdldNeighborPortID"))
if mibBuilder.loadTexts: rlUdldNeighborEntry.setStatus('current')
rlUdldNeighborPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rlUdldNeighborPortIfIndex.setStatus('current')
rlUdldNeighborDeviceID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2, 1, 2), UdldString())
if mibBuilder.loadTexts: rlUdldNeighborDeviceID.setStatus('current')
rlUdldNeighborPortID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2, 1, 3), UdldString())
if mibBuilder.loadTexts: rlUdldNeighborPortID.setStatus('current')
rlUdldNeighborDeviceMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2, 1, 4), MacAddress())
if mibBuilder.loadTexts: rlUdldNeighborDeviceMACAddress.setStatus('current')
rlUdldNeighborDeviceName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2, 1, 5), UdldString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldNeighborDeviceName.setStatus('current')
rlUdldNeighborMessageTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldNeighborMessageTime.setStatus('current')
rlUdldNeighborLeftLifeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldNeighborLeftLifeTime.setStatus('current')
rlUdldNeighborCurrentState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2, 1, 8), UdldNeighborCurrentState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldNeighborCurrentState.setStatus('current')
rlUdldGlobalUDLDMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 3), UdldGlobalMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlUdldGlobalUDLDMode.setStatus('current')
rlUdldGlobalMessageTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlUdldGlobalMessageTime.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-UDLD-MIB", rlUdldPortOperMode=rlUdldPortOperMode, UdldPortBidirectionalState=UdldPortBidirectionalState, rlUdldGlobalMessageTime=rlUdldGlobalMessageTime, rlUdld=rlUdld, rlUdldNeighborTable=rlUdldNeighborTable, rlUdldPortDefaultConfiguration=rlUdldPortDefaultConfiguration, UdldString=UdldString, rlUdldNeighborEntry=rlUdldNeighborEntry, rlUdldPortAdminMode=rlUdldPortAdminMode, rlUdldBidirectionalState=rlUdldBidirectionalState, rlUdldPortTable=rlUdldPortTable, rlUdldPortIfIndex=rlUdldPortIfIndex, PYSNMP_MODULE_ID=rlUdld, rlUdldNumberOfDetectedNeighbors=rlUdldNumberOfDetectedNeighbors, rlUdldNeighborDeviceID=rlUdldNeighborDeviceID, rlUdldNeighborPortID=rlUdldNeighborPortID, rlUdldNeighborMessageTime=rlUdldNeighborMessageTime, rlUdldNeighborCurrentState=rlUdldNeighborCurrentState, rlUdldNeighborPortIfIndex=rlUdldNeighborPortIfIndex, UdldPortMode=UdldPortMode, UdldGlobalMode=UdldGlobalMode, rlUdldPortEntry=rlUdldPortEntry, rlUdldNeighborDeviceName=rlUdldNeighborDeviceName, rlUdldGlobalUDLDMode=rlUdldGlobalUDLDMode, rlUdldNeighborDeviceMACAddress=rlUdldNeighborDeviceMACAddress, UdldNeighborCurrentState=UdldNeighborCurrentState, rlUdldNeighborLeftLifeTime=rlUdldNeighborLeftLifeTime)
