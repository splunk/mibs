#
# PySNMP MIB module CISCO-POLICY-GROUP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-POLICY-GROUP-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoPolicyGroupCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 512))
ciscoPolicyGroupCapability.setRevisions(('2006-06-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoPolicyGroupCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoPolicyGroupCapability.setLastUpdated('200606260000Z')
if mibBuilder.loadTexts: ciscoPolicyGroupCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoPolicyGroupCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 West Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoPolicyGroupCapability.setDescription('The capabilities description of\n                 CISCO-POLICY-GROUP-MIB.')
ciscoPolicyGroupCapV08R0601 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 512, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPolicyGroupCapV08R0601 = ciscoPolicyGroupCapV08R0601.setProductRelease('Cisco CatOS 8.6(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoPolicyGroupCapV08R0601 = ciscoPolicyGroupCapV08R0601.setStatus('current')
if mibBuilder.loadTexts: ciscoPolicyGroupCapV08R0601.setDescription('CISCO-POLICY-GROUP-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-POLICY-GROUP-CAPABILITY", ciscoPolicyGroupCapability=ciscoPolicyGroupCapability, ciscoPolicyGroupCapV08R0601=ciscoPolicyGroupCapV08R0601, PYSNMP_MODULE_ID=ciscoPolicyGroupCapability)
