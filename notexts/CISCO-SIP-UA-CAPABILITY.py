#
# PySNMP MIB module CISCO-SIP-UA-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SIP-UA-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
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
ciscoSipUaCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 172))
ciscoSipUaCapability.setRevisions(('2005-06-22 00:00', '2003-07-30 00:00', '2003-03-21 00:00', '2001-09-26 00:00', '2001-06-11 00:00',))
if mibBuilder.loadTexts: ciscoSipUaCapability.setLastUpdated('200506220000Z')
if mibBuilder.loadTexts: ciscoSipUaCapability.setOrganization('Cisco Systems, Inc.')
ciscoSipUaCapabilityV12R0202 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 172, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0202 = ciscoSipUaCapabilityV12R0202.setProductRelease('Cisco IOS 12.2(2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0202 = ciscoSipUaCapabilityV12R0202.setStatus('current')
ciscoSipUaCapabilityV12R0208 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 172, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0208 = ciscoSipUaCapabilityV12R0208.setProductRelease('Cisco IOS 12.2(8).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0208 = ciscoSipUaCapabilityV12R0208.setStatus('current')
ciscoSipUaCapabilityV12R0211 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 172, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0211 = ciscoSipUaCapabilityV12R0211.setProductRelease('Cisco IOS 12.2(11).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0211 = ciscoSipUaCapabilityV12R0211.setStatus('current')
ciscoSipUaCapabilityV12R0215 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 172, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0215 = ciscoSipUaCapabilityV12R0215.setProductRelease('Cisco IOS 12.2(15).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0215 = ciscoSipUaCapabilityV12R0215.setStatus('current')
ciscoSipUaCapabilityV12R0302 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 172, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0302 = ciscoSipUaCapabilityV12R0302.setProductRelease('Cisco IOS 12.3(2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0302 = ciscoSipUaCapabilityV12R0302.setStatus('current')
ciscoSipUaCapabilityV12R0402T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 172, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0402T = ciscoSipUaCapabilityV12R0402T.setProductRelease('Cisco IOS 12.4(2)T.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSipUaCapabilityV12R0402T = ciscoSipUaCapabilityV12R0402T.setStatus('current')
mibBuilder.exportSymbols("CISCO-SIP-UA-CAPABILITY", ciscoSipUaCapabilityV12R0208=ciscoSipUaCapabilityV12R0208, ciscoSipUaCapabilityV12R0302=ciscoSipUaCapabilityV12R0302, ciscoSipUaCapabilityV12R0202=ciscoSipUaCapabilityV12R0202, ciscoSipUaCapabilityV12R0211=ciscoSipUaCapabilityV12R0211, ciscoSipUaCapabilityV12R0215=ciscoSipUaCapabilityV12R0215, ciscoSipUaCapabilityV12R0402T=ciscoSipUaCapabilityV12R0402T, ciscoSipUaCapability=ciscoSipUaCapability, PYSNMP_MODULE_ID=ciscoSipUaCapability)
