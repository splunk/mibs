#
# PySNMP MIB module CISCOSB-UDLD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCOSB-UDLD-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:07 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
rndNotifications, switch001 = mibBuilder.importSymbols("CISCOSB-MIB", "rndNotifications", "switch001")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
RowStatus, MacAddress, TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "MacAddress", "TextualConvention", "DisplayString", "TruthValue")
class UdldString(SnmpAdminString):
    description = 'The Device-ID TLV should contain the switch base MAC address in ACSII format.'
    status = 'current'

class UdldPortBidirectionalState(TextualConvention, Integer32):
    description = 'Port UDLD current status (shutdown, idle, detection, undetermined, bidirectional).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("shutdown", 1), ("idle", 2), ("detection", 3), ("undetermined", 4), ("bidirectional", 5))

class UdldNeighborCurrentState(TextualConvention, Integer32):
    description = 'Port UDLD Neighbor current status (Disabled, Enabled, Undefined, Bidirectional).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("disabled", 1), ("enabled", 2), ("undefined", 3), ("bidirectional", 4))

class UdldGlobalMode(TextualConvention, Integer32):
    description = 'Global (fiber) Port UDLD curent status (normal, aggressive, disabled).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("normal", 1), ("aggressive", 2), ("disabled", 3))

class UdldPortMode(TextualConvention, Integer32):
    description = 'Port UDLD curent status (normal, aggressive, disabled, default).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("normal", 1), ("aggressive", 2), ("disabled", 3), ("default", 4))

