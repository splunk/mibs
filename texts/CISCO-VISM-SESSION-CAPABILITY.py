#
# PySNMP MIB module CISCO-VISM-SESSION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VISM-SESSION-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:06 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVismSessionCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 415))
ciscoVismSessionCapability.setRevisions(('2005-09-19 00:00', '2004-09-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVismSessionCapability.setRevisionsDescriptions(('Added capabilities for VISM Release 3.3.25.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVismSessionCapability.setLastUpdated('200509190000Z')
if mibBuilder.loadTexts: ciscoVismSessionCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVismSessionCapability.setContactInfo('        Cisco Systems\n                 Customer Service\n        Postal: 170 W Tasman Drive\n                San Jose, CA 95134\n                USA\n           Tel: +1 800 553-NETS\n        E-mail: cs-voice-gateway@cisco.com')
if mibBuilder.loadTexts: ciscoVismSessionCapability.setDescription('This MIB defines the agent capabilities for \n         CISCO-VISM-SESSION-MIB.')
ciscoVismSessionCapV5R015 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 415, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismSessionCapV5R015 = ciscoVismSessionCapV5R015.setProductRelease('MGX8850 Release 5.0.15')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismSessionCapV5R015 = ciscoVismSessionCapV5R015.setStatus('current')
if mibBuilder.loadTexts: ciscoVismSessionCapV5R015.setDescription('Agent capabilities for Voice Switch \n                     Service Module (VXSM) in MGX8850\n                     release 5.0.15.')
ciscoVismSessionCapV3325 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 415, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismSessionCapV3325 = ciscoVismSessionCapV3325.setProductRelease('Cisco VISM Release 3.3.25')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVismSessionCapV3325 = ciscoVismSessionCapV3325.setStatus('current')
if mibBuilder.loadTexts: ciscoVismSessionCapV3325.setDescription('CISCO-VISM-SESSION-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-VISM-SESSION-CAPABILITY", ciscoVismSessionCapV5R015=ciscoVismSessionCapV5R015, ciscoVismSessionCapability=ciscoVismSessionCapability, ciscoVismSessionCapV3325=ciscoVismSessionCapV3325, PYSNMP_MODULE_ID=ciscoVismSessionCapability)
