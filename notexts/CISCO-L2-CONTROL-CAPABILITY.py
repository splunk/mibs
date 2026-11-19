#
# PySNMP MIB module CISCO-L2-CONTROL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-L2-CONTROL-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:23 2026
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
ciscoL2ControlCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 397))
ciscoL2ControlCapability.setRevisions(('2013-10-16 00:00', '2007-06-30 00:00', '2007-02-28 00:00', '2004-11-01 00:00', '2004-03-29 00:00', '2003-10-31 00:00',))
if mibBuilder.loadTexts: ciscoL2ControlCapability.setLastUpdated('201310160000Z')
if mibBuilder.loadTexts: ciscoL2ControlCapability.setOrganization('Cisco Systems, Inc.')
clcCapabilityV12R0217aSXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 397, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clcCapabilityV12R0217aSXCat6K = clcCapabilityV12R0217aSXCat6K.setProductRelease('Cisco IOS 12.2(17a)SX on Catalyst 6000/6500\n                      and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clcCapabilityV12R0217aSXCat6K = clcCapabilityV12R0217aSXCat6K.setStatus('current')
clcCapabilityCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 397, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clcCapabilityCatOSV08R0301 = clcCapabilityCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clcCapabilityCatOSV08R0301 = clcCapabilityCatOSV08R0301.setStatus('current')
clcCapabilityCatOSV08R0601 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 397, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clcCapabilityCatOSV08R0601 = clcCapabilityCatOSV08R0601.setProductRelease('Cisco CatOS 8.6(1) on Catalyst 6000/6500\n                      and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clcCapabilityCatOSV08R0601 = clcCapabilityCatOSV08R0601.setStatus('current')
clcCapabilityV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 397, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clcCapabilityV12R0233SXHPCat6K = clcCapabilityV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                       series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clcCapabilityV12R0233SXHPCat6K = clcCapabilityV12R0233SXHPCat6K.setStatus('current')
clcCapabilityV6R0002U0102PN3K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 397, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clcCapabilityV6R0002U0102PN3K = clcCapabilityV6R0002U0102PN3K.setProductRelease('Cisco NX-OS 6.0(2)U1(2) on Nexus 3000\n                       series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clcCapabilityV6R0002U0102PN3K = clcCapabilityV6R0002U0102PN3K.setStatus('current')
mibBuilder.exportSymbols("CISCO-L2-CONTROL-CAPABILITY", PYSNMP_MODULE_ID=ciscoL2ControlCapability, ciscoL2ControlCapability=ciscoL2ControlCapability, clcCapabilityV12R0233SXHPCat6K=clcCapabilityV12R0233SXHPCat6K, clcCapabilityV6R0002U0102PN3K=clcCapabilityV6R0002U0102PN3K, clcCapabilityV12R0217aSXCat6K=clcCapabilityV12R0217aSXCat6K, clcCapabilityCatOSV08R0601=clcCapabilityCatOSV08R0601, clcCapabilityCatOSV08R0301=clcCapabilityCatOSV08R0301)
