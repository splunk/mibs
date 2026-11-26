#
# PySNMP MIB module CISCO-IETF-NAT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IETF-NAT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
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
ciscoIetfNatCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 99999))
ciscoIetfNatCapability.setRevisions(('2001-09-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIetfNatCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIetfNatCapability.setLastUpdated('200109100000Z')
if mibBuilder.loadTexts: ciscoIetfNatCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIetfNatCapability.setContactInfo('          Cisco Systems\n                               Customer Service\n\n                    Postal:    170 West Tasman Drive\n                               San Jose, CA  95134\n                               USA\n\n                       Tel:    +1 800 553-NETS\n\n                    E-mail:    cs-nat@cisco.com')
if mibBuilder.loadTexts: ciscoIetfNatCapability.setDescription('Agent capabilities for NAT-MIB')
ciscoIetfNatCapabilityV12R02T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 99999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfNatCapabilityV12R02T = ciscoIetfNatCapabilityV12R02T.setProductRelease('Cisco IOS 12.2T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIetfNatCapabilityV12R02T = ciscoIetfNatCapabilityV12R02T.setStatus('current')
if mibBuilder.loadTexts: ciscoIetfNatCapabilityV12R02T.setDescription('NAT MIB capabilities')
mibBuilder.exportSymbols("CISCO-IETF-NAT-CAPABILITY", PYSNMP_MODULE_ID=ciscoIetfNatCapability, ciscoIetfNatCapabilityV12R02T=ciscoIetfNatCapabilityV12R02T, ciscoIetfNatCapability=ciscoIetfNatCapability)
