#
# PySNMP MIB module CISCO-SWITCH-STATS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SWITCH-STATS-CAPABILITY
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
mibBuilder.exportSymbols("CISCO-SWITCH-STATS-CAPABILITY", PYSNMP_MODULE_ID=ciscoSwitchStatsCapability, ciscoSwitchStatsCapability=ciscoSwitchStatsCapability, csstCapV15R0102SYPCat6kPfc4=csstCapV15R0102SYPCat6kPfc4, csstCapV12R0250SYPCat6kPfc4=csstCapV12R0250SYPCat6kPfc4, csstCapNxOSV06R0201PMds=csstCapNxOSV06R0201PMds, csstCapNxOSV06R0104PN7k=csstCapNxOSV06R0104PN7k, csstCapV15R0102SYPCat6kPfc3=csstCapV15R0102SYPCat6kPfc3)
