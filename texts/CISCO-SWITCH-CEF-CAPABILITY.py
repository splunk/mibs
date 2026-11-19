#
# PySNMP MIB module CISCO-SWITCH-CEF-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SWITCH-CEF-CAPABILITY
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
ciscoSwitchCefCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 614))
ciscoSwitchCefCapability.setRevisions(('2012-09-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSwitchCefCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSwitchCefCapability.setLastUpdated('201209070000Z')
if mibBuilder.loadTexts: ciscoSwitchCefCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSwitchCefCapability.setContactInfo('Cisco Systems, Inc\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n                    San Jose, CA  95134\n                    USA\n\n               Tel: +1 800 553-NETS\n\n            E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSwitchCefCapability.setDescription('The capabilities description of CISCO-SWITCH-CEF-MIB.')
ciscoSwitchCefCapV15R0101SYPCat6kPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 614, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchCefCapV15R0101SYPCat6kPfc3 = ciscoSwitchCefCapV15R0101SYPCat6kPfc3.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices with PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchCefCapV15R0101SYPCat6kPfc3 = ciscoSwitchCefCapV15R0101SYPCat6kPfc3.setStatus('current')
if mibBuilder.loadTexts: ciscoSwitchCefCapV15R0101SYPCat6kPfc3.setDescription('CISCO-SWITCH-CEF-MIB capabilities.')
ciscoSwitchCefCapV15R0101SYPCat6kPfc4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 614, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchCefCapV15R0101SYPCat6kPfc4 = ciscoSwitchCefCapV15R0101SYPCat6kPfc4.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices with PFC4 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchCefCapV15R0101SYPCat6kPfc4 = ciscoSwitchCefCapV15R0101SYPCat6kPfc4.setStatus('current')
if mibBuilder.loadTexts: ciscoSwitchCefCapV15R0101SYPCat6kPfc4.setDescription('CISCO-SWITCH-CEF-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SWITCH-CEF-CAPABILITY", ciscoSwitchCefCapability=ciscoSwitchCefCapability, ciscoSwitchCefCapV15R0101SYPCat6kPfc3=ciscoSwitchCefCapV15R0101SYPCat6kPfc3, ciscoSwitchCefCapV15R0101SYPCat6kPfc4=ciscoSwitchCefCapV15R0101SYPCat6kPfc4, PYSNMP_MODULE_ID=ciscoSwitchCefCapability)
