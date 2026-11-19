#
# PySNMP MIB module CISCO-MODULE-AUTO-SHUTDOWN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-MODULE-AUTO-SHUTDOWN-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:07 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cmAutoShutdownCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 386))
cmAutoShutdownCapability.setRevisions(('2008-10-29 00:00', '2004-01-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cmAutoShutdownCapability.setRevisionsDescriptions(('Add the capability statements\n        cmAutoShutdownCapV12R0233SXH3PCat6K and\n        cmAutoShutdownCapV12R0233SXIPCat6K.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: cmAutoShutdownCapability.setLastUpdated('200810290000Z')
if mibBuilder.loadTexts: cmAutoShutdownCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cmAutoShutdownCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: cmAutoShutdownCapability.setDescription('The capabilities description of\n        CISCO-MODULE-AUTO-SHUTDOWN-MIB.')
cmAutoShutdownCapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 386, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmAutoShutdownCapCatOSV08R0301 = cmAutoShutdownCapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmAutoShutdownCapCatOSV08R0301 = cmAutoShutdownCapCatOSV08R0301.setStatus('current')
if mibBuilder.loadTexts: cmAutoShutdownCapCatOSV08R0301.setDescription('CISCO-MODULE-AUTO-SHUTDOWN-MIB capabilities.')
cmAutoShutdownCapV12R0233SXH3PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 386, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmAutoShutdownCapV12R0233SXH3PCat6K = cmAutoShutdownCapV12R0233SXH3PCat6K.setProductRelease('Cisco IOS 12.2(33)SXH3 on Catalyst 6000/6500\n                        series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmAutoShutdownCapV12R0233SXH3PCat6K = cmAutoShutdownCapV12R0233SXH3PCat6K.setStatus('current')
if mibBuilder.loadTexts: cmAutoShutdownCapV12R0233SXH3PCat6K.setDescription('CISCO-MODULE-AUTO-SHUTDOWN-MIB capabilities.')
cmAutoShutdownCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 386, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmAutoShutdownCapV12R0233SXIPCat6K = cmAutoShutdownCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                        series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmAutoShutdownCapV12R0233SXIPCat6K = cmAutoShutdownCapV12R0233SXIPCat6K.setStatus('current')
if mibBuilder.loadTexts: cmAutoShutdownCapV12R0233SXIPCat6K.setDescription('CISCO-MODULE-AUTO-SHUTDOWN-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-MODULE-AUTO-SHUTDOWN-CAPABILITY", cmAutoShutdownCapability=cmAutoShutdownCapability, PYSNMP_MODULE_ID=cmAutoShutdownCapability, cmAutoShutdownCapV12R0233SXH3PCat6K=cmAutoShutdownCapV12R0233SXH3PCat6K, cmAutoShutdownCapCatOSV08R0301=cmAutoShutdownCapCatOSV08R0301, cmAutoShutdownCapV12R0233SXIPCat6K=cmAutoShutdownCapV12R0233SXIPCat6K)
