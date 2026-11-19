#
# PySNMP MIB module CISCO-NETFLOW-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-NETFLOW-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:07 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NfTopFlowsSortTypes, = mibBuilder.importSymbols("CISCO-NETFLOW-MIB", "NfTopFlowsSortTypes")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoNetflowCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 407))
ciscoNetflowCapability.setRevisions(('2010-11-04 00:01', '2007-08-24 00:00', '2004-06-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoNetflowCapability.setRevisionsDescriptions(('Added capability statement\n        ciscoNetflowCapV12R0250SYPCat6kPfc4.', 'Added ciscoNetflowCapV12R0233SXHPCat6K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoNetflowCapability.setLastUpdated('201011040001Z')
if mibBuilder.loadTexts: ciscoNetflowCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoNetflowCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com\n            cs-netflow-mib@cisco.com')
if mibBuilder.loadTexts: ciscoNetflowCapability.setDescription('The capabilities description of CISCO-NETFLOW-MIB.')
ciscoNetflowCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 407, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNetflowCapCatOSV08R0401 = ciscoNetflowCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNetflowCapCatOSV08R0401 = ciscoNetflowCapCatOSV08R0401.setStatus('current')
if mibBuilder.loadTexts: ciscoNetflowCapCatOSV08R0401.setDescription('CISCO-NETFLOW-MIB capabilities.')
ciscoNetflowCapV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 407, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNetflowCapV12R0233SXHPCat6K = ciscoNetflowCapV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNetflowCapV12R0233SXHPCat6K = ciscoNetflowCapV12R0233SXHPCat6K.setStatus('current')
if mibBuilder.loadTexts: ciscoNetflowCapV12R0233SXHPCat6K.setDescription('CISCO-NETFLOW-MIB capabilities.')
ciscoNetflowCapV12R0250SYPCat6kPfc4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 407, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNetflowCapV12R0250SYPCat6kPfc4 = ciscoNetflowCapV12R0250SYPCat6kPfc4.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500 \n                    series devices with PFC4 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNetflowCapV12R0250SYPCat6kPfc4 = ciscoNetflowCapV12R0250SYPCat6kPfc4.setStatus('current')
if mibBuilder.loadTexts: ciscoNetflowCapV12R0250SYPCat6kPfc4.setDescription('CISCO-NETFLOW-MIB is not supported.')
mibBuilder.exportSymbols("CISCO-NETFLOW-CAPABILITY", ciscoNetflowCapV12R0250SYPCat6kPfc4=ciscoNetflowCapV12R0250SYPCat6kPfc4, ciscoNetflowCapCatOSV08R0401=ciscoNetflowCapCatOSV08R0401, ciscoNetflowCapability=ciscoNetflowCapability, ciscoNetflowCapV12R0233SXHPCat6K=ciscoNetflowCapV12R0233SXHPCat6K, PYSNMP_MODULE_ID=ciscoNetflowCapability)
