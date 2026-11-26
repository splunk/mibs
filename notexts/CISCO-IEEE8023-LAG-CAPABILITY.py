#
# PySNMP MIB module CISCO-IEEE8023-LAG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IEEE8023-LAG-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIeee8023LagCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 337))
ciscoIeee8023LagCapability.setRevisions(('2006-04-19 00:00', '2004-02-06 00:00',))
if mibBuilder.loadTexts: ciscoIeee8023LagCapability.setLastUpdated('200604190000Z')
if mibBuilder.loadTexts: ciscoIeee8023LagCapability.setOrganization('Cisco Systems, Inc.')
cIeee8023LagCapV12R0111bEXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 337, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8023LagCapV12R0111bEXCat6K = cIeee8023LagCapV12R0111bEXCat6K.setProductRelease('Cisco IOS 12.1(11b)EX on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8023LagCapV12R0111bEXCat6K = cIeee8023LagCapV12R0111bEXCat6K.setStatus('current')
cIeee8023LagCapV12R0214SXCat6K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 337, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8023LagCapV12R0214SXCat6K = cIeee8023LagCapV12R0214SXCat6K.setProductRelease('Cisco IOS 12.2(14)SX on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8023LagCapV12R0214SXCat6K = cIeee8023LagCapV12R0214SXCat6K.setStatus('current')
cIeee8023LagCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 337, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8023LagCapCatOSV08R0101 = cIeee8023LagCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8023LagCapCatOSV08R0101 = cIeee8023LagCapCatOSV08R0101.setStatus('current')
cIeee8023LagCapCatOSV08R0601 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 337, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8023LagCapCatOSV08R0601 = cIeee8023LagCapCatOSV08R0601.setProductRelease('Cisco CatOS 8.6(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIeee8023LagCapCatOSV08R0601 = cIeee8023LagCapCatOSV08R0601.setStatus('current')
mibBuilder.exportSymbols("CISCO-IEEE8023-LAG-CAPABILITY", PYSNMP_MODULE_ID=ciscoIeee8023LagCapability, cIeee8023LagCapCatOSV08R0601=cIeee8023LagCapCatOSV08R0601, cIeee8023LagCapV12R0214SXCat6K=cIeee8023LagCapV12R0214SXCat6K, cIeee8023LagCapV12R0111bEXCat6K=cIeee8023LagCapV12R0111bEXCat6K, ciscoIeee8023LagCapability=ciscoIeee8023LagCapability, cIeee8023LagCapCatOSV08R0101=cIeee8023LagCapCatOSV08R0101)
