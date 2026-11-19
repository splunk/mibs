#
# PySNMP MIB module CISCO-SRP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SRP-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:13 2026
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
ciscoSrpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 9999))
if mibBuilder.loadTexts: ciscoSrpCapability.setLastUpdated('200005260000Z')
if mibBuilder.loadTexts: ciscoSrpCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSrpCapability.setContactInfo('       Cisco Systems\n                                 Customer Service\n\n                         Postal: 170 West Tasman Drive\n                                 San Jose, CA  95134\n                                 USA\n\n                            Tel: +1 800 553-NETS\n\n                         E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSrpCapability.setDescription('Initial version of this MIB module.')
ciscoSrpCapabilityV12R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSrpCapabilityV12R00 = ciscoSrpCapabilityV12R00.setProductRelease('Cisco IOS 12.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSrpCapabilityV12R00 = ciscoSrpCapabilityV12R00.setStatus('current')
if mibBuilder.loadTexts: ciscoSrpCapabilityV12R00.setDescription('CISCO-SRP-MIB agent capabilities')
mibBuilder.exportSymbols("CISCO-SRP-CAPABILITY", ciscoSrpCapability=ciscoSrpCapability, PYSNMP_MODULE_ID=ciscoSrpCapability, ciscoSrpCapabilityV12R00=ciscoSrpCapabilityV12R00)
