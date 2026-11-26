#
# PySNMP MIB module CISCO-WLAN-MAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-WLAN-MAN-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
ciscoWlanManMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 415))
ciscoWlanManMIB.setRevisions(('2004-03-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWlanManMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoWlanManMIB.setLastUpdated('200403220000Z')
if mibBuilder.loadTexts: ciscoWlanManMIB.setOrganization('Cisco System Inc.')
if mibBuilder.loadTexts: ciscoWlanManMIB.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive,\n                        San Jose CA 95134-1706.\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                 Email: cs-dot11@cisco.com')
if mibBuilder.loadTexts: ciscoWlanManMIB.setDescription('This MIB module provides network management\n                and configuration support for IEEE 802.11\n                Wireless LAN devices.\n\n                          ACRONYMS\n\n                HTTP\n                    Hypertext Transfer Protocol.')
ciscoWlanManMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 415, 0))
ciscoWlanManMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 415, 1))
ciscoWlanManMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 415, 2))
cwmDeviceConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 415, 1, 1))
cwmNetworkConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 415, 1, 2))
cwmHttpServerEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 415, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmHttpServerEnabled.setStatus('current')
if mibBuilder.loadTexts: cwmHttpServerEnabled.setDescription("This object enables the HTTP Web server as follows:\n                    'true'  - HTTP Web server function is enabled,\n                    'false' - HTTP Web server function is disabled.")
cwmTelnetLoginEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 415, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmTelnetLoginEnabled.setStatus('current')
if mibBuilder.loadTexts: cwmTelnetLoginEnabled.setDescription("This object enables the telnet console login as \n                follows:                         \n                    'true'  - telnet console login is enabled,\n                    'false' - telnet console login is disabled.")
ciscoWlanManMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 415, 2, 1))
ciscoWlanManMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 415, 2, 2))
ciscoWlanManMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 415, 2, 1, 1)).setObjects(("CISCO-WLAN-MAN-MIB", "cwmWirelessDeviceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWlanManMIBCompliance = ciscoWlanManMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoWlanManMIBCompliance.setDescription('The compliance statement for the\n                ciscoWlanManMIB module.')
cwmWirelessDeviceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 415, 2, 2, 1)).setObjects(("CISCO-WLAN-MAN-MIB", "cwmHttpServerEnabled"), ("CISCO-WLAN-MAN-MIB", "cwmTelnetLoginEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwmWirelessDeviceGroup = cwmWirelessDeviceGroup.setStatus('current')
if mibBuilder.loadTexts: cwmWirelessDeviceGroup.setDescription('Configuration for Wireless LAN Access Points\n                and bridges.')
mibBuilder.exportSymbols("CISCO-WLAN-MAN-MIB", ciscoWlanManMIBNotifs=ciscoWlanManMIBNotifs, cwmNetworkConfig=cwmNetworkConfig, ciscoWlanManMIBCompliances=ciscoWlanManMIBCompliances, ciscoWlanManMIBConform=ciscoWlanManMIBConform, cwmWirelessDeviceGroup=cwmWirelessDeviceGroup, PYSNMP_MODULE_ID=ciscoWlanManMIB, cwmHttpServerEnabled=cwmHttpServerEnabled, cwmDeviceConfig=cwmDeviceConfig, ciscoWlanManMIBGroups=ciscoWlanManMIBGroups, ciscoWlanManMIBCompliance=ciscoWlanManMIBCompliance, ciscoWlanManMIB=ciscoWlanManMIB, ciscoWlanManMIBObjects=ciscoWlanManMIBObjects, cwmTelnetLoginEnabled=cwmTelnetLoginEnabled)
