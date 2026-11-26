#
# PySNMP MIB module CISCO-WAN-RSRC-PART-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-WAN-RSRC-PART-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:01 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanRsrcPartCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 260))
ciscoWanRsrcPartCapability.setRevisions(('2005-04-26 00:00', '2004-09-29 00:00', '2003-11-13 00:00', '2002-11-11 00:00', '2002-03-13 00:00',))
if mibBuilder.loadTexts: ciscoWanRsrcPartCapability.setLastUpdated('200504260000Z')
if mibBuilder.loadTexts: ciscoWanRsrcPartCapability.setOrganization('Cisco Systems, Inc.')
cwRsrcPartCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 260, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityV2R00 = cwRsrcPartCapabilityV2R00.setProductRelease('MGX8850 Release 2.0.00\n                          and Release 2.1.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityV2R00 = cwRsrcPartCapabilityV2R00.setStatus('current')
cwRsrcPartCapabilityRpmV2R0160 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 260, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityRpmV2R0160 = cwRsrcPartCapabilityRpmV2R0160.setProductRelease('MGX8850 Release 2.1.60')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityRpmV2R0160 = cwRsrcPartCapabilityRpmV2R0160.setStatus('current')
cwRsrcPartCapabilityRpmxfV12R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 260, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityRpmxfV12R02 = cwRsrcPartCapabilityRpmxfV12R02.setProductRelease('IOS Release 12.2.\n                          MGX8850 Release 3.0.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityRpmxfV12R02 = cwRsrcPartCapabilityRpmxfV12R02.setStatus('current')
cwRsrcPartCapabilityV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 260, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityV4R00 = cwRsrcPartCapabilityV4R00.setProductRelease('MGX8850 Release 4.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityV4R00 = cwRsrcPartCapabilityV4R00.setStatus('current')
cwRsrcPartCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 260, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityV5R00 = cwRsrcPartCapabilityV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityV5R00 = cwRsrcPartCapabilityV5R00.setStatus('current')
cwRsrcPartCapabilityAxsmeV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 260, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityAxsmeV2R00 = cwRsrcPartCapabilityAxsmeV2R00.setProductRelease('MGX8850 Release 2.0.00\n                          and Release 2.1.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityAxsmeV2R00 = cwRsrcPartCapabilityAxsmeV2R00.setStatus('current')
cwRsrcPartCapabilityAxsmeV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 260, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityAxsmeV4R00 = cwRsrcPartCapabilityAxsmeV4R00.setProductRelease('MGX8850 Release 4.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityAxsmeV4R00 = cwRsrcPartCapabilityAxsmeV4R00.setStatus('current')
cwRsrcPartCapabilityAxsmeV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 260, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityAxsmeV5R00 = cwRsrcPartCapabilityAxsmeV5R00.setProductRelease('MGX8850 Release 5.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwRsrcPartCapabilityAxsmeV5R00 = cwRsrcPartCapabilityAxsmeV5R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-RSRC-PART-CAPABILITY", cwRsrcPartCapabilityRpmV2R0160=cwRsrcPartCapabilityRpmV2R0160, PYSNMP_MODULE_ID=ciscoWanRsrcPartCapability, cwRsrcPartCapabilityRpmxfV12R02=cwRsrcPartCapabilityRpmxfV12R02, cwRsrcPartCapabilityV4R00=cwRsrcPartCapabilityV4R00, cwRsrcPartCapabilityV5R00=cwRsrcPartCapabilityV5R00, cwRsrcPartCapabilityAxsmeV5R00=cwRsrcPartCapabilityAxsmeV5R00, cwRsrcPartCapabilityV2R00=cwRsrcPartCapabilityV2R00, cwRsrcPartCapabilityAxsmeV4R00=cwRsrcPartCapabilityAxsmeV4R00, cwRsrcPartCapabilityAxsmeV2R00=cwRsrcPartCapabilityAxsmeV2R00, ciscoWanRsrcPartCapability=ciscoWanRsrcPartCapability)
