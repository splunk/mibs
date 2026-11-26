#
# PySNMP MIB module CISCO-MLD-SNOOPING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-MLD-SNOOPING-CAPABILITY
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
ciscoMldSnoopingCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 586))
ciscoMldSnoopingCapability.setRevisions(('2010-03-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMldSnoopingCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoMldSnoopingCapability.setLastUpdated('201003020000Z')
if mibBuilder.loadTexts: ciscoMldSnoopingCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMldSnoopingCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n\n            Postal: 170 W Tasman Drive\n\n            San Jose, CA  95134\n\n            USA\n\n\n            Tel: +1 800 553-NETS\n\n\n            E-mail: cs-<list>@cisco.com')
if mibBuilder.loadTexts: ciscoMldSnoopingCapability.setDescription('The capabilities description of CISCO-MLD-SNOOPING-MIB.')
ciscoMldSnoopingCapabilityV04R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 586, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMldSnoopingCapabilityV04R01 = ciscoMldSnoopingCapabilityV04R01.setProductRelease('Cisco IOS-XR')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMldSnoopingCapabilityV04R01 = ciscoMldSnoopingCapabilityV04R01.setStatus('current')
if mibBuilder.loadTexts: ciscoMldSnoopingCapabilityV04R01.setDescription('Capabilities description for CISCO-MLD-SNOOPING-MIB.')
mibBuilder.exportSymbols("CISCO-MLD-SNOOPING-CAPABILITY", ciscoMldSnoopingCapabilityV04R01=ciscoMldSnoopingCapabilityV04R01, ciscoMldSnoopingCapability=ciscoMldSnoopingCapability, PYSNMP_MODULE_ID=ciscoMldSnoopingCapability)
