#
# PySNMP MIB module CISCO-DOT11-LBS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DOT11-LBS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:14 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddress, InetAddressType, InetPortNumber = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType", "InetPortNumber")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, TruthValue, MacAddress, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "MacAddress", "RowStatus", "TextualConvention")
ciscoDot11LbsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 454))
ciscoDot11LbsMIB.setRevisions(('2004-11-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoDot11LbsMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoDot11LbsMIB.setLastUpdated('200411170000Z')
if mibBuilder.loadTexts: ciscoDot11LbsMIB.setOrganization('Cisco System Inc.')
if mibBuilder.loadTexts: ciscoDot11LbsMIB.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive,\n                        San Jose CA 95134-1706.\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-dot11@cisco.com')
if mibBuilder.loadTexts: ciscoDot11LbsMIB.setDescription('This MIB module supports network management \n                for Location Based Services on IEEE 802.11 wireless\n                LAN devices.  Location Based Services allows third\n                party applications and positioning servers to work \n                with Access Points to track positions of wireless \n                clients in the network.  \n\n                          GLOSSARY and ACRONYMS\n\n                AP\n                    Access point, a transmitter/receiver device\n                    that commonly connects and transports data\n                    between a wireless network and a wired network.\n\n                LBS \n                    Location Based Services\n\n                MAC\n                    Medium Access Control.  Layer 2 in the network \n                    model. \n\n                PS\n                    Positioning Server.  An application server\n                    provides IEEE 802.11 wireless client location\n                    information and services.\n\n                RSSI \n                    Received Signal Strength Indication.')
ciscoDot11LbsMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 454, 0))
ciscoDot11LbsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 454, 1))
ciscoDot11LbsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 454, 2))
ciscoDot11LbsConfigInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1))
ciscoDot11LbsStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 2))
class Cdot11LbsTrackMethodType(TextualConvention, Bits):
    description = 'These are the supported methods for wireless\n                client location tracking:\n                    rssi(0)    - RSSI detection.'
    status = 'current'
    namedValues = NamedValues(("rssi", 0))

class Cdot11LbsPsPacketType(TextualConvention, Integer32):
    description = 'These are the types of packets sending to the\n                positioning server.  There are two packet types:\n                    extended(1) -  all data field from LBS message\n                                   Tag and header are included,\n                    short(2)    -  only the LBS message header will\n                                   be included in the PS packets.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("extended", 1), ("short", 2))

