#
# PySNMP MIB module CISCO-IETF-PW-ENET-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IETF-PW-ENET-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:06 2026
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
ciscoIetfPwEnetCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 428))
ciscoIetfPwEnetCapability.setRevisions(('2004-11-29 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIetfPwEnetCapability.setRevisionsDescriptions(('Initial version:  ciscoIetfPwEnetCapabilityV12R00\n                ',))
if mibBuilder.loadTexts: ciscoIetfPwEnetCapability.setLastUpdated('200411291200Z')
if mibBuilder.loadTexts: ciscoIetfPwEnetCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIetfPwEnetCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: mpls-mib@cisco.com')
if mibBuilder.loadTexts: ciscoIetfPwEnetCapability.setDescription('Agent capabilities for CISCO-IETF-PW-ENET-MIB')
ciscoIetfPwEnetCapabilityV12R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 428, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfPwEnetCapabilityV12R00 = ciscoIetfPwEnetCapabilityV12R00.setProductRelease('Cisco IOS 12.0(28)S, Cisco IOS 12.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfPwEnetCapabilityV12R00 = ciscoIetfPwEnetCapabilityV12R00.setStatus('current')
if mibBuilder.loadTexts: ciscoIetfPwEnetCapabilityV12R00.setDescription('Pseudowire Ethernet MIB capabilities')
mibBuilder.exportSymbols("CISCO-IETF-PW-ENET-CAPABILITY", ciscoIetfPwEnetCapabilityV12R00=ciscoIetfPwEnetCapabilityV12R00, PYSNMP_MODULE_ID=ciscoIetfPwEnetCapability, ciscoIetfPwEnetCapability=ciscoIetfPwEnetCapability)
