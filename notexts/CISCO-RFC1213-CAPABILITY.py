#
# PySNMP MIB module CISCO-RFC1213-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-RFC1213-CAPABILITY
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
ciscoRFC1213Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 101))
ciscoRFC1213Capability.setRevisions(('2003-10-27 16:00', '2001-09-08 16:00', '1994-08-18 00:00',))
if mibBuilder.loadTexts: ciscoRFC1213Capability.setLastUpdated('200310271600Z')
if mibBuilder.loadTexts: ciscoRFC1213Capability.setOrganization('Cisco Systems, Inc.')
ciscoRFC1213CapabilityV10R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 101, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapabilityV10R02 = ciscoRFC1213CapabilityV10R02.setProductRelease('Cisco IOS 10.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapabilityV10R02 = ciscoRFC1213CapabilityV10R02.setStatus('current')
ciscoRFC1213CapabilityV12R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 101, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapabilityV12R02 = ciscoRFC1213CapabilityV12R02.setProductRelease('Cisco IOS 12.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapabilityV12R02 = ciscoRFC1213CapabilityV12R02.setStatus('current')
ciscoRFC1213CapabilityV12R00S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 101, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapabilityV12R00S = ciscoRFC1213CapabilityV12R00S.setProductRelease('Cisco IOS 12.0S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapabilityV12R00S = ciscoRFC1213CapabilityV12R00S.setStatus('current')
ciscoRFC1213CapabilityV12R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 101, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapabilityV12R01 = ciscoRFC1213CapabilityV12R01.setProductRelease('Cisco IOS 12.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapabilityV12R01 = ciscoRFC1213CapabilityV12R01.setStatus('current')
ciscoRFC1213CapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 101, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapCatOSV08R0101 = ciscoRFC1213CapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRFC1213CapCatOSV08R0101 = ciscoRFC1213CapCatOSV08R0101.setStatus('current')
mibBuilder.exportSymbols("CISCO-RFC1213-CAPABILITY", ciscoRFC1213CapCatOSV08R0101=ciscoRFC1213CapCatOSV08R0101, ciscoRFC1213CapabilityV12R02=ciscoRFC1213CapabilityV12R02, ciscoRFC1213CapabilityV12R00S=ciscoRFC1213CapabilityV12R00S, PYSNMP_MODULE_ID=ciscoRFC1213Capability, ciscoRFC1213CapabilityV12R01=ciscoRFC1213CapabilityV12R01, ciscoRFC1213CapabilityV10R02=ciscoRFC1213CapabilityV10R02, ciscoRFC1213Capability=ciscoRFC1213Capability)
