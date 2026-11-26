#
# PySNMP MIB module CISCO-IETF-PIM-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IETF-PIM-EXT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:45 2026
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
ciscoIetfPimExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 443))
ciscoIetfPimExtCapability.setRevisions(('2005-07-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIetfPimExtCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIetfPimExtCapability.setLastUpdated('200507270000Z')
if mibBuilder.loadTexts: ciscoIetfPimExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIetfPimExtCapability.setContactInfo('       Cisco Systems\n                Customer Service\n\n               Postal: 170 West Tasman Drive\n               San Jose, CA  95134\n               USA\n\n               Tel: +1 800 553-NETS\n\n               E-mail: cs-ipmulticast@cisco.com')
if mibBuilder.loadTexts: ciscoIetfPimExtCapability.setDescription('The capabilities description of CISCO-IETF-PIM-EXT-MIB')
cIetfPimExtCapV320CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 443, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIetfPimExtCapV320CRS1 = cIetfPimExtCapV320CRS1.setProductRelease('Cisco IOS XR 3.2.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIetfPimExtCapV320CRS1 = cIetfPimExtCapV320CRS1.setStatus('current')
if mibBuilder.loadTexts: cIetfPimExtCapV320CRS1.setDescription('CISCO-IETF-PIM-EXT-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-IETF-PIM-EXT-CAPABILITY", PYSNMP_MODULE_ID=ciscoIetfPimExtCapability, ciscoIetfPimExtCapability=ciscoIetfPimExtCapability, cIetfPimExtCapV320CRS1=cIetfPimExtCapV320CRS1)
