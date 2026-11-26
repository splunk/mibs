#
# PySNMP MIB module CISCO-SWITCH-CEF-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SWITCH-CEF-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
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
ciscoSwitchCefCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 614))
ciscoSwitchCefCapability.setRevisions(('2012-09-07 00:00',))
if mibBuilder.loadTexts: ciscoSwitchCefCapability.setLastUpdated('201209070000Z')
if mibBuilder.loadTexts: ciscoSwitchCefCapability.setOrganization('Cisco Systems, Inc.')
ciscoSwitchCefCapV15R0101SYPCat6kPfc3 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 614, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchCefCapV15R0101SYPCat6kPfc3 = ciscoSwitchCefCapV15R0101SYPCat6kPfc3.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices with PFC3 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchCefCapV15R0101SYPCat6kPfc3 = ciscoSwitchCefCapV15R0101SYPCat6kPfc3.setStatus('current')
ciscoSwitchCefCapV15R0101SYPCat6kPfc4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 614, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchCefCapV15R0101SYPCat6kPfc4 = ciscoSwitchCefCapV15R0101SYPCat6kPfc4.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices with PFC4 card.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSwitchCefCapV15R0101SYPCat6kPfc4 = ciscoSwitchCefCapV15R0101SYPCat6kPfc4.setStatus('current')
mibBuilder.exportSymbols("CISCO-SWITCH-CEF-CAPABILITY", ciscoSwitchCefCapV15R0101SYPCat6kPfc3=ciscoSwitchCefCapV15R0101SYPCat6kPfc3, PYSNMP_MODULE_ID=ciscoSwitchCefCapability, ciscoSwitchCefCapability=ciscoSwitchCefCapability, ciscoSwitchCefCapV15R0101SYPCat6kPfc4=ciscoSwitchCefCapV15R0101SYPCat6kPfc4)
