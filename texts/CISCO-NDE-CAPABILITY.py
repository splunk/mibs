#
# PySNMP MIB module CISCO-NDE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-NDE-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoNdeCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 328))
ciscoNdeCapability.setRevisions(('2010-11-04 00:00', '2004-01-27 00:00', '2003-08-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoNdeCapability.setRevisionsDescriptions(('Added agent capability object\n        ciscoNdeCapV12R0250SYPCat6kPfc4.', 'Added agent capability object\n        ciscoNdeCapCatOSV08R0301.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoNdeCapability.setLastUpdated('201011040000Z')
if mibBuilder.loadTexts: ciscoNdeCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoNdeCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoNdeCapability.setDescription('The agent capabilities description of CISCO-NDE-MIB.')
ciscoNdeCapabilityV12R0119E = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 328, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNdeCapabilityV12R0119E = ciscoNdeCapabilityV12R0119E.setProductRelease('Cisco IOS 12.1(19E) on Catalyst 6000/6500 \n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNdeCapabilityV12R0119E = ciscoNdeCapabilityV12R0119E.setStatus('current')
if mibBuilder.loadTexts: ciscoNdeCapabilityV12R0119E.setDescription('CISCO-NDE-MIB agent capabilities.')
ciscoNdeCapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 328, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNdeCapCatOSV08R0301 = ciscoNdeCapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500 \n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNdeCapCatOSV08R0301 = ciscoNdeCapCatOSV08R0301.setStatus('current')
if mibBuilder.loadTexts: ciscoNdeCapCatOSV08R0301.setDescription('CISCO-NDE-MIB agent capabilities.')
ciscoNdeCapV12R0250SYPCat6kPfc4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 328, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNdeCapV12R0250SYPCat6kPfc4 = ciscoNdeCapV12R0250SYPCat6kPfc4.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500 \n                    series devices with PFC4 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNdeCapV12R0250SYPCat6kPfc4 = ciscoNdeCapV12R0250SYPCat6kPfc4.setStatus('current')
if mibBuilder.loadTexts: ciscoNdeCapV12R0250SYPCat6kPfc4.setDescription('CISCO-NDE-MIB is not supported.')
mibBuilder.exportSymbols("CISCO-NDE-CAPABILITY", ciscoNdeCapability=ciscoNdeCapability, ciscoNdeCapCatOSV08R0301=ciscoNdeCapCatOSV08R0301, ciscoNdeCapabilityV12R0119E=ciscoNdeCapabilityV12R0119E, ciscoNdeCapV12R0250SYPCat6kPfc4=ciscoNdeCapV12R0250SYPCat6kPfc4, PYSNMP_MODULE_ID=ciscoNdeCapability)
