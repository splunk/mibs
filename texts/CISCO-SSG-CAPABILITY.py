#
# PySNMP MIB module CISCO-SSG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SSG-CAPABILITY
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
ciscoSsgCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 1500))
ciscoSsgCapability.setRevisions(('2004-08-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSsgCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSsgCapability.setLastUpdated('200408130000Z')
if mibBuilder.loadTexts: ciscoSsgCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSsgCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                   Tel: +1 800 553-NETS\n\n                E-mail: cs-ssg@cisco.com')
if mibBuilder.loadTexts: ciscoSsgCapability.setDescription('This is the Agent Capability MIB for\n                 CISCO-SSG-MIB.')
ciscoSsgCapabilityV12R03RevT = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 1500, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSsgCapabilityV12R03RevT = ciscoSsgCapabilityV12R03RevT.setProductRelease('Cisco IOS 12.3T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSsgCapabilityV12R03RevT = ciscoSsgCapabilityV12R03RevT.setStatus('current')
if mibBuilder.loadTexts: ciscoSsgCapabilityV12R03RevT.setDescription('CISCO-SSG-MIB capabilities')
mibBuilder.exportSymbols("CISCO-SSG-CAPABILITY", ciscoSsgCapabilityV12R03RevT=ciscoSsgCapabilityV12R03RevT, ciscoSsgCapability=ciscoSsgCapability, PYSNMP_MODULE_ID=ciscoSsgCapability)