rlUdld = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218))
rlUdld.setRevisions(('2012-08-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlUdld.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlUdld.setLastUpdated('201208010000Z')
if mibBuilder.loadTexts: rlUdld.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: rlUdld.setContactInfo('Postal: 170 West Tasman Drive\n         San Jose , CA 95134-1706\n         USA\n\n         \n         Website:  Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: rlUdld.setDescription('This private MIB module for UDLD (Cisco Systems UniDirectional Link Detection Protocol).')
rlUdldPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 1), )
if mibBuilder.loadTexts: rlUdldPortTable.setStatus('current')
if mibBuilder.loadTexts: rlUdldPortTable.setDescription('The table holds information for Udld Ethernet ports.')
rlUdldPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 1, 1), ).setIndexNames((0, "CISCOSB-UDLD-MIB", "rlUdldPortIfIndex"))
if mibBuilder.loadTexts: rlUdldPortEntry.setStatus('current')
if mibBuilder.loadTexts: rlUdldPortEntry.setDescription('Entry in the rlUdldPortTable.')
rlUdldPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rlUdldPortIfIndex.setStatus('current')
if mibBuilder.loadTexts: rlUdldPortIfIndex.setDescription('Interface Index. This variable is the key for udld port table.\n         uniquely identifies the udld port information.')
rlUdldPortAdminMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 1, 1, 2), UdldPortMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlUdldPortAdminMode.setStatus('current')
if mibBuilder.loadTexts: rlUdldPortAdminMode.setDescription('This variable identifies port UDLD admin configured mode (normal, aggressive, disable).')
rlUdldPortOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 1, 1, 3), UdldPortMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldPortOperMode.setStatus('current')
if mibBuilder.loadTexts: rlUdldPortOperMode.setDescription('This variable identifies port UDLD operational mode (normal, aggressive, disable).\n        for fiber ports it is combination of global mode and port mode')
rlUdldPortDefaultConfiguration = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldPortDefaultConfiguration.setStatus('current')
if mibBuilder.loadTexts: rlUdldPortDefaultConfiguration.setDescription('This variable indicates whether tne user configure the udld port. to present (default) or not in port configuration.')
rlUdldBidirectionalState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 1, 1, 5), UdldPortBidirectionalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldBidirectionalState.setStatus('current')
if mibBuilder.loadTexts: rlUdldBidirectionalState.setDescription('This variable identifies the port UDLD status (shutdown, idle, detection, undetermined, bidirectional).')
rlUdldNumberOfDetectedNeighbors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldNumberOfDetectedNeighbors.setStatus('current')
if mibBuilder.loadTexts: rlUdldNumberOfDetectedNeighbors.setDescription('Number Of Detected Neighbors for this port.')
rlUdldNeighborTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2), )
if mibBuilder.loadTexts: rlUdldNeighborTable.setStatus('current')
if mibBuilder.loadTexts: rlUdldNeighborTable.setDescription('The table holds information for Udld Neighbor of ethernet ports.')
rlUdldNeighborEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2, 1), ).setIndexNames((0, "CISCOSB-UDLD-MIB", "rlUdldNeighborPortIfIndex"), (0, "CISCOSB-UDLD-MIB", "rlUdldNeighborDeviceID"), (0, "CISCOSB-UDLD-MIB", "rlUdldNeighborPortID"))
if mibBuilder.loadTexts: rlUdldNeighborEntry.setStatus('current')
if mibBuilder.loadTexts: rlUdldNeighborEntry.setDescription('Entry in the rlUdldNeighborTable.')
rlUdldNeighborPortIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rlUdldNeighborPortIfIndex.setStatus('current')
if mibBuilder.loadTexts: rlUdldNeighborPortIfIndex.setDescription('Interface Index. This variable is the key for udld port Neighbor table.\n         uniquely identifies the udld port index.')
rlUdldNeighborDeviceID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2, 1, 2), UdldString())
if mibBuilder.loadTexts: rlUdldNeighborDeviceID.setStatus('current')
if mibBuilder.loadTexts: rlUdldNeighborDeviceID.setDescription('The Neighbor Device-ID TLV should contain the switch base MAC address in ACSII format.')
rlUdldNeighborPortID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2, 1, 3), UdldString())
if mibBuilder.loadTexts: rlUdldNeighborPortID.setStatus('current')
if mibBuilder.loadTexts: rlUdldNeighborPortID.setDescription('The Port-ID TLV should contain the port ACSII name as it is printed in show CLI commands.')
rlUdldNeighborDeviceMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2, 1, 4), MacAddress())
if mibBuilder.loadTexts: rlUdldNeighborDeviceMACAddress.setStatus('current')
if mibBuilder.loadTexts: rlUdldNeighborDeviceMACAddress.setDescription('The Neighbor mac address')
rlUdldNeighborDeviceName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2, 1, 5), UdldString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldNeighborDeviceName.setStatus('current')
if mibBuilder.loadTexts: rlUdldNeighborDeviceName.setDescription('The Neighbor NeighborDevice Name TLV should contain sysName in ACSII.')
rlUdldNeighborMessageTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldNeighborMessageTime.setStatus('current')
if mibBuilder.loadTexts: rlUdldNeighborMessageTime.setDescription('The Neighbor Message Time is from Message Interval TLV.\n        This time interval value used by a neighbor to send UDLD probes\n        after the linkup or detection phases. Its time unit is 1 second.')
rlUdldNeighborLeftLifeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldNeighborLeftLifeTime.setStatus('current')
if mibBuilder.loadTexts: rlUdldNeighborLeftLifeTime.setDescription('The remaining holdtime for Neighbor entry in cache in seconds.')
rlUdldNeighborCurrentState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 2, 1, 8), UdldNeighborCurrentState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlUdldNeighborCurrentState.setStatus('current')
if mibBuilder.loadTexts: rlUdldNeighborCurrentState.setDescription('This variable identifies the Neighbor port UDLD current status (Disabled, Enabled, Undefined, Bidirectional).')
rlUdldGlobalUDLDMode = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 3), UdldGlobalMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlUdldGlobalUDLDMode.setStatus('current')
if mibBuilder.loadTexts: rlUdldGlobalUDLDMode.setDescription('Define Global UDLD Mode (normal, aggressive, disable)')
rlUdldGlobalMessageTime = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 218, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlUdldGlobalMessageTime.setStatus('current')
if mibBuilder.loadTexts: rlUdldGlobalMessageTime.setDescription('Define global value of the interval between two sent probe messages, use the udld\n        message time command in Global Configuration mode.')
mibBuilder.exportSymbols("CISCOSB-UDLD-MIB", rlUdldGlobalMessageTime=rlUdldGlobalMessageTime, rlUdldNeighborLeftLifeTime=rlUdldNeighborLeftLifeTime, rlUdldNeighborMessageTime=rlUdldNeighborMessageTime, rlUdldPortIfIndex=rlUdldPortIfIndex, rlUdldPortDefaultConfiguration=rlUdldPortDefaultConfiguration, rlUdldPortEntry=rlUdldPortEntry, rlUdldNeighborTable=rlUdldNeighborTable, rlUdldNeighborDeviceID=rlUdldNeighborDeviceID, UdldNeighborCurrentState=UdldNeighborCurrentState, rlUdldPortAdminMode=rlUdldPortAdminMode, rlUdldNeighborCurrentState=rlUdldNeighborCurrentState, rlUdldNumberOfDetectedNeighbors=rlUdldNumberOfDetectedNeighbors, rlUdldNeighborDeviceName=rlUdldNeighborDeviceName, rlUdldNeighborEntry=rlUdldNeighborEntry, rlUdldGlobalUDLDMode=rlUdldGlobalUDLDMode, rlUdldPortTable=rlUdldPortTable, UdldString=UdldString, PYSNMP_MODULE_ID=rlUdld, rlUdld=rlUdld, rlUdldNeighborPortID=rlUdldNeighborPortID, UdldGlobalMode=UdldGlobalMode, rlUdldNeighborDeviceMACAddress=rlUdldNeighborDeviceMACAddress, rlUdldBidirectionalState=rlUdldBidirectionalState, UdldPortBidirectionalState=UdldPortBidirectionalState, rlUdldNeighborPortIfIndex=rlUdldNeighborPortIfIndex, rlUdldPortOperMode=rlUdldPortOperMode, UdldPortMode=UdldPortMode)
