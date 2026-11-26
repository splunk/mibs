#
# PySNMP MIB module CISCO-POWER-ETHERNET-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-POWER-ETHERNET-EXT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
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
ciscoPowerEthernetExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 406))
ciscoPowerEthernetExtCapability.setRevisions(('2013-07-16 00:00', '2012-12-12 00:00', '2012-04-04 00:00', '2009-05-29 00:00', '2008-10-28 00:00', '2007-06-29 00:00', '2007-06-27 00:00', '2007-02-08 00:00', '2006-12-20 00:00', '2006-10-19 00:00', '2004-06-15 00:00', '2004-06-07 00:00',))
if mibBuilder.loadTexts: ciscoPowerEthernetExtCapability.setLastUpdated('201307160000Z')
if mibBuilder.loadTexts: ciscoPowerEthernetExtCapability.setOrganization('Cisco Systems, Inc.')
cPowerEthExtCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 406, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapCatOSV08R0401 = cPowerEthExtCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapCatOSV08R0401 = cPowerEthExtCapCatOSV08R0401.setStatus('current')
cPowerEthExtCapCatOSV08R0501 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 406, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapCatOSV08R0501 = cPowerEthExtCapCatOSV08R0501.setProductRelease('Cisco CatOS 8.5(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapCatOSV08R0501 = cPowerEthExtCapCatOSV08R0501.setStatus('current')
cPowerEthExtCapC3kV122SR035 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 406, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapC3kV122SR035 = cPowerEthExtCapC3kV122SR035.setProductRelease('CISCO IOS 12.2S(0.35) for Cat3k')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapC3kV122SR035 = cPowerEthExtCapC3kV122SR035.setStatus('current')
cPowerEthExtCapCatOSV08R0601 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 406, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapCatOSV08R0601 = cPowerEthExtCapCatOSV08R0601.setProductRelease('Cisco CatOS 8.6(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapCatOSV08R0601 = cPowerEthExtCapCatOSV08R0601.setStatus('current')
cPowerEthExtCapC3kV122SU040 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 406, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapC3kV122SU040 = cPowerEthExtCapC3kV122SU040.setProductRelease('CISCO IOS 12.2S(0.40) for Cat3k')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapC3kV122SU040 = cPowerEthExtCapC3kV122SU040.setStatus('current')
cPowerEthExtCapV12R0233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 406, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapV12R0233SXHPCat6K = cPowerEthExtCapV12R0233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500 \n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapV12R0233SXHPCat6K = cPowerEthExtCapV12R0233SXHPCat6K.setStatus('current')
cPowerEthExtCapV12R0233SXIPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 406, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapV12R0233SXIPCat6K = cPowerEthExtCapV12R0233SXIPCat6K.setProductRelease('Cisco IOS 12.2(33)SXI on Catalyst 6000/6500 \n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapV12R0233SXIPCat6K = cPowerEthExtCapV12R0233SXIPCat6K.setStatus('current')
cPowerEthExtCapV12R0252SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 406, 8))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapV12R0252SGPCat4K = cPowerEthExtCapV12R0252SGPCat4K.setProductRelease('Cisco IOS 12.2(52)SG on CAT4K family\n                    switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapV12R0252SGPCat4K = cPowerEthExtCapV12R0252SGPCat4K.setStatus('current')
cPowerEthExtCapV12R0233SXJ2PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 406, 9))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapV12R0233SXJ2PCat6K = cPowerEthExtCapV12R0233SXJ2PCat6K.setProductRelease('Cisco IOS 12.2(33)SXJ2 on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapV12R0233SXJ2PCat6K = cPowerEthExtCapV12R0233SXJ2PCat6K.setStatus('current')
cPowerEthExtCapV15R0101SGCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 406, 10))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapV15R0101SGCat4K = cPowerEthExtCapV15R0101SGCat4K.setProductRelease('Cisco IOS 15.1(1)SG on Cat4K family switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapV15R0101SGCat4K = cPowerEthExtCapV15R0101SGCat4K.setStatus('current')
cPowerEthExtCapV15R0101SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 406, 11))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapV15R0101SYPCat6K = cPowerEthExtCapV15R0101SYPCat6K.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapV15R0101SYPCat6K = cPowerEthExtCapV15R0101SYPCat6K.setStatus('current')
cPowerEthExtCapV15R0102SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 406, 12))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapV15R0102SYPCat6K = cPowerEthExtCapV15R0102SYPCat6K.setProductRelease('Cisco IOS 15.1(2)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthExtCapV15R0102SYPCat6K = cPowerEthExtCapV15R0102SYPCat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-POWER-ETHERNET-EXT-CAPABILITY", cPowerEthExtCapV12R0233SXJ2PCat6K=cPowerEthExtCapV12R0233SXJ2PCat6K, cPowerEthExtCapV15R0102SYPCat6K=cPowerEthExtCapV15R0102SYPCat6K, cPowerEthExtCapCatOSV08R0501=cPowerEthExtCapCatOSV08R0501, ciscoPowerEthernetExtCapability=ciscoPowerEthernetExtCapability, cPowerEthExtCapCatOSV08R0401=cPowerEthExtCapCatOSV08R0401, cPowerEthExtCapV12R0233SXHPCat6K=cPowerEthExtCapV12R0233SXHPCat6K, cPowerEthExtCapC3kV122SU040=cPowerEthExtCapC3kV122SU040, cPowerEthExtCapV12R0233SXIPCat6K=cPowerEthExtCapV12R0233SXIPCat6K, cPowerEthExtCapV15R0101SGCat4K=cPowerEthExtCapV15R0101SGCat4K, cPowerEthExtCapV15R0101SYPCat6K=cPowerEthExtCapV15R0101SYPCat6K, cPowerEthExtCapV12R0252SGPCat4K=cPowerEthExtCapV12R0252SGPCat4K, cPowerEthExtCapCatOSV08R0601=cPowerEthExtCapCatOSV08R0601, PYSNMP_MODULE_ID=ciscoPowerEthernetExtCapability, cPowerEthExtCapC3kV122SR035=cPowerEthExtCapC3kV122SR035)
