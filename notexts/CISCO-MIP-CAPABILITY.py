#
# PySNMP MIB module CISCO-MIP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-MIP-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
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
mibBuilder.exportSymbols("CISCO-MIP-CAPABILITY", ciscoMIPCapabilityV12R0304T=ciscoMIPCapabilityV12R0304T, ciscoMIPCapabilityV12R02=ciscoMIPCapabilityV12R02, ciscoMIPCapabilityV12R0204T=ciscoMIPCapabilityV12R0204T, PYSNMP_MODULE_ID=ciscoMIPCapability, ciscoMIPCapability=ciscoMIPCapability)
