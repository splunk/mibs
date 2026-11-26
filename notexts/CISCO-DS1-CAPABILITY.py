#
# PySNMP MIB module CISCO-DS1-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DS1-CAPABILITY
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
ciscoDs1Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 273))
ciscoDs1Capability.setRevisions(('2007-10-31 00:00', '2007-09-10 00:00', '2007-05-11 00:00', '2006-06-16 00:00', '2005-07-11 00:00', '2003-12-22 00:00', '2002-04-28 00:00',))
if mibBuilder.loadTexts: ciscoDs1Capability.setLastUpdated('200710310000Z')
if mibBuilder.loadTexts: ciscoDs1Capability.setOrganization('Cisco Systems, Inc.')
ciscoDs1AxsmeCapabilityV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 273, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1AxsmeCapabilityV3R00 = ciscoDs1AxsmeCapabilityV3R00.setProductRelease('MGX8850 Release 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1AxsmeCapabilityV3R00 = ciscoDs1AxsmeCapabilityV3R00.setStatus('current')
ciscoDs1CapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 273, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityV5R00 = ciscoDs1CapabilityV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityV5R00 = ciscoDs1CapabilityV5R00.setStatus('current')
ciscoDs1CapabilityV5R100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 273, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityV5R100 = ciscoDs1CapabilityV5R100.setProductRelease('MGX8880 Release 5.1.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityV5R100 = ciscoDs1CapabilityV5R100.setStatus('current')
ciscoDs1CapabilityV5R310 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 273, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityV5R310 = ciscoDs1CapabilityV5R310.setProductRelease('MGX8880 Release 5.3.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityV5R310 = ciscoDs1CapabilityV5R310.setStatus('current')
ciscoDs1CapabilityMARsV12R5T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 273, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityMARsV12R5T = ciscoDs1CapabilityMARsV12R5T.setProductRelease('IOS 12.5T for Cisco Access Routers and ISRs')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityMARsV12R5T = ciscoDs1CapabilityMARsV12R5T.setStatus('current')
ciscoDs1CapabilityAS5xxxV12R5T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 273, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityAS5xxxV12R5T = ciscoDs1CapabilityAS5xxxV12R5T.setProductRelease('IOS 12.5T for Cisco Access Servers')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityAS5xxxV12R5T = ciscoDs1CapabilityAS5xxxV12R5T.setStatus('current')
ciscoDs1CapabilityV5R500 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 273, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityV5R500 = ciscoDs1CapabilityV5R500.setProductRelease('MGX8880 Release 5.5.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs1CapabilityV5R500 = ciscoDs1CapabilityV5R500.setStatus('current')
mibBuilder.exportSymbols("CISCO-DS1-CAPABILITY", ciscoDs1CapabilityV5R100=ciscoDs1CapabilityV5R100, ciscoDs1CapabilityV5R00=ciscoDs1CapabilityV5R00, ciscoDs1Capability=ciscoDs1Capability, PYSNMP_MODULE_ID=ciscoDs1Capability, ciscoDs1CapabilityAS5xxxV12R5T=ciscoDs1CapabilityAS5xxxV12R5T, ciscoDs1CapabilityV5R310=ciscoDs1CapabilityV5R310, ciscoDs1AxsmeCapabilityV3R00=ciscoDs1AxsmeCapabilityV3R00, ciscoDs1CapabilityV5R500=ciscoDs1CapabilityV5R500, ciscoDs1CapabilityMARsV12R5T=ciscoDs1CapabilityMARsV12R5T)
