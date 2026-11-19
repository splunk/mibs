#
# PySNMP MIB module CISCO-ENTITY-DISPLAY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ENTITY-DISPLAY-CAPABILITY
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
mibBuilder.exportSymbols("CISCO-ENTITY-DISPLAY-CAPABILITY", ciscoEntityDisplayCapability=ciscoEntityDisplayCapability, PYSNMP_MODULE_ID=ciscoEntityDisplayCapability, cEntDisplayCapV12R0233SXHPCat6k=cEntDisplayCapV12R0233SXHPCat6k, cEntDisplayCapCatOSV08R0301Cat6k=cEntDisplayCapCatOSV08R0301Cat6k, cEntDisplayCapV12R0250SYPCat6k=cEntDisplayCapV12R0250SYPCat6k)
