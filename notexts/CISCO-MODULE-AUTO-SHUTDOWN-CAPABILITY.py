#
# PySNMP MIB module CISCO-MODULE-AUTO-SHUTDOWN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-MODULE-AUTO-SHUTDOWN-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:01 2026
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
cmAutoShutdownCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 386))
cmAutoShutdownCapability.setRevisions(('2008-10-29 00:00', '2004-01-19 00:00',))
if mibBuilder.loadTexts: cmAutoShutdownCapability.setLastUpdated('200810290000Z')
if mibBuilder.loadTexts: cmAutoShutdownCapability.setOrganization('Cisco Systems, Inc.')
cmAutoShutdownCapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 386, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmAutoShutdownCapCatOSV08R0301 = cmAutoShutdownCapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmAutoShutdownCapCatOSV08R0301 = cmAutoShutdownCapCatOSV08R0301.setStatus('current')
cmAutoShutdownCapV12R0233SXH3PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 386, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmAutoShutdownCapV12R0233SXH3PCat6K = cmAutoShutdownCapV12R0233SXH3PCat6K.setProductRelease('Cisco IOS 12.2(33)SXH3 on Catalyst 6000/6500\n                        series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmAutoShutdownCapV12R0233SXH3PCat6K = cmAutoShutdownCapV12R0233SXH3PCat6K.setStatus('current')
cmAutoShutdownCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 386, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmAutoShutdownCapV12R0233SXIPCat6K = cmAutoShutdownCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                        series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmAutoShutdownCapV12R0233SXIPCat6K = cmAutoShutdownCapV12R0233SXIPCat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-MODULE-AUTO-SHUTDOWN-CAPABILITY", cmAutoShutdownCapability=cmAutoShutdownCapability, PYSNMP_MODULE_ID=cmAutoShutdownCapability, cmAutoShutdownCapV12R0233SXIPCat6K=cmAutoShutdownCapV12R0233SXIPCat6K, cmAutoShutdownCapV12R0233SXH3PCat6K=cmAutoShutdownCapV12R0233SXH3PCat6K, cmAutoShutdownCapCatOSV08R0301=cmAutoShutdownCapCatOSV08R0301)
