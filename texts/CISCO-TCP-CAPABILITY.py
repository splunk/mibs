#
# PySNMP MIB module CISCO-TCP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-TCP-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:46 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("CISCO-TCP-CAPABILITY", ciscoTcpCapability=ciscoTcpCapability, cTcpCapabilityIOSXRV2R0CRS1=cTcpCapabilityIOSXRV2R0CRS1, PYSNMP_MODULE_ID=ciscoTcpCapability)
