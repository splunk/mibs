#
# PySNMP MIB module CISCO-IMAGE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IMAGE-CAPABILITY
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
ciscoImageMIBCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 580))
ciscoImageMIBCapability.setRevisions(('2009-03-26 00:00', '2003-09-15 00:00', '1995-01-25 00:00',))
if mibBuilder.loadTexts: ciscoImageMIBCapability.setLastUpdated('200903260000Z')
if mibBuilder.loadTexts: ciscoImageMIBCapability.setOrganization('Cisco Systems, Inc.')
ciscoImageMIBCapabilityV10R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 580, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageMIBCapabilityV10R01 = ciscoImageMIBCapabilityV10R01.setProductRelease('Cisco IOS 10.2')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageMIBCapabilityV10R01 = ciscoImageMIBCapabilityV10R01.setStatus('current')
ciscoImageCapabilityV12R0119ECat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 580, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageCapabilityV12R0119ECat6K = ciscoImageCapabilityV12R0119ECat6K.setProductRelease('Cisco IOS 12.1(19E) on Catalyst 6000/6500\n                      and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageCapabilityV12R0119ECat6K = ciscoImageCapabilityV12R0119ECat6K.setStatus('current')
ciscoImageCapabilityV12R0217SXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 580, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageCapabilityV12R0217SXCat6K = ciscoImageCapabilityV12R0217SXCat6K.setProductRelease('Cisco IOS 12.2(17SX) on Catalyst 6000/6500\n                      and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageCapabilityV12R0217SXCat6K = ciscoImageCapabilityV12R0217SXCat6K.setStatus('current')
ciscoImageCapabilityCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 580, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageCapabilityCatOSV08R0101 = ciscoImageCapabilityCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageCapabilityCatOSV08R0101 = ciscoImageCapabilityCatOSV08R0101.setStatus('current')
ciscoImageCapabilityGssV03R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 580, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageCapabilityGssV03R01 = ciscoImageCapabilityGssV03R01.setProductRelease('Global Site Selector(GSS) 3.1(0)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoImageCapabilityGssV03R01 = ciscoImageCapabilityGssV03R01.setStatus('current')
mibBuilder.exportSymbols("CISCO-IMAGE-CAPABILITY", ciscoImageCapabilityGssV03R01=ciscoImageCapabilityGssV03R01, ciscoImageMIBCapability=ciscoImageMIBCapability, ciscoImageCapabilityCatOSV08R0101=ciscoImageCapabilityCatOSV08R0101, ciscoImageMIBCapabilityV10R01=ciscoImageMIBCapabilityV10R01, PYSNMP_MODULE_ID=ciscoImageMIBCapability, ciscoImageCapabilityV12R0119ECat6K=ciscoImageCapabilityV12R0119ECat6K, ciscoImageCapabilityV12R0217SXCat6K=ciscoImageCapabilityV12R0217SXCat6K)
