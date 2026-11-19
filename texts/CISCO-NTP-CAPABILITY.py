#
# PySNMP MIB module CISCO-NTP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-NTP-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:14 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoNtpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 99999))
ciscoNtpCapability.setRevisions(('2006-04-05 00:00', '2005-06-22 00:00', '2003-04-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoNtpCapability.setRevisionsDescriptions(('Added ciscoNtpCapabilityIOS124', 'Capability for MDS platform.', 'Initial version of the MIB Module.',))
if mibBuilder.loadTexts: ciscoNtpCapability.setLastUpdated('200604050000Z')
if mibBuilder.loadTexts: ciscoNtpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoNtpCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoNtpCapability.setDescription('The Agent Capabilities for CISCO-NTP-MIB.')
ciscoNtpCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 99999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpCapabilityV3R00 = ciscoNtpCapabilityV3R00.setProductRelease('MGX8850 Release 3.00,BPX SES Release ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpCapabilityV3R00 = ciscoNtpCapabilityV3R00.setStatus('current')
if mibBuilder.loadTexts: ciscoNtpCapabilityV3R00.setDescription('NTP MIB Capabilities.')
ciscoNtpCapabilitySANOSV3R0001 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 99999, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpCapabilitySANOSV3R0001 = ciscoNtpCapabilitySANOSV3R0001.setProductRelease('SAN-OS 3.0(1) ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpCapabilitySANOSV3R0001 = ciscoNtpCapabilitySANOSV3R0001.setStatus('current')
if mibBuilder.loadTexts: ciscoNtpCapabilitySANOSV3R0001.setDescription('NTP MIB Capabilities for \n                          SAN-OS 3.0(1).')
ciscoNtpCapabilityIOS124 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 99999, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpCapabilityIOS124 = ciscoNtpCapabilityIOS124.setProductRelease('IOS 12.4')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNtpCapabilityIOS124 = ciscoNtpCapabilityIOS124.setStatus('current')
if mibBuilder.loadTexts: ciscoNtpCapabilityIOS124.setDescription('NTP MIB Capabilities for\n\t\t\t  IOS 12.4 release')
mibBuilder.exportSymbols("CISCO-NTP-CAPABILITY", ciscoNtpCapabilitySANOSV3R0001=ciscoNtpCapabilitySANOSV3R0001, ciscoNtpCapabilityIOS124=ciscoNtpCapabilityIOS124, ciscoNtpCapability=ciscoNtpCapability, ciscoNtpCapabilityV3R00=ciscoNtpCapabilityV3R00, PYSNMP_MODULE_ID=ciscoNtpCapability)
