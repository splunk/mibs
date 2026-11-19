#
# PySNMP MIB module CISCO-NDE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-NDE-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:44 2026
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
ciscoNdeCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 328))
ciscoNdeCapability.setRevisions(('2010-11-04 00:00', '2004-01-27 00:00', '2003-08-26 00:00',))
if mibBuilder.loadTexts: ciscoNdeCapability.setLastUpdated('201011040000Z')
if mibBuilder.loadTexts: ciscoNdeCapability.setOrganization('Cisco Systems, Inc.')
ciscoNdeCapabilityV12R0119E = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 328, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNdeCapabilityV12R0119E = ciscoNdeCapabilityV12R0119E.setProductRelease('Cisco IOS 12.1(19E) on Catalyst 6000/6500 \n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNdeCapabilityV12R0119E = ciscoNdeCapabilityV12R0119E.setStatus('current')
ciscoNdeCapCatOSV08R0301 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 328, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNdeCapCatOSV08R0301 = ciscoNdeCapCatOSV08R0301.setProductRelease('Cisco CatOS 8.3(1) on Catalyst 6000/6500 \n                    and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNdeCapCatOSV08R0301 = ciscoNdeCapCatOSV08R0301.setStatus('current')
ciscoNdeCapV12R0250SYPCat6kPfc4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 328, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNdeCapV12R0250SYPCat6kPfc4 = ciscoNdeCapV12R0250SYPCat6kPfc4.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500 \n                    series devices with PFC4 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoNdeCapV12R0250SYPCat6kPfc4 = ciscoNdeCapV12R0250SYPCat6kPfc4.setStatus('current')
mibBuilder.exportSymbols("CISCO-NDE-CAPABILITY", ciscoNdeCapCatOSV08R0301=ciscoNdeCapCatOSV08R0301, ciscoNdeCapabilityV12R0119E=ciscoNdeCapabilityV12R0119E, ciscoNdeCapability=ciscoNdeCapability, PYSNMP_MODULE_ID=ciscoNdeCapability, ciscoNdeCapV12R0250SYPCat6kPfc4=ciscoNdeCapV12R0250SYPCat6kPfc4)
