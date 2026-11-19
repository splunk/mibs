#
# PySNMP MIB module CISCO-POWER-ETHERNET-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-POWER-ETHERNET-CAPABILITY
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
mibBuilder.exportSymbols("CISCO-POWER-ETHERNET-CAPABILITY", cPowerEthernetCapV12RO233SXJ2PCat6K=cPowerEthernetCapV12RO233SXJ2PCat6K, cPowerEthernetCapV12RO233SXHPCat6K=cPowerEthernetCapV12RO233SXHPCat6K, cPowerEthernetCapCatOSV08R0401=cPowerEthernetCapCatOSV08R0401, cPowerEthernetCapV12RO252SGPCat4K=cPowerEthernetCapV12RO252SGPCat4K, PYSNMP_MODULE_ID=ciscoPowerEthernetCapability, ciscoPowerEthernetCapability=ciscoPowerEthernetCapability, cPowerEthernetCapV15RO101SYPCat6K=cPowerEthernetCapV15RO101SYPCat6K, cPowerEthernetCapC3kV122SR035=cPowerEthernetCapC3kV122SR035)
