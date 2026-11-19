#
# PySNMP MIB module CISCO-VISM-SESSION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VISM-SESSION-CAPABILITY
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
ciscoVismSessionCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 415))
ciscoVismSessionCapability.setRevisions(('2005-09-19 00:00', '2004-09-03 00:00',))
if mibBuilder.loadTexts: ciscoVismSessionCapability.setLastUpdated('200509190000Z')
if mibBuilder.loadTexts: ciscoVismSessionCapability.setOrganization('Cisco Systems, Inc.')
ciscoVismSessionCapV5R015 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 415, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismSessionCapV5R015 = ciscoVismSessionCapV5R015.setProductRelease('MGX8850 Release 5.0.15')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismSessionCapV5R015 = ciscoVismSessionCapV5R015.setStatus('current')
ciscoVismSessionCapV3325 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 415, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismSessionCapV3325 = ciscoVismSessionCapV3325.setProductRelease('Cisco VISM Release 3.3.25')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismSessionCapV3325 = ciscoVismSessionCapV3325.setStatus('current')
mibBuilder.exportSymbols("CISCO-VISM-SESSION-CAPABILITY", ciscoVismSessionCapV3325=ciscoVismSessionCapV3325, PYSNMP_MODULE_ID=ciscoVismSessionCapability, ciscoVismSessionCapV5R015=ciscoVismSessionCapV5R015, ciscoVismSessionCapability=ciscoVismSessionCapability)
