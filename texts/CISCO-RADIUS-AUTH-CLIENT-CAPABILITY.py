#
# PySNMP MIB module CISCO-RADIUS-AUTH-CLIENT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-RADIUS-AUTH-CLIENT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:46 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoRadiusAuthClientCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 494))
ciscoRadiusAuthClientCapability.setRevisions(('2006-03-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoRadiusAuthClientCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoRadiusAuthClientCapability.setLastUpdated('200603060000Z')
if mibBuilder.loadTexts: ciscoRadiusAuthClientCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoRadiusAuthClientCapability.setContactInfo('       Cisco Systems\n                Customer Service\n\n               Postal: 170 West Tasman Drive\n               San Jose, CA  95134\n               USA\n\n               Tel: +1 800 553-NETS\n\n               E-mail: cs-radius@cisco.com')
if mibBuilder.loadTexts: ciscoRadiusAuthClientCapability.setDescription('The capabilities description of RADIUS-AUTH-CLIENT-MIB')
ciscoRadiusAuthClientCapV330CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 494, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRadiusAuthClientCapV330CRS1 = ciscoRadiusAuthClientCapV330CRS1.setProductRelease('Cisco IOS XR release 3.3.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRadiusAuthClientCapV330CRS1 = ciscoRadiusAuthClientCapV330CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoRadiusAuthClientCapV330CRS1.setDescription('RADIUS-AUTH-CLIENT-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-RADIUS-AUTH-CLIENT-CAPABILITY", ciscoRadiusAuthClientCapability=ciscoRadiusAuthClientCapability, PYSNMP_MODULE_ID=ciscoRadiusAuthClientCapability, ciscoRadiusAuthClientCapV330CRS1=ciscoRadiusAuthClientCapV330CRS1)
