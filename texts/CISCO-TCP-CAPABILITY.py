#
# PySNMP MIB module CISCO-TCP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-TCP-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:05 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoTcpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 26))
ciscoTcpCapability.setRevisions(('2006-01-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoTcpCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoTcpCapability.setLastUpdated('200601180000Z')
if mibBuilder.loadTexts: ciscoTcpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoTcpCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-snmp@cisco.com\n                        cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoTcpCapability.setDescription('Agent capabilities for\n                 CISCO-TCP-MIB')
cTcpCapabilityIOSXRV2R0CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 26, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cTcpCapabilityIOSXRV2R0CRS1 = cTcpCapabilityIOSXRV2R0CRS1.setProductRelease('Cisco IOS XR 2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cTcpCapabilityIOSXRV2R0CRS1 = cTcpCapabilityIOSXRV2R0CRS1.setStatus('current')
if mibBuilder.loadTexts: cTcpCapabilityIOSXRV2R0CRS1.setDescription('CISCO-TCP-MIB capabilities\n                         for IOS XR release 2.0')
mibBuilder.exportSymbols("CISCO-TCP-CAPABILITY", PYSNMP_MODULE_ID=ciscoTcpCapability, cTcpCapabilityIOSXRV2R0CRS1=cTcpCapabilityIOSXRV2R0CRS1, ciscoTcpCapability=ciscoTcpCapability)
