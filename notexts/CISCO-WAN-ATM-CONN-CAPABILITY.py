#
# PySNMP MIB module CISCO-WAN-ATM-CONN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-WAN-ATM-CONN-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, Bits, iso, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "Bits", "iso", "Unsigned32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanAtmConnCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 380))
ciscoWanAtmConnCapability.setRevisions(('2004-02-07 00:00', '2002-03-26 00:00',))
if mibBuilder.loadTexts: ciscoWanAtmConnCapability.setLastUpdated('200402070000Z')
if mibBuilder.loadTexts: ciscoWanAtmConnCapability.setOrganization('Cisco Systems, Inc.')
cwAtmConnCapabilityAxsmV2R0160 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 380, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityAxsmV2R0160 = cwAtmConnCapabilityAxsmV2R0160.setProductRelease('MGX8850 Release 2.1.60.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityAxsmV2R0160 = cwAtmConnCapabilityAxsmV2R0160.setStatus('current')
cwAtmConnCapabilityAxsmeV2R0160 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 380, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityAxsmeV2R0160 = cwAtmConnCapabilityAxsmeV2R0160.setProductRelease('MGX8850 Release 2.1.60')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityAxsmeV2R0160 = cwAtmConnCapabilityAxsmeV2R0160.setStatus('current')
cwAtmConnCapabilityRpmprV2R0160 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 380, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityRpmprV2R0160 = cwAtmConnCapabilityRpmprV2R0160.setProductRelease('MGX8850 Release 2.1.60')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityRpmprV2R0160 = cwAtmConnCapabilityRpmprV2R0160.setStatus('current')
cwAtmConnCapabilityBpxsesV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 380, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityBpxsesV3R00 = cwAtmConnCapabilityBpxsesV3R00.setProductRelease('BPX SES Release 3.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityBpxsesV3R00 = cwAtmConnCapabilityBpxsesV3R00.setStatus('current')
cwAtmConnCapabilityAxsmV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 380, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityAxsmV3R00 = cwAtmConnCapabilityAxsmV3R00.setProductRelease('MGX8850 Release 3.0.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityAxsmV3R00 = cwAtmConnCapabilityAxsmV3R00.setStatus('current')
cwAtmConnCapabilityAxsmeV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 380, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityAxsmeV3R00 = cwAtmConnCapabilityAxsmeV3R00.setProductRelease('MGX8850 Release 3.0.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityAxsmeV3R00 = cwAtmConnCapabilityAxsmeV3R00.setStatus('current')
cwAtmConnCapabilityPxm1eV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 380, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityPxm1eV3R00 = cwAtmConnCapabilityPxm1eV3R00.setProductRelease('MGX8850 Release 3.0.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityPxm1eV3R00 = cwAtmConnCapabilityPxm1eV3R00.setStatus('current')
cwAtmConnCapabilityRpmprV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 380, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityRpmprV3R00 = cwAtmConnCapabilityRpmprV3R00.setProductRelease('MGX8850 Release 3.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityRpmprV3R00 = cwAtmConnCapabilityRpmprV3R00.setStatus('current')
cwAtmConnCapabilityRpmxfV12R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 380, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityRpmxfV12R02 = cwAtmConnCapabilityRpmxfV12R02.setProductRelease('IOS Release 12.2\n                          in MGX8850 Release 3.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityRpmxfV12R02 = cwAtmConnCapabilityRpmxfV12R02.setStatus('current')
cwAtmConnCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 380, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityV5R00 = cwAtmConnCapabilityV5R00.setProductRelease('MGX8850 Release 5.0.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnCapabilityV5R00 = cwAtmConnCapabilityV5R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-ATM-CONN-CAPABILITY", cwAtmConnCapabilityAxsmV3R00=cwAtmConnCapabilityAxsmV3R00, cwAtmConnCapabilityAxsmeV3R00=cwAtmConnCapabilityAxsmeV3R00, cwAtmConnCapabilityPxm1eV3R00=cwAtmConnCapabilityPxm1eV3R00, PYSNMP_MODULE_ID=ciscoWanAtmConnCapability, cwAtmConnCapabilityAxsmeV2R0160=cwAtmConnCapabilityAxsmeV2R0160, cwAtmConnCapabilityRpmxfV12R02=cwAtmConnCapabilityRpmxfV12R02, cwAtmConnCapabilityRpmprV2R0160=cwAtmConnCapabilityRpmprV2R0160, cwAtmConnCapabilityBpxsesV3R00=cwAtmConnCapabilityBpxsesV3R00, cwAtmConnCapabilityV5R00=cwAtmConnCapabilityV5R00, cwAtmConnCapabilityAxsmV2R0160=cwAtmConnCapabilityAxsmV2R0160, cwAtmConnCapabilityRpmprV3R00=cwAtmConnCapabilityRpmprV3R00, ciscoWanAtmConnCapability=ciscoWanAtmConnCapability)
