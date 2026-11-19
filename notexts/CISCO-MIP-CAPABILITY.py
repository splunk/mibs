#
# PySNMP MIB module CISCO-MIP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-MIP-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
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
ciscoMIPCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 203))
ciscoMIPCapability.setRevisions(('2003-12-24 00:00', '2002-10-08 00:00', '2000-11-17 00:00',))
if mibBuilder.loadTexts: ciscoMIPCapability.setLastUpdated('200312240000Z')
if mibBuilder.loadTexts: ciscoMIPCapability.setOrganization('Cisco Systems, Inc.')
ciscoMIPCapabilityV12R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 203, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMIPCapabilityV12R02 = ciscoMIPCapabilityV12R02.setProductRelease('Cisco IOS 12.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMIPCapabilityV12R02 = ciscoMIPCapabilityV12R02.setStatus('current')
ciscoMIPCapabilityV12R0204T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 203, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMIPCapabilityV12R0204T = ciscoMIPCapabilityV12R0204T.setProductRelease('Cisco IOS 12.2(4)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMIPCapabilityV12R0204T = ciscoMIPCapabilityV12R0204T.setStatus('current')
ciscoMIPCapabilityV12R0304T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 203, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMIPCapabilityV12R0304T = ciscoMIPCapabilityV12R0304T.setProductRelease('Cisco IOS 12.3(4)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMIPCapabilityV12R0304T = ciscoMIPCapabilityV12R0304T.setStatus('current')
mibBuilder.exportSymbols("CISCO-MIP-CAPABILITY", ciscoMIPCapability=ciscoMIPCapability, PYSNMP_MODULE_ID=ciscoMIPCapability, ciscoMIPCapabilityV12R0304T=ciscoMIPCapabilityV12R0304T, ciscoMIPCapabilityV12R02=ciscoMIPCapabilityV12R02, ciscoMIPCapabilityV12R0204T=ciscoMIPCapabilityV12R0204T)
