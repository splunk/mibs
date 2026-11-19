#
# PySNMP MIB module CISCO-NTP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-NTP-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:24 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoNtpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 99999))
ciscoNtpCapability.setRevisions(('2006-04-05 00:00', '2005-06-22 00:00', '2003-04-08 00:00',))
if mibBuilder.loadTexts: ciscoNtpCapability.setLastUpdated('200604050000Z')
if mibBuilder.loadTexts: ciscoNtpCapability.setOrganization('Cisco Systems, Inc.')
ciscoNtpCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 99999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpCapabilityV3R00 = ciscoNtpCapabilityV3R00.setProductRelease('MGX8850 Release 3.00,BPX SES Release ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpCapabilityV3R00 = ciscoNtpCapabilityV3R00.setStatus('current')
ciscoNtpCapabilitySANOSV3R0001 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 99999, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpCapabilitySANOSV3R0001 = ciscoNtpCapabilitySANOSV3R0001.setProductRelease('SAN-OS 3.0(1) ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpCapabilitySANOSV3R0001 = ciscoNtpCapabilitySANOSV3R0001.setStatus('current')
ciscoNtpCapabilityIOS124 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 99999, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpCapabilityIOS124 = ciscoNtpCapabilityIOS124.setProductRelease('IOS 12.4')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpCapabilityIOS124 = ciscoNtpCapabilityIOS124.setStatus('current')
mibBuilder.exportSymbols("CISCO-NTP-CAPABILITY", ciscoNtpCapabilityIOS124=ciscoNtpCapabilityIOS124, PYSNMP_MODULE_ID=ciscoNtpCapability, ciscoNtpCapability=ciscoNtpCapability, ciscoNtpCapabilityV3R00=ciscoNtpCapabilityV3R00, ciscoNtpCapabilitySANOSV3R0001=ciscoNtpCapabilitySANOSV3R0001)
