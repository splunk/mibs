#
# PySNMP MIB module CISCO-PAGP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-PAGP-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:44 2026
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
ciscoPagpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 391))
ciscoPagpCapability.setRevisions(('2011-09-27 00:00', '2010-11-17 00:00', '2010-05-06 00:00', '2004-03-30 00:00',))
if mibBuilder.loadTexts: ciscoPagpCapability.setLastUpdated('201109270000Z')
if mibBuilder.loadTexts: ciscoPagpCapability.setOrganization('Cisco Systems, Inc.')
ciscoPagpCapV12R0111bEXCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 391, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpCapV12R0111bEXCat6k = ciscoPagpCapV12R0111bEXCat6k.setProductRelease('Cisco IOS 12.1(11b)EX on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpCapV12R0111bEXCat6k = ciscoPagpCapV12R0111bEXCat6k.setStatus('current')
ciscoPagpCapV12R0217aSXCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 391, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpCapV12R0217aSXCat6k = ciscoPagpCapV12R0217aSXCat6k.setProductRelease('Cisco IOS 12.2(17a)SX on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpCapV12R0217aSXCat6k = ciscoPagpCapV12R0217aSXCat6k.setStatus('current')
ciscoPagpCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 391, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpCapCatOSV08R0101 = ciscoPagpCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpCapCatOSV08R0101 = ciscoPagpCapCatOSV08R0101.setStatus('current')
ciscoPagpCapV12R0254SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 391, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpCapV12R0254SGPCat4K = ciscoPagpCapV12R0254SGPCat4K.setProductRelease('Cisco IOS 12.2(54)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpCapV12R0254SGPCat4K = ciscoPagpCapV12R0254SGPCat4K.setStatus('current')
ciscoPagpCapV12R0250SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 391, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpCapV12R0250SYPCat6K = ciscoPagpCapV12R0250SYPCat6K.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpCapV12R0250SYPCat6K = ciscoPagpCapV12R0250SYPCat6K.setStatus('current')
ciscoPagpCapV15R0001SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 391, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpCapV15R0001SYPCat6k = ciscoPagpCapV15R0001SYPCat6k.setProductRelease('Cisco IOS 15.0(1)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPagpCapV15R0001SYPCat6k = ciscoPagpCapV15R0001SYPCat6k.setStatus('current')
mibBuilder.exportSymbols("CISCO-PAGP-CAPABILITY", ciscoPagpCapV12R0250SYPCat6K=ciscoPagpCapV12R0250SYPCat6K, ciscoPagpCapV12R0111bEXCat6k=ciscoPagpCapV12R0111bEXCat6k, PYSNMP_MODULE_ID=ciscoPagpCapability, ciscoPagpCapV15R0001SYPCat6k=ciscoPagpCapV15R0001SYPCat6k, ciscoPagpCapV12R0217aSXCat6k=ciscoPagpCapV12R0217aSXCat6k, ciscoPagpCapCatOSV08R0101=ciscoPagpCapCatOSV08R0101, ciscoPagpCapV12R0254SGPCat4K=ciscoPagpCapV12R0254SGPCat4K, ciscoPagpCapability=ciscoPagpCapability)
