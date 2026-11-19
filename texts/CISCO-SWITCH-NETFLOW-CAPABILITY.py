#
# PySNMP MIB module CISCO-SWITCH-NETFLOW-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SWITCH-NETFLOW-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:06 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
Percent, = mibBuilder.importSymbols("CISCO-QOS-PIB-MIB", "Percent")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSwitchNetflowCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 602))
ciscoSwitchNetflowCapability.setRevisions(('2012-09-11 00:00', '2010-11-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSwitchNetflowCapability.setRevisionsDescriptions(('Added apability statement csnCapV15R0101SYPCat6kPfc3.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSwitchNetflowCapability.setLastUpdated('201209110000Z')
if mibBuilder.loadTexts: ciscoSwitchNetflowCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSwitchNetflowCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSwitchNetflowCapability.setDescription('The capabilities description of\n        CISCO-SWITCH-NETFLOW-MIB.')
csnCapV12R0250SYPCat6kPfc4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 602, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csnCapV12R0250SYPCat6kPfc4 = csnCapV12R0250SYPCat6kPfc4.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                    series devices with PFC4 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csnCapV12R0250SYPCat6kPfc4 = csnCapV12R0250SYPCat6kPfc4.setStatus('current')
if mibBuilder.loadTexts: csnCapV12R0250SYPCat6kPfc4.setDescription('CISCO-SWITCH-NETFLOW-MIB capabilities.')
csnCapV15R0101SYPCat6kPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 602, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csnCapV15R0101SYPCat6kPfc3 = csnCapV15R0101SYPCat6kPfc3.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices with PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csnCapV15R0101SYPCat6kPfc3 = csnCapV15R0101SYPCat6kPfc3.setStatus('current')
if mibBuilder.loadTexts: csnCapV15R0101SYPCat6kPfc3.setDescription('CISCO-SWITCH-NETFLOW-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SWITCH-NETFLOW-CAPABILITY", PYSNMP_MODULE_ID=ciscoSwitchNetflowCapability, ciscoSwitchNetflowCapability=ciscoSwitchNetflowCapability, csnCapV15R0101SYPCat6kPfc3=csnCapV15R0101SYPCat6kPfc3, csnCapV12R0250SYPCat6kPfc4=csnCapV12R0250SYPCat6kPfc4)
