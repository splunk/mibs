#
# PySNMP MIB module CISCO-ITP-GSCCP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ITP-GSCCP-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "iso", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoGsccpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 539))
ciscoGsccpCapability.setRevisions(('2007-05-17 00:00', '2005-01-14 00:00', '2004-10-07 00:00', '2003-12-08 00:00', '2003-10-28 00:00', '2003-05-20 00:00',))
if mibBuilder.loadTexts: ciscoGsccpCapability.setLastUpdated('200705170000Z')
if mibBuilder.loadTexts: ciscoGsccpCapability.setOrganization('Cisco Systems, Inc.')
ciscoGsccpCapabilityV12R0204MB10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 539, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0204MB10 = ciscoGsccpCapabilityV12R0204MB10.setProductRelease('Cisco IOS 12.2(4)MB10')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0204MB10 = ciscoGsccpCapabilityV12R0204MB10.setStatus('current')
ciscoGsccpCapabilityV12R0204MB13 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 539, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0204MB13 = ciscoGsccpCapabilityV12R0204MB13.setProductRelease('Cisco IOS 12.2(4)MB13')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0204MB13 = ciscoGsccpCapabilityV12R0204MB13.setStatus('current')
ciscoGsccpCapabilityV12R022004SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 539, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R022004SW = ciscoGsccpCapabilityV12R022004SW.setProductRelease('Cisco IOS 12.2(20.4)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R022004SW = ciscoGsccpCapabilityV12R022004SW.setStatus('current')
ciscoGsccpCapabilityV12R023000SW1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 539, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R023000SW1 = ciscoGsccpCapabilityV12R023000SW1.setProductRelease('Cisco IOS 12.2(23)SW1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R023000SW1 = ciscoGsccpCapabilityV12R023000SW1.setStatus('current')
ciscoGsccpCapabilityV12R025000SW1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 539, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R025000SW1 = ciscoGsccpCapabilityV12R025000SW1.setProductRelease('Cisco IOS 12.2(25)SW1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R025000SW1 = ciscoGsccpCapabilityV12R025000SW1.setStatus('current')
ciscoGsccpCapabilityV12R0218IXA = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 539, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0218IXA = ciscoGsccpCapabilityV12R0218IXA.setProductRelease('Cisco IOS 12.2(18)IXA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0218IXA = ciscoGsccpCapabilityV12R0218IXA.setStatus('current')
ciscoGsccpCapabilityV12R0411SW = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 539, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0411SW = ciscoGsccpCapabilityV12R0411SW.setProductRelease('Cisco IOS IOS 12.4(11)SW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGsccpCapabilityV12R0411SW = ciscoGsccpCapabilityV12R0411SW.setStatus('current')
mibBuilder.exportSymbols("CISCO-ITP-GSCCP-CAPABILITY", ciscoGsccpCapabilityV12R0204MB13=ciscoGsccpCapabilityV12R0204MB13, ciscoGsccpCapabilityV12R025000SW1=ciscoGsccpCapabilityV12R025000SW1, ciscoGsccpCapabilityV12R0218IXA=ciscoGsccpCapabilityV12R0218IXA, ciscoGsccpCapabilityV12R0204MB10=ciscoGsccpCapabilityV12R0204MB10, PYSNMP_MODULE_ID=ciscoGsccpCapability, ciscoGsccpCapabilityV12R0411SW=ciscoGsccpCapabilityV12R0411SW, ciscoGsccpCapabilityV12R022004SW=ciscoGsccpCapabilityV12R022004SW, ciscoGsccpCapabilityV12R023000SW1=ciscoGsccpCapabilityV12R023000SW1, ciscoGsccpCapability=ciscoGsccpCapability)
