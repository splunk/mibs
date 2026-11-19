#
# PySNMP MIB module CISCO-SWITCH-STATS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SWITCH-STATS-CAPABILITY
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
ciscoSwitchStatsCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 600))
ciscoSwitchStatsCapability.setRevisions(('2013-09-25 00:00', '2013-07-26 00:00', '2010-11-11 00:00',))
if mibBuilder.loadTexts: ciscoSwitchStatsCapability.setLastUpdated('201309250000Z')
if mibBuilder.loadTexts: ciscoSwitchStatsCapability.setOrganization('Cisco Systems, Inc.')
csstCapV12R0250SYPCat6kPfc4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 600, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapV12R0250SYPCat6kPfc4 = csstCapV12R0250SYPCat6kPfc4.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                    series devices with PFC4 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapV12R0250SYPCat6kPfc4 = csstCapV12R0250SYPCat6kPfc4.setStatus('current')
csstCapNxOSV06R0104PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 600, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapNxOSV06R0104PN7k = csstCapNxOSV06R0104PN7k.setProductRelease('Cisco NX-OS 6.1(4) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapNxOSV06R0104PN7k = csstCapNxOSV06R0104PN7k.setStatus('current')
csstCapNxOSV06R0201PMds = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 600, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapNxOSV06R0201PMds = csstCapNxOSV06R0201PMds.setProductRelease('Cisco NX-OS 6.2(1) on MDS series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapNxOSV06R0201PMds = csstCapNxOSV06R0201PMds.setStatus('current')
csstCapV15R0102SYPCat6kPfc4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 600, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapV15R0102SYPCat6kPfc4 = csstCapV15R0102SYPCat6kPfc4.setProductRelease('Cisco IOS 15.1(2)SY on Catalyst 6000/6500\n                    series devices with PFC4 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapV15R0102SYPCat6kPfc4 = csstCapV15R0102SYPCat6kPfc4.setStatus('current')
csstCapV15R0102SYPCat6kPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 600, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapV15R0102SYPCat6kPfc3 = csstCapV15R0102SYPCat6kPfc3.setProductRelease('Cisco IOS 15.1(2)SY on Catalyst 6000/6500\n                    series devices with PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapV15R0102SYPCat6kPfc3 = csstCapV15R0102SYPCat6kPfc3.setStatus('current')
mibBuilder.exportSymbols("CISCO-SWITCH-STATS-CAPABILITY", csstCapV15R0102SYPCat6kPfc3=csstCapV15R0102SYPCat6kPfc3, PYSNMP_MODULE_ID=ciscoSwitchStatsCapability, csstCapNxOSV06R0201PMds=csstCapNxOSV06R0201PMds, csstCapV15R0102SYPCat6kPfc4=csstCapV15R0102SYPCat6kPfc4, ciscoSwitchStatsCapability=ciscoSwitchStatsCapability, csstCapNxOSV06R0104PN7k=csstCapNxOSV06R0104PN7k, csstCapV12R0250SYPCat6kPfc4=csstCapV12R0250SYPCat6kPfc4)
