#
# PySNMP MIB module CISCO-STACK-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-STACK-CAPABILITY
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
ciscoStackCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 378))
ciscoStackCapability.setRevisions(('2008-03-19 00:00', '2006-03-15 00:00', '2005-01-19 00:00', '2003-12-17 00:00',))
if mibBuilder.loadTexts: ciscoStackCapability.setLastUpdated('200803190000Z')
if mibBuilder.loadTexts: ciscoStackCapability.setOrganization('Cisco Systems, Inc.')
ciscoStackCapCatOSV08R0101Cat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 378, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoStackCapCatOSV08R0101Cat6k = ciscoStackCapCatOSV08R0101Cat6k.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoStackCapCatOSV08R0101Cat6k = ciscoStackCapCatOSV08R0101Cat6k.setStatus('current')
ciscoStackCapV12R0111bEXCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 378, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoStackCapV12R0111bEXCat6k = ciscoStackCapV12R0111bEXCat6k.setProductRelease('Cisco IOS 12.1(11b)EX on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoStackCapV12R0111bEXCat6k = ciscoStackCapV12R0111bEXCat6k.setStatus('current')
ciscoStackCapV12R0112cE01PCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 378, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoStackCapV12R0112cE01PCat6k = ciscoStackCapV12R0112cE01PCat6k.setProductRelease('Cisco IOS 12.1(12c)E1 on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoStackCapV12R0112cE01PCat6k = ciscoStackCapV12R0112cE01PCat6k.setStatus('current')
ciscoStackCapCatOSV08R0701PCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 378, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoStackCapCatOSV08R0701PCat6k = ciscoStackCapCatOSV08R0701PCat6k.setProductRelease('Cisco CatOS 8.7(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoStackCapCatOSV08R0701PCat6k = ciscoStackCapCatOSV08R0701PCat6k.setStatus('current')
mibBuilder.exportSymbols("CISCO-STACK-CAPABILITY", PYSNMP_MODULE_ID=ciscoStackCapability, ciscoStackCapCatOSV08R0101Cat6k=ciscoStackCapCatOSV08R0101Cat6k, ciscoStackCapV12R0111bEXCat6k=ciscoStackCapV12R0111bEXCat6k, ciscoStackCapCatOSV08R0701PCat6k=ciscoStackCapCatOSV08R0701PCat6k, ciscoStackCapability=ciscoStackCapability, ciscoStackCapV12R0112cE01PCat6k=ciscoStackCapV12R0112cE01PCat6k)
