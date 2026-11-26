#
# PySNMP MIB module CISCO-VIDEO-SESSION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VIDEO-SESSION-CAPABILITY
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
ciscoVideoSessionCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 599))
ciscoVideoSessionCapability.setRevisions(('2011-05-24 00:00', '2010-11-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVideoSessionCapability.setRevisionsDescriptions(('Added ciscoVideoSessionCapabilityV152T02.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVideoSessionCapability.setLastUpdated('201105240000Z')
if mibBuilder.loadTexts: ciscoVideoSessionCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVideoSessionCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-video@cisco.com')
if mibBuilder.loadTexts: ciscoVideoSessionCapability.setDescription('Agent capabilities for CISCO-VIDEO-SESSION-MIB.')
ciscoVideoSessionCapabilityV15R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 599, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVideoSessionCapabilityV15R01 = ciscoVideoSessionCapabilityV15R01.setProductRelease('OS=IOS\n                     OSVERSION=15.1\n                     PLATFORM=c29xx,c3925,c3945,c3925E,c3945E\n                     INTERFACE=None')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVideoSessionCapabilityV15R01 = ciscoVideoSessionCapabilityV15R01.setStatus('current')
if mibBuilder.loadTexts: ciscoVideoSessionCapabilityV15R01.setDescription('Cisco Video Session MIB capabilities.')
ciscoVideoSessionCapabilityV152T02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 599, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVideoSessionCapabilityV152T02 = ciscoVideoSessionCapabilityV152T02.setProductRelease('OS=IOS\n                     OSVERSION=15.2(2)T\n                     PLATFORM=c29xx,c3925,c3945,c3925E,c3945E\n                     INTERFACE=None')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVideoSessionCapabilityV152T02 = ciscoVideoSessionCapabilityV152T02.setStatus('current')
if mibBuilder.loadTexts: ciscoVideoSessionCapabilityV152T02.setDescription('Cisco Video Session MIB capabilities.\n        Some objects are not implemented due to DSP statistics reporting\n        capabilities.')
mibBuilder.exportSymbols("CISCO-VIDEO-SESSION-CAPABILITY", ciscoVideoSessionCapability=ciscoVideoSessionCapability, ciscoVideoSessionCapabilityV152T02=ciscoVideoSessionCapabilityV152T02, PYSNMP_MODULE_ID=ciscoVideoSessionCapability, ciscoVideoSessionCapabilityV15R01=ciscoVideoSessionCapabilityV15R01)
