#
# PySNMP MIB module CISCO-L2-CONTROL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-L2-CONTROL-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
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
mibBuilder.exportSymbols("CISCO-L2-CONTROL-CAPABILITY", clcCapabilityCatOSV08R0601=clcCapabilityCatOSV08R0601, ciscoL2ControlCapability=ciscoL2ControlCapability, clcCapabilityV6R0002U0102PN3K=clcCapabilityV6R0002U0102PN3K, clcCapabilityCatOSV08R0301=clcCapabilityCatOSV08R0301, clcCapabilityV12R0217aSXCat6K=clcCapabilityV12R0217aSXCat6K, clcCapabilityV12R0233SXHPCat6K=clcCapabilityV12R0233SXHPCat6K, PYSNMP_MODULE_ID=ciscoL2ControlCapability)
