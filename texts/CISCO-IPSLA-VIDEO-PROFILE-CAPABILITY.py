#
# PySNMP MIB module CISCO-IPSLA-VIDEO-PROFILE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IPSLA-VIDEO-PROFILE-CAPABILITY
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
ciscoIpslaVideoProfileCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 605))
ciscoIpslaVideoProfileCapability.setRevisions(('2011-06-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIpslaVideoProfileCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoIpslaVideoProfileCapability.setLastUpdated('201106010000Z')
if mibBuilder.loadTexts: ciscoIpslaVideoProfileCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIpslaVideoProfileCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-ipsla@cisco.com')
if mibBuilder.loadTexts: ciscoIpslaVideoProfileCapability.setDescription('Agent capabilities for CISCO-IPSLA-VIDEO-PROFILE-MIB')
ciscoIpslaVideoProfileCapabilityV152R02T = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 605, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpslaVideoProfileCapabilityV152R02T = ciscoIpslaVideoProfileCapabilityV152R02T.setProductRelease('OS=IOS\n                     OSVERSION=15.2(2)T\n                     PLATFORM=c29xx,c3925,c3945,c3925E,c3945E\n                     INTERFACE=None')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpslaVideoProfileCapabilityV152R02T = ciscoIpslaVideoProfileCapabilityV152R02T.setStatus('current')
if mibBuilder.loadTexts: ciscoIpslaVideoProfileCapabilityV152R02T.setDescription('Cisco IPSLA Video Profile MIB Capabilities in 15.2(2)T Release')
mibBuilder.exportSymbols("CISCO-IPSLA-VIDEO-PROFILE-CAPABILITY", ciscoIpslaVideoProfileCapability=ciscoIpslaVideoProfileCapability, PYSNMP_MODULE_ID=ciscoIpslaVideoProfileCapability, ciscoIpslaVideoProfileCapabilityV152R02T=ciscoIpslaVideoProfileCapabilityV152R02T)
