#
# PySNMP MIB module CISCO-SWITCH-NETFLOW-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SWITCH-NETFLOW-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
Percent, = mibBuilder.importSymbols("CISCO-QOS-PIB-MIB", "Percent")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, Bits, iso, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "Bits", "iso", "Unsigned32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSwitchNetflowCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 602))
ciscoSwitchNetflowCapability.setRevisions(('2012-09-11 00:00', '2010-11-17 00:00',))
if mibBuilder.loadTexts: ciscoSwitchNetflowCapability.setLastUpdated('201209110000Z')
if mibBuilder.loadTexts: ciscoSwitchNetflowCapability.setOrganization('Cisco Systems, Inc.')
csnCapV12R0250SYPCat6kPfc4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 602, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csnCapV12R0250SYPCat6kPfc4 = csnCapV12R0250SYPCat6kPfc4.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                    series devices with PFC4 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csnCapV12R0250SYPCat6kPfc4 = csnCapV12R0250SYPCat6kPfc4.setStatus('current')
csnCapV15R0101SYPCat6kPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 602, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csnCapV15R0101SYPCat6kPfc3 = csnCapV15R0101SYPCat6kPfc3.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices with PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csnCapV15R0101SYPCat6kPfc3 = csnCapV15R0101SYPCat6kPfc3.setStatus('current')
mibBuilder.exportSymbols("CISCO-SWITCH-NETFLOW-CAPABILITY", PYSNMP_MODULE_ID=ciscoSwitchNetflowCapability, csnCapV12R0250SYPCat6kPfc4=csnCapV12R0250SYPCat6kPfc4, ciscoSwitchNetflowCapability=ciscoSwitchNetflowCapability, csnCapV15R0101SYPCat6kPfc3=csnCapV15R0101SYPCat6kPfc3)
