#
# PySNMP MIB module CISCO-NETFLOW-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-NETFLOW-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:24 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NfTopFlowsSortTypes, = mibBuilder.importSymbols("CISCO-NETFLOW-MIB", "NfTopFlowsSortTypes")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoNetflowCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 407))
ciscoNetflowCapability.setRevisions(('2010-11-04 00:01', '2007-08-24 00:00', '2004-06-21 00:00',))
if mibBuilder.loadTexts: ciscoNetflowCapability.setLastUpdated('201011040001Z')
if mibBuilder.loadTexts: ciscoNetflowCapability.setOrganization('Cisco Systems, Inc.')
ciscoNetflowCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 407, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNetflowCapCatOSV08R0401 = ciscoNetflowCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNetflowCapCatOSV08R0401 = ciscoNetflowCapCatOSV08R0401.setStatus('current')
ciscoNetflowCapV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 407, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNetflowCapV12R0233SXHPCat6K = ciscoNetflowCapV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNetflowCapV12R0233SXHPCat6K = ciscoNetflowCapV12R0233SXHPCat6K.setStatus('current')
ciscoNetflowCapV12R0250SYPCat6kPfc4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 407, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNetflowCapV12R0250SYPCat6kPfc4 = ciscoNetflowCapV12R0250SYPCat6kPfc4.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500 \n                    series devices with PFC4 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNetflowCapV12R0250SYPCat6kPfc4 = ciscoNetflowCapV12R0250SYPCat6kPfc4.setStatus('current')
mibBuilder.exportSymbols("CISCO-NETFLOW-CAPABILITY", ciscoNetflowCapCatOSV08R0401=ciscoNetflowCapCatOSV08R0401, ciscoNetflowCapability=ciscoNetflowCapability, ciscoNetflowCapV12R0233SXHPCat6K=ciscoNetflowCapV12R0233SXHPCat6K, PYSNMP_MODULE_ID=ciscoNetflowCapability, ciscoNetflowCapV12R0250SYPCat6kPfc4=ciscoNetflowCapV12R0250SYPCat6kPfc4)
