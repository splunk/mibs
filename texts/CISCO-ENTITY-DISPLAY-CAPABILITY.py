#
# PySNMP MIB module CISCO-ENTITY-DISPLAY-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ENTITY-DISPLAY-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:06 2026
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
ciscoEntityDisplayCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 379))
ciscoEntityDisplayCapability.setRevisions(('2010-11-09 00:00', '2007-07-16 00:00', '2004-03-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEntityDisplayCapability.setRevisionsDescriptions(('Added the agent capabilities statement\n        cEntDisplayCapV12R0250SYPCat6k.', 'Added the agent capabilities statement\n        cEntDisplayCapV12R0233SXHPCat6k.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoEntityDisplayCapability.setLastUpdated('201011090000Z')
if mibBuilder.loadTexts: ciscoEntityDisplayCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEntityDisplayCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-displaymib@cisco.com,\n            cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoEntityDisplayCapability.setDescription('The capabilities description of\n        CISCO-ENTITY-DISPLAY-MIB.')
cEntDisplayCapCatOSV08R0301Cat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 379, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntDisplayCapCatOSV08R0301Cat6k = cEntDisplayCapCatOSV08R0301Cat6k.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500\n                          and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntDisplayCapCatOSV08R0301Cat6k = cEntDisplayCapCatOSV08R0301Cat6k.setStatus('current')
if mibBuilder.loadTexts: cEntDisplayCapCatOSV08R0301Cat6k.setDescription('CISCO-ENTITY-DISPLAY-MIB capabilities.')
cEntDisplayCapV12R0233SXHPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 379, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntDisplayCapV12R0233SXHPCat6k = cEntDisplayCapV12R0233SXHPCat6k.setProductRelease('Cisco IOS 12.2(33)SXH on Catalyst 6000/6500\n                         series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntDisplayCapV12R0233SXHPCat6k = cEntDisplayCapV12R0233SXHPCat6k.setStatus('current')
if mibBuilder.loadTexts: cEntDisplayCapV12R0233SXHPCat6k.setDescription('CISCO-ENTITY-DISPLAY-MIB capabilities.')
cEntDisplayCapV12R0250SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 379, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntDisplayCapV12R0250SYPCat6k = cEntDisplayCapV12R0250SYPCat6k.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cEntDisplayCapV12R0250SYPCat6k = cEntDisplayCapV12R0250SYPCat6k.setStatus('current')
if mibBuilder.loadTexts: cEntDisplayCapV12R0250SYPCat6k.setDescription('CISCO-ENTITY-DISPLAY-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-ENTITY-DISPLAY-CAPABILITY", cEntDisplayCapCatOSV08R0301Cat6k=cEntDisplayCapCatOSV08R0301Cat6k, cEntDisplayCapV12R0233SXHPCat6k=cEntDisplayCapV12R0233SXHPCat6k, ciscoEntityDisplayCapability=ciscoEntityDisplayCapability, PYSNMP_MODULE_ID=ciscoEntityDisplayCapability, cEntDisplayCapV12R0250SYPCat6k=cEntDisplayCapV12R0250SYPCat6k)
