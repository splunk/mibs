#
# PySNMP MIB module CISCO-SMON-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SMON-CAPABILITY
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
ciscoSmonCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 381))
ciscoSmonCapability.setRevisions(('2004-01-22 00:00',))
if mibBuilder.loadTexts: ciscoSmonCapability.setLastUpdated('200401220000Z')
if mibBuilder.loadTexts: ciscoSmonCapability.setOrganization('Cisco Systems, Inc.')
csCapV12R0214SXCat6KPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 381, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csCapV12R0214SXCat6KPfc3 = csCapV12R0214SXCat6KPfc3.setProductRelease('Cisco IOS 12.2(14)SX on Catalyst 6000/6500\n                         and Cisco 7600 series devices with the \n                         Policy Feature Card 3 (PFC 3).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csCapV12R0214SXCat6KPfc3 = csCapV12R0214SXCat6KPfc3.setStatus('current')
csCapV12R0113ECat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 381, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csCapV12R0113ECat6KPfc2 = csCapV12R0113ECat6KPfc2.setProductRelease('Cisco IOS 12.1(13)E on Catalyst 6000/6500\n                         and Cisco 7600 series devices with the \n                         Policy Feature Card 2 (PFC 2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csCapV12R0113ECat6KPfc2 = csCapV12R0113ECat6KPfc2.setStatus('current')
csCapCatOSV07R0102Cat6KPfc2 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 381, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csCapCatOSV07R0102Cat6KPfc2 = csCapCatOSV07R0102Cat6KPfc2.setProductRelease('Cisco CatOS 7.1(2) on Catalyst 6000/6500\n                         and Cisco 7600 series devices with the \n                         Policy Feature Card 2 (PFC 2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csCapCatOSV07R0102Cat6KPfc2 = csCapCatOSV07R0102Cat6KPfc2.setStatus('current')
mibBuilder.exportSymbols("CISCO-SMON-CAPABILITY", PYSNMP_MODULE_ID=ciscoSmonCapability, csCapCatOSV07R0102Cat6KPfc2=csCapCatOSV07R0102Cat6KPfc2, csCapV12R0113ECat6KPfc2=csCapV12R0113ECat6KPfc2, ciscoSmonCapability=ciscoSmonCapability, csCapV12R0214SXCat6KPfc3=csCapV12R0214SXCat6KPfc3)
