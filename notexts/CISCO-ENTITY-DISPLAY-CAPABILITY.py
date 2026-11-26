#
# PySNMP MIB module CISCO-ENTITY-DISPLAY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ENTITY-DISPLAY-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
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
ciscoEntityDisplayCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 379))
ciscoEntityDisplayCapability.setRevisions(('2010-11-09 00:00', '2007-07-16 00:00', '2004-03-30 00:00',))
if mibBuilder.loadTexts: ciscoEntityDisplayCapability.setLastUpdated('201011090000Z')
if mibBuilder.loadTexts: ciscoEntityDisplayCapability.setOrganization('Cisco Systems, Inc.')
cEntDisplayCapCatOSV08R0301Cat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 379, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntDisplayCapCatOSV08R0301Cat6k = cEntDisplayCapCatOSV08R0301Cat6k.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntDisplayCapCatOSV08R0301Cat6k = cEntDisplayCapCatOSV08R0301Cat6k.setStatus('current')
cEntDisplayCapV12R0233SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 379, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntDisplayCapV12R0233SXHPCat6k = cEntDisplayCapV12R0233SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntDisplayCapV12R0233SXHPCat6k = cEntDisplayCapV12R0233SXHPCat6k.setStatus('current')
cEntDisplayCapV12R0250SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 379, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntDisplayCapV12R0250SYPCat6k = cEntDisplayCapV12R0250SYPCat6k.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntDisplayCapV12R0250SYPCat6k = cEntDisplayCapV12R0250SYPCat6k.setStatus('current')
mibBuilder.exportSymbols("CISCO-ENTITY-DISPLAY-CAPABILITY", PYSNMP_MODULE_ID=ciscoEntityDisplayCapability, cEntDisplayCapCatOSV08R0301Cat6k=cEntDisplayCapCatOSV08R0301Cat6k, cEntDisplayCapV12R0233SXHPCat6k=cEntDisplayCapV12R0233SXHPCat6k, cEntDisplayCapV12R0250SYPCat6k=cEntDisplayCapV12R0250SYPCat6k, ciscoEntityDisplayCapability=ciscoEntityDisplayCapability)
