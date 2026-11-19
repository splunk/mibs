#
# PySNMP MIB module CISCO-AAA-CLIENT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-AAA-CLIENT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:07 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoAaaClientCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 322))
ciscoAaaClientCapability.setRevisions(('2004-02-03 00:00', '2003-08-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAaaClientCapability.setRevisionsDescriptions(('Added VARIATION for cacEnable and cacPrimaryMethod.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoAaaClientCapability.setLastUpdated('200402030000Z')
if mibBuilder.loadTexts: ciscoAaaClientCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAaaClientCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoAaaClientCapability.setDescription('The capabilities description of CISCO-AAA-CLIENT-MIB.')
ciscoAaaClientCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 322, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAaaClientCapCatOSV08R0101 = ciscoAaaClientCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1) on Catalyst 6000/6500\n                         and Cisco 7600 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAaaClientCapCatOSV08R0101 = ciscoAaaClientCapCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: ciscoAaaClientCapCatOSV08R0101.setDescription('CISCO-AAA-CLIENT-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-AAA-CLIENT-CAPABILITY", ciscoAaaClientCapCatOSV08R0101=ciscoAaaClientCapCatOSV08R0101, ciscoAaaClientCapability=ciscoAaaClientCapability, PYSNMP_MODULE_ID=ciscoAaaClientCapability)
