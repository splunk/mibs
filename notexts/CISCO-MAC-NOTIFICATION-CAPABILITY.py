#
# PySNMP MIB module CISCO-MAC-NOTIFICATION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-MAC-NOTIFICATION-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:57 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMacNotificationCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 327))
ciscoMacNotificationCapability.setRevisions(('2007-07-09 00:00', '2004-02-05 00:00', '2003-11-12 00:00',))
if mibBuilder.loadTexts: ciscoMacNotificationCapability.setLastUpdated('200707090000Z')
if mibBuilder.loadTexts: ciscoMacNotificationCapability.setOrganization('Cisco Systems, Inc.')
cmnCapabilityCatOSV08R0101Cat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 327, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnCapabilityCatOSV08R0101Cat4K = cmnCapabilityCatOSV08R0101Cat4K.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 4000 series\n                        devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnCapabilityCatOSV08R0101Cat4K = cmnCapabilityCatOSV08R0101Cat4K.setStatus('current')
cmnCapabilityCatOSV08R0101Cat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 327, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnCapabilityCatOSV08R0101Cat6K = cmnCapabilityCatOSV08R0101Cat6K.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnCapabilityCatOSV08R0101Cat6K = cmnCapabilityCatOSV08R0101Cat6K.setStatus('current')
cmnCapabilityV12R0217SXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 327, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnCapabilityV12R0217SXCat6K = cmnCapabilityV12R0217SXCat6K.setProductRelease('Cisco IOS 12.2(17)SX on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnCapabilityV12R0217SXCat6K = cmnCapabilityV12R0217SXCat6K.setStatus('current')
cmnCapabilityCatOSV08R0301Cat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 327, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnCapabilityCatOSV08R0301Cat6K = cmnCapabilityCatOSV08R0301Cat6K.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                        and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnCapabilityCatOSV08R0301Cat6K = cmnCapabilityCatOSV08R0301Cat6K.setStatus('current')
cmnCapabilityV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 327, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnCapabilityV12R0233SXHPCat6K = cmnCapabilityV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmnCapabilityV12R0233SXHPCat6K = cmnCapabilityV12R0233SXHPCat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-MAC-NOTIFICATION-CAPABILITY", ciscoMacNotificationCapability=ciscoMacNotificationCapability, cmnCapabilityCatOSV08R0301Cat6K=cmnCapabilityCatOSV08R0301Cat6K, cmnCapabilityV12R0217SXCat6K=cmnCapabilityV12R0217SXCat6K, cmnCapabilityCatOSV08R0101Cat6K=cmnCapabilityCatOSV08R0101Cat6K, PYSNMP_MODULE_ID=ciscoMacNotificationCapability, cmnCapabilityCatOSV08R0101Cat4K=cmnCapabilityCatOSV08R0101Cat4K, cmnCapabilityV12R0233SXHPCat6K=cmnCapabilityV12R0233SXHPCat6K)
