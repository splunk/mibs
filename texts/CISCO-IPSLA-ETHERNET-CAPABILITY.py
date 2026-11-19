#
# PySNMP MIB module CISCO-IPSLA-ETHERNET-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IPSLA-ETHERNET-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:07 2026
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
ciscoIpSlaEthernetCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 498))
ciscoIpSlaEthernetCapability.setRevisions(('2006-02-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIpSlaEthernetCapability.setRevisionsDescriptions(('Initial Creation',))
if mibBuilder.loadTexts: ciscoIpSlaEthernetCapability.setLastUpdated('200602080000Z')
if mibBuilder.loadTexts: ciscoIpSlaEthernetCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIpSlaEthernetCapability.setContactInfo('       Cisco Systems\n                    Customer Service\n\n            Postal: 170 W Tasman Drive\n                    San Jose, CA  95134\n                    USA\n\n               Tel: +1 800 553-NETS\n\n            E-mail: cs-ipsla@cisco.com')
if mibBuilder.loadTexts: ciscoIpSlaEthernetCapability.setDescription('Agent capabilities for CISCO-IPSLA-ETHERNET-MIB')
ciscoIpSlaEthernetCapabilityRev1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 498, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpSlaEthernetCapabilityRev1 = ciscoIpSlaEthernetCapabilityRev1.setProductRelease('Cisco IOS 12.2(01)SRB')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpSlaEthernetCapabilityRev1 = ciscoIpSlaEthernetCapabilityRev1.setStatus('current')
if mibBuilder.loadTexts: ciscoIpSlaEthernetCapabilityRev1.setDescription('Cisco IP SLA ETHERNET MIB capabilities')
mibBuilder.exportSymbols("CISCO-IPSLA-ETHERNET-CAPABILITY", ciscoIpSlaEthernetCapability=ciscoIpSlaEthernetCapability, PYSNMP_MODULE_ID=ciscoIpSlaEthernetCapability, ciscoIpSlaEthernetCapabilityRev1=ciscoIpSlaEthernetCapabilityRev1)
