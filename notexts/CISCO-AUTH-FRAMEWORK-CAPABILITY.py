#
# PySNMP MIB module CISCO-AUTH-FRAMEWORK-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-AUTH-FRAMEWORK-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:01 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoAuthFrameworkCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 573))
ciscoAuthFrameworkCapability.setRevisions(('2012-09-04 00:00', '2012-04-02 00:00', '2011-03-29 00:00', '2011-03-24 00:00', '2010-05-06 00:00', '2010-04-05 00:00', '2010-03-09 00:00', '2009-05-18 00:00', '2008-10-30 00:00',))
if mibBuilder.loadTexts: ciscoAuthFrameworkCapability.setLastUpdated('201209040000Z')
if mibBuilder.loadTexts: ciscoAuthFrameworkCapability.setOrganization('Cisco Systems, Inc.')
cafCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 573, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV12R0233SXIPCat6K = cafCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV12R0233SXIPCat6K = cafCapV12R0233SXIPCat6K.setStatus('current')
cafCapV12R0233SXI2PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 573, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV12R0233SXI2PCat6K = cafCapV12R0233SXI2PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI2 on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV12R0233SXI2PCat6K = cafCapV12R0233SXI2PCat6K.setStatus('current')
cafCapV12R0252SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 573, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV12R0252SGPCat4K = cafCapV12R0252SGPCat4K.setProductRelease('Cisco IOS 12.2(52)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV12R0252SGPCat4K = cafCapV12R0252SGPCat4K.setStatus('current')
cafCapV12R0233SXI4PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 573, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV12R0233SXI4PCat6K = cafCapV12R0233SXI4PCat6K.setProductRelease('Cisco IOS 12.2(33)SXI4 on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV12R0233SXI4PCat6K = cafCapV12R0233SXI4PCat6K.setStatus('current')
cafCapV12R0254SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 573, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV12R0254SGPCat4K = cafCapV12R0254SGPCat4K.setProductRelease('Cisco IOS 12.2(54)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV12R0254SGPCat4K = cafCapV12R0254SGPCat4K.setStatus('current')
cafCapV12R0233SXJPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 573, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV12R0233SXJPCat6K = cafCapV12R0233SXJPCat6K.setProductRelease('Cisco IOS 12.2(33)SXJ on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV12R0233SXJPCat6K = cafCapV12R0233SXJPCat6K.setStatus('current')
cafCapV15R0002SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 573, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV15R0002SGPCat4K = cafCapV15R0002SGPCat4K.setProductRelease('Cisco IOS 15.0(2)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV15R0002SGPCat4K = cafCapV15R0002SGPCat4K.setStatus('current')
cafCapV15R0101SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 573, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV15R0101SGPCat4K = cafCapV15R0101SGPCat4K.setProductRelease('Cisco IOS 15.1(1)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV15R0101SGPCat4K = cafCapV15R0101SGPCat4K.setStatus('current')
cafCapV15R0101SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 573, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV15R0101SYPCat6K = cafCapV15R0101SYPCat6K.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cafCapV15R0101SYPCat6K = cafCapV15R0101SYPCat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-AUTH-FRAMEWORK-CAPABILITY", cafCapV12R0233SXI4PCat6K=cafCapV12R0233SXI4PCat6K, PYSNMP_MODULE_ID=ciscoAuthFrameworkCapability, cafCapV12R0233SXI2PCat6K=cafCapV12R0233SXI2PCat6K, cafCapV15R0101SGPCat4K=cafCapV15R0101SGPCat4K, cafCapV15R0101SYPCat6K=cafCapV15R0101SYPCat6K, cafCapV12R0233SXJPCat6K=cafCapV12R0233SXJPCat6K, cafCapV12R0254SGPCat4K=cafCapV12R0254SGPCat4K, cafCapV15R0002SGPCat4K=cafCapV15R0002SGPCat4K, ciscoAuthFrameworkCapability=ciscoAuthFrameworkCapability, cafCapV12R0233SXIPCat6K=cafCapV12R0233SXIPCat6K, cafCapV12R0252SGPCat4K=cafCapV12R0252SGPCat4K)
