#
# PySNMP MIB module CISCO-ITP-GSP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ITP-GSP-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:24 2026
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
ciscoGspCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 306))
ciscoGspCapability.setRevisions(('2007-07-16 00:00', '2006-01-06 00:00', '2003-10-15 00:00', '2003-07-17 00:00',))
if mibBuilder.loadTexts: ciscoGspCapability.setLastUpdated('200707160000Z')
if mibBuilder.loadTexts: ciscoGspCapability.setOrganization('Cisco Systems, Inc.')
ciscoGspCapabilityV12R0204MB10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 306, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0204MB10 = ciscoGspCapabilityV12R0204MB10.setProductRelease('Cisco IOS 12.2(4)MB10')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0204MB10 = ciscoGspCapabilityV12R0204MB10.setStatus('current')
ciscoGspCapabilityV12R0219SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 306, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0219SW = ciscoGspCapabilityV12R0219SW.setProductRelease('Cisco IOS 12.2(19)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0219SW = ciscoGspCapabilityV12R0219SW.setStatus('current')
ciscoGspCapabilityV12R0225SW3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 306, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0225SW3 = ciscoGspCapabilityV12R0225SW3.setProductRelease('Cisco IOS 12.2(25)SW3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0225SW3 = ciscoGspCapabilityV12R0225SW3.setStatus('current')
ciscoGspCapabilityV12R0218IXA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 306, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0218IXA = ciscoGspCapabilityV12R0218IXA.setProductRelease('Cisco IOS 12.2(18)IXA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0218IXA = ciscoGspCapabilityV12R0218IXA.setStatus('current')
ciscoGspCapabilityV12R0411SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 306, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0411SW = ciscoGspCapabilityV12R0411SW.setProductRelease('Cisco IOS 12.4(11)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGspCapabilityV12R0411SW = ciscoGspCapabilityV12R0411SW.setStatus('current')
mibBuilder.exportSymbols("CISCO-ITP-GSP-CAPABILITY", PYSNMP_MODULE_ID=ciscoGspCapability, ciscoGspCapabilityV12R0218IXA=ciscoGspCapabilityV12R0218IXA, ciscoGspCapability=ciscoGspCapability, ciscoGspCapabilityV12R0225SW3=ciscoGspCapabilityV12R0225SW3, ciscoGspCapabilityV12R0411SW=ciscoGspCapabilityV12R0411SW, ciscoGspCapabilityV12R0219SW=ciscoGspCapabilityV12R0219SW, ciscoGspCapabilityV12R0204MB10=ciscoGspCapabilityV12R0204MB10)