cdot11LbsProfileTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1), )
if mibBuilder.loadTexts: cdot11LbsProfileTable.setStatus('current')
if mibBuilder.loadTexts: cdot11LbsProfileTable.setDescription('This table contains the set of attributes for \n                configuration of connection to remote LBS positioning\n                servers and tracking methods supported on the servers.\n                A positioning server may support LBS application at \n                multiple UDP ports.  This wireless station serves as\n                a LBS agent to track the wireless client device.  It\n                receives multicast wireless packet sending by the \n                client devices on specific multicast addresses and \n                forward the information to the positioning server.')
cdot11LbsProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-DOT11-LBS-MIB", "cdot11LbsProfileName"))
if mibBuilder.loadTexts: cdot11LbsProfileEntry.setStatus('current')
if mibBuilder.loadTexts: cdot11LbsProfileEntry.setDescription('Each entry contains parameters to configure\n                a LBS positioning server profile for this wireless\n                station.')
cdot11LbsProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 16)))
if mibBuilder.loadTexts: cdot11LbsProfileName.setStatus('current')
if mibBuilder.loadTexts: cdot11LbsProfileName.setDescription('This is the name of LBS profile for configuration of\n                a connection to a LBS positioning server at a specific\n                address and UDP port.')
cdot11LbsServerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 2), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11LbsServerAddressType.setStatus('current')
if mibBuilder.loadTexts: cdot11LbsServerAddressType.setDescription('This is the address type of the \n                cdot11LbsServerAddress.')
cdot11LbsServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11LbsServerAddress.setStatus('current')
if mibBuilder.loadTexts: cdot11LbsServerAddress.setDescription('This is the address of the LBS positioning server.\n                The cdot11LbsServerAddressType specifies the \n                type of this address.')
cdot11LbsServerUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 4), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11LbsServerUdpPort.setStatus('current')
if mibBuilder.loadTexts: cdot11LbsServerUdpPort.setDescription('This is the UDP port of the LBS positioning server\n                used to receive LBS packets from this wireless\n                station.')
cdot11LbsTrackMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 5), Cdot11LbsTrackMethodType().clone(namedValues=NamedValues(("rssi", 0)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11LbsTrackMethod.setStatus('current')
if mibBuilder.loadTexts: cdot11LbsTrackMethod.setDescription('This specifies the method used to detect the\n                location of the wireless client relative to the\n                position of this wireless station.  RSSI method\n                uses the strength of the received signals from\n                the wireless client devices to determine their \n                positions.')
cdot11LbsPsPacketType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 6), Cdot11LbsPsPacketType().clone('extended')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11LbsPsPacketType.setStatus('current')
if mibBuilder.loadTexts: cdot11LbsPsPacketType.setDescription('This specifies the type of LBS packets sent to \n                the LBS position server from this wireless station.')
cdot11LbsTrackMulticast = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 7), MacAddress().clone(hexValue="014096000010")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11LbsTrackMulticast.setStatus('current')
if mibBuilder.loadTexts: cdot11LbsTrackMulticast.setDescription('This is the multicast MAC destination address\n                of the LBS frames sending from the wireless \n                clients to this wireless station.')
cdot11LbsMatchChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 8), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11LbsMatchChannel.setStatus('current')
if mibBuilder.loadTexts: cdot11LbsMatchChannel.setDescription("This object determines if this wireless station will\n                include LBS frames received in channels other than\n                the sender's channel in the RSSI measurement.  If the\n                value is 'true', this station will include only LBS \n                frames matching the sender's channel in the RSSI\n                measurement.  If the value is 'false', all received\n                LBS frames will be included in the measurement.")
cdot11LbsProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 1, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11LbsProfileRowStatus.setStatus('current')
if mibBuilder.loadTexts: cdot11LbsProfileRowStatus.setDescription("This configures a new LBS positioning server for this\n                wireless station and modifies or deletes an existing \n                positioning server configuration.\n\n                Creation of rows must be done via 'createAndGo' and\n                with the cdot11LbsServerAddress and\n                cdot11LbsServerUdpPort set to the address and UDP\n                of the LBS positioning server.\n\n                This object will become 'notInService' if the NMS \n                successfully performs a multivarbind set for all \n                required objects including this object while this\n                profile is not attached to any wireless interface\n                or a connection cannot be established to the LBS\n                positioning server.\n\n                This object will become 'active' when this profile\n                is attached to at least one wireless interface via \n                cdot11LbsProfInterfaceTable and a connection to the\n                LBS positioning server is successfully established. \n\n                Modification and deletion (via 'destroy') of rows can\n                be done when this object is 'active', or \n                'notInService'.  Deletion of a row will remove the\n                corresponding entries for the same profile from the\n                cdot11LbsProfInterfaceTable.")
cdot11LbsProfInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 2), )
if mibBuilder.loadTexts: cdot11LbsProfInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: cdot11LbsProfInterfaceTable.setDescription('This table configures the Location Based Services\n                settings on the IEEE 802.11 radio interfaces of \n                this device.                  \n\n                This table has an expansion dependent relationship\n                on the cdot11LbsProfileTable.  This table uses the\n                ifIndex of interfaces of ifType ieee80211(71) as \n                the expansion index.')
cdot11LbsProfInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-DOT11-LBS-MIB", "cdot11LbsProfileName"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cdot11LbsProfInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: cdot11LbsProfInterfaceEntry.setDescription('Each entry indicates if the LBS client location \n                tracking by a particular location positioning server\n                profile is enabled on an IEEE 802.11 interface.')
cdot11LbsProfInterfaceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 454, 1, 1, 2, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cdot11LbsProfInterfaceRowStatus.setStatus('current')
if mibBuilder.loadTexts: cdot11LbsProfInterfaceRowStatus.setDescription("This configures and attaches a LBS profile to an \n                IEEE 802.11 wireless LAN network interface or remove\n                a configured interface from the profile.\n\n                Creation of rows must be done via 'createAndGo' and\n                specifying the cdot11LbsProfileName of an existing\n                profile and the ifIndex of an IEEE 802.11 interface. \n\n                This object will become 'active' when the profile is\n                attached to a network interface and a connection to the\n                LBS positioning server is successfully established. \n                Otherwise, if this object will become 'notInService'.\n\n                Modification and deletion (via 'destroy') of rows can\n                be done when this object is 'active' or 'notInService'.\n\n                If all interfaces are removed from an 'active' profile,\n                the profile cdot11LbsProfileRowStatus will become\n                'notInService'.")
ciscoDot11LbsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 454, 2, 1))
ciscoDot11LbsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 454, 2, 2))
ciscoDot11LbsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 454, 2, 1, 1)).setObjects(("CISCO-DOT11-LBS-MIB", "ciscoDot11LbsConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11LbsMIBCompliance = ciscoDot11LbsMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoDot11LbsMIBCompliance.setDescription('The compliance statement for the \n                ciscoDot11LbsMIB module.')
ciscoDot11LbsConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 454, 2, 2, 1)).setObjects(("CISCO-DOT11-LBS-MIB", "cdot11LbsServerAddressType"), ("CISCO-DOT11-LBS-MIB", "cdot11LbsServerAddress"), ("CISCO-DOT11-LBS-MIB", "cdot11LbsServerUdpPort"), ("CISCO-DOT11-LBS-MIB", "cdot11LbsTrackMethod"), ("CISCO-DOT11-LBS-MIB", "cdot11LbsPsPacketType"), ("CISCO-DOT11-LBS-MIB", "cdot11LbsTrackMulticast"), ("CISCO-DOT11-LBS-MIB", "cdot11LbsMatchChannel"), ("CISCO-DOT11-LBS-MIB", "cdot11LbsProfileRowStatus"), ("CISCO-DOT11-LBS-MIB", "cdot11LbsProfInterfaceRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDot11LbsConfigGroup = ciscoDot11LbsConfigGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoDot11LbsConfigGroup.setDescription('Configurations for IEEE 802.11 Location Based\n                Services.')
mibBuilder.exportSymbols("CISCO-DOT11-LBS-MIB", cdot11LbsProfInterfaceEntry=cdot11LbsProfInterfaceEntry, ciscoDot11LbsMIBConformance=ciscoDot11LbsMIBConformance, cdot11LbsPsPacketType=cdot11LbsPsPacketType, Cdot11LbsPsPacketType=Cdot11LbsPsPacketType, cdot11LbsProfInterfaceTable=cdot11LbsProfInterfaceTable, Cdot11LbsTrackMethodType=Cdot11LbsTrackMethodType, PYSNMP_MODULE_ID=ciscoDot11LbsMIB, cdot11LbsProfInterfaceRowStatus=cdot11LbsProfInterfaceRowStatus, ciscoDot11LbsMIBCompliance=ciscoDot11LbsMIBCompliance, cdot11LbsProfileRowStatus=cdot11LbsProfileRowStatus, cdot11LbsServerAddressType=cdot11LbsServerAddressType, cdot11LbsServerAddress=cdot11LbsServerAddress, cdot11LbsProfileEntry=cdot11LbsProfileEntry, ciscoDot11LbsConfigGroup=ciscoDot11LbsConfigGroup, ciscoDot11LbsStatistics=ciscoDot11LbsStatistics, ciscoDot11LbsConfigInfo=ciscoDot11LbsConfigInfo, cdot11LbsProfileTable=cdot11LbsProfileTable, cdot11LbsTrackMethod=cdot11LbsTrackMethod, ciscoDot11LbsMIB=ciscoDot11LbsMIB, ciscoDot11LbsMIBCompliances=ciscoDot11LbsMIBCompliances, cdot11LbsMatchChannel=cdot11LbsMatchChannel, cdot11LbsServerUdpPort=cdot11LbsServerUdpPort, cdot11LbsTrackMulticast=cdot11LbsTrackMulticast, ciscoDot11LbsMIBObjects=ciscoDot11LbsMIBObjects, cdot11LbsProfileName=cdot11LbsProfileName, ciscoDot11LbsMIBNotifs=ciscoDot11LbsMIBNotifs, ciscoDot11LbsMIBGroups=ciscoDot11LbsMIBGroups)
