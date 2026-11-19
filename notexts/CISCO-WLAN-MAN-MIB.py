#
# PySNMP MIB module CISCO-WLAN-MAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-WLAN-MAN-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:44 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Counter32")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoWlanManMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 415))
ciscoWlanManMIB.setRevisions(('2004-03-22 00:00',))
if mibBuilder.loadTexts: ciscoWlanManMIB.setLastUpdated('200403220000Z')
if mibBuilder.loadTexts: ciscoWlanManMIB.setOrganization('Cisco System Inc.')
ciscoWlanManMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 415, 0))
ciscoWlanManMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 415, 1))
ciscoWlanManMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 415, 2))
cwmDeviceConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 415, 1, 1))
cwmNetworkConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 415, 1, 2))
cwmHttpServerEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 415, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmHttpServerEnabled.setStatus('current')
cwmTelnetLoginEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 415, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cwmTelnetLoginEnabled.setStatus('current')
ciscoWlanManMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 415, 2, 1))
ciscoWlanManMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 415, 2, 2))
ciscoWlanManMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 415, 2, 1, 1)).setObjects(("CISCO-WLAN-MAN-MIB", "cwmWirelessDeviceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWlanManMIBCompliance = ciscoWlanManMIBCompliance.setStatus('current')
cwmWirelessDeviceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 415, 2, 2, 1)).setObjects(("CISCO-WLAN-MAN-MIB", "cwmHttpServerEnabled"), ("CISCO-WLAN-MAN-MIB", "cwmTelnetLoginEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwmWirelessDeviceGroup = cwmWirelessDeviceGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-WLAN-MAN-MIB", cwmNetworkConfig=cwmNetworkConfig, ciscoWlanManMIBGroups=ciscoWlanManMIBGroups, ciscoWlanManMIBConform=ciscoWlanManMIBConform, ciscoWlanManMIBCompliance=ciscoWlanManMIBCompliance, cwmWirelessDeviceGroup=cwmWirelessDeviceGroup, ciscoWlanManMIBNotifs=ciscoWlanManMIBNotifs, cwmTelnetLoginEnabled=cwmTelnetLoginEnabled, cwmDeviceConfig=cwmDeviceConfig, ciscoWlanManMIBObjects=ciscoWlanManMIBObjects, cwmHttpServerEnabled=cwmHttpServerEnabled, PYSNMP_MODULE_ID=ciscoWlanManMIB, ciscoWlanManMIBCompliances=ciscoWlanManMIBCompliances, ciscoWlanManMIB=ciscoWlanManMIB)
