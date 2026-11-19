#
# PySNMP MIB module CISCO-SWITCH-STATS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SWITCH-STATS-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:13 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSwitchStatsCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 600))
ciscoSwitchStatsCapability.setRevisions(('2013-09-25 00:00', '2013-07-26 00:00', '2010-11-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSwitchStatsCapability.setRevisionsDescriptions(('Added capability statement\n        csstCapV15R0102SYPCat6kPfc4 and\n        csstCapV15R0102SYPCat6kPfc3.', 'Add agent capability statement\n        csstCapNxOSV06R0104PN7k and csstCapNxOSV06R0201PMds.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSwitchStatsCapability.setLastUpdated('201309250000Z')
if mibBuilder.loadTexts: ciscoSwitchStatsCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSwitchStatsCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSwitchStatsCapability.setDescription('The capabilities description of\n        CISCO-SWITCH-STATS-MIB.')
csstCapV12R0250SYPCat6kPfc4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 600, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapV12R0250SYPCat6kPfc4 = csstCapV12R0250SYPCat6kPfc4.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                    series devices with PFC4 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapV12R0250SYPCat6kPfc4 = csstCapV12R0250SYPCat6kPfc4.setStatus('current')
if mibBuilder.loadTexts: csstCapV12R0250SYPCat6kPfc4.setDescription('CISCO-SWITCH-STATS-MIB capabilities.')
csstCapNxOSV06R0104PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 600, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapNxOSV06R0104PN7k = csstCapNxOSV06R0104PN7k.setProductRelease('Cisco NX-OS 6.1(4) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapNxOSV06R0104PN7k = csstCapNxOSV06R0104PN7k.setStatus('current')
if mibBuilder.loadTexts: csstCapNxOSV06R0104PN7k.setDescription('CISCO-SWITCH-STATS-MIB capabilities.')
csstCapNxOSV06R0201PMds = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 600, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapNxOSV06R0201PMds = csstCapNxOSV06R0201PMds.setProductRelease('Cisco NX-OS 6.2(1) on MDS series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapNxOSV06R0201PMds = csstCapNxOSV06R0201PMds.setStatus('current')
if mibBuilder.loadTexts: csstCapNxOSV06R0201PMds.setDescription('CISCO-SWITCH-STATS-MIB capabilities.')
csstCapV15R0102SYPCat6kPfc4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 600, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapV15R0102SYPCat6kPfc4 = csstCapV15R0102SYPCat6kPfc4.setProductRelease('Cisco IOS 15.1(2)SY on Catalyst 6000/6500\n                    series devices with PFC4 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapV15R0102SYPCat6kPfc4 = csstCapV15R0102SYPCat6kPfc4.setStatus('current')
if mibBuilder.loadTexts: csstCapV15R0102SYPCat6kPfc4.setDescription('CISCO-SWITCH-STATS-MIB capabilities.')
csstCapV15R0102SYPCat6kPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 600, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapV15R0102SYPCat6kPfc3 = csstCapV15R0102SYPCat6kPfc3.setProductRelease('Cisco IOS 15.1(2)SY on Catalyst 6000/6500\n                    series devices with PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csstCapV15R0102SYPCat6kPfc3 = csstCapV15R0102SYPCat6kPfc3.setStatus('current')
if mibBuilder.loadTexts: csstCapV15R0102SYPCat6kPfc3.setDescription('CISCO-SWITCH-STATS-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SWITCH-STATS-CAPABILITY", csstCapNxOSV06R0104PN7k=csstCapNxOSV06R0104PN7k, csstCapNxOSV06R0201PMds=csstCapNxOSV06R0201PMds, PYSNMP_MODULE_ID=ciscoSwitchStatsCapability, csstCapV15R0102SYPCat6kPfc4=csstCapV15R0102SYPCat6kPfc4, csstCapV12R0250SYPCat6kPfc4=csstCapV12R0250SYPCat6kPfc4, csstCapV15R0102SYPCat6kPfc3=csstCapV15R0102SYPCat6kPfc3, ciscoSwitchStatsCapability=ciscoSwitchStatsCapability)
