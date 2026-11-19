#
# PySNMP MIB module CISCO-POWER-ETHERNET-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-POWER-ETHERNET-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "iso", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoPowerEthernetCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 412))
ciscoPowerEthernetCapability.setRevisions(('2012-09-04 00:00', '2012-04-06 00:00', '2009-02-14 00:00', '2007-07-09 00:00', '2007-02-08 00:00', '2006-05-31 00:00', '2004-06-28 00:00',))
if mibBuilder.loadTexts: ciscoPowerEthernetCapability.setLastUpdated('201209040000Z')
if mibBuilder.loadTexts: ciscoPowerEthernetCapability.setOrganization('Cisco Systems, Inc.')
cPowerEthernetCapCatOSV08R0401 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 412, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthernetCapCatOSV08R0401 = cPowerEthernetCapCatOSV08R0401.setProductRelease('Cisco CatOS 8.4(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthernetCapCatOSV08R0401 = cPowerEthernetCapCatOSV08R0401.setStatus('current')
cPowerEthernetCapC3kV122SR035 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 412, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthernetCapC3kV122SR035 = cPowerEthernetCapC3kV122SR035.setProductRelease('CISCO IOS 12.2S(0.35) for cat3k')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthernetCapC3kV122SR035 = cPowerEthernetCapC3kV122SR035.setStatus('current')
cPowerEthernetCapV12RO233SXHPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 412, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthernetCapV12RO233SXHPCat6K = cPowerEthernetCapV12RO233SXHPCat6K.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthernetCapV12RO233SXHPCat6K = cPowerEthernetCapV12RO233SXHPCat6K.setStatus('current')
cPowerEthernetCapV12RO252SGPCat4K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 412, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthernetCapV12RO252SGPCat4K = cPowerEthernetCapV12RO252SGPCat4K.setProductRelease('Cisco IOS 12.2(52)SG on CAT4K family\n                    switches.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthernetCapV12RO252SGPCat4K = cPowerEthernetCapV12RO252SGPCat4K.setStatus('current')
cPowerEthernetCapV12RO233SXJ2PCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 412, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthernetCapV12RO233SXJ2PCat6K = cPowerEthernetCapV12RO233SXJ2PCat6K.setProductRelease('Cisco IOS 12.2(33)SXJ2 on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthernetCapV12RO233SXJ2PCat6K = cPowerEthernetCapV12RO233SXJ2PCat6K.setStatus('current')
cPowerEthernetCapV15RO101SYPCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 412, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthernetCapV15RO101SYPCat6K = cPowerEthernetCapV15RO101SYPCat6K.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cPowerEthernetCapV15RO101SYPCat6K = cPowerEthernetCapV15RO101SYPCat6K.setStatus('current')
mibBuilder.exportSymbols("CISCO-POWER-ETHERNET-CAPABILITY", cPowerEthernetCapV12RO233SXHPCat6K=cPowerEthernetCapV12RO233SXHPCat6K, PYSNMP_MODULE_ID=ciscoPowerEthernetCapability, cPowerEthernetCapV12RO252SGPCat4K=cPowerEthernetCapV12RO252SGPCat4K, cPowerEthernetCapV15RO101SYPCat6K=cPowerEthernetCapV15RO101SYPCat6K, cPowerEthernetCapV12RO233SXJ2PCat6K=cPowerEthernetCapV12RO233SXJ2PCat6K, cPowerEthernetCapCatOSV08R0401=cPowerEthernetCapCatOSV08R0401, ciscoPowerEthernetCapability=ciscoPowerEthernetCapability, cPowerEthernetCapC3kV122SR035=cPowerEthernetCapC3kV122SR035)
