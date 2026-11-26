#
# PySNMP MIB module CISCO-ITP-GRT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ITP-GRT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
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
ciscoItpGrtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 309))
ciscoItpGrtCapability.setRevisions(('2007-04-25 00:00', '2006-10-13 00:00', '2003-07-10 00:00',))
if mibBuilder.loadTexts: ciscoItpGrtCapability.setLastUpdated('200704250000Z')
if mibBuilder.loadTexts: ciscoItpGrtCapability.setOrganization('Cisco Systems, Inc.')
ciscoGrtCapabilityV12R0204MB10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 309, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtCapabilityV12R0204MB10 = ciscoGrtCapabilityV12R0204MB10.setProductRelease('Cisco IOS 12.2(4)MB10')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtCapabilityV12R0204MB10 = ciscoGrtCapabilityV12R0204MB10.setStatus('current')
ciscoGrtCapabilityV12R0218IXA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 309, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtCapabilityV12R0218IXA = ciscoGrtCapabilityV12R0218IXA.setProductRelease('Cisco IOS 12.2(18)IXA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtCapabilityV12R0218IXA = ciscoGrtCapabilityV12R0218IXA.setStatus('current')
ciscoGrtCapabilityV12R0411SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 309, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtCapabilityV12R0411SW = ciscoGrtCapabilityV12R0411SW.setProductRelease('Cisco IOS 12.4(11)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGrtCapabilityV12R0411SW = ciscoGrtCapabilityV12R0411SW.setStatus('current')
mibBuilder.exportSymbols("CISCO-ITP-GRT-CAPABILITY", ciscoGrtCapabilityV12R0218IXA=ciscoGrtCapabilityV12R0218IXA, PYSNMP_MODULE_ID=ciscoItpGrtCapability, ciscoItpGrtCapability=ciscoItpGrtCapability, ciscoGrtCapabilityV12R0204MB10=ciscoGrtCapabilityV12R0204MB10, ciscoGrtCapabilityV12R0411SW=ciscoGrtCapabilityV12R0411SW)
