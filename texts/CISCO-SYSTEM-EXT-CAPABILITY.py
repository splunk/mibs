#
# PySNMP MIB module CISCO-SYSTEM-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SYSTEM-EXT-CAPABILITY
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
ciscoSysExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 569))
ciscoSysExtCapability.setRevisions(('2008-08-19 00:00', '2005-09-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSysExtCapability.setRevisionsDescriptions(('Added ciscoSysExtCapabilityGssV02R00 agent\n        capabilities for Global Site Selector(GSS)\n        release 2.0.', 'Initial version of this MIB.',))
if mibBuilder.loadTexts: ciscoSysExtCapability.setLastUpdated('200808190000Z')
if mibBuilder.loadTexts: ciscoSysExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSysExtCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoSysExtCapability.setDescription('Agent capabilities for CISCO-SYSTEM-EXT-MIB.')
ciscoSysExtCapabilityMDS3R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 569, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysExtCapabilityMDS3R0 = ciscoSysExtCapabilityMDS3R0.setProductRelease('Cisco MDS 3.0(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysExtCapabilityMDS3R0 = ciscoSysExtCapabilityMDS3R0.setStatus('current')
if mibBuilder.loadTexts: ciscoSysExtCapabilityMDS3R0.setDescription('Cisco System Extension MIB capabilities.')
ciscoSysExtCapabilityGssV02R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 569, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysExtCapabilityGssV02R00 = ciscoSysExtCapabilityGssV02R00.setProductRelease('Global Site Selector(GSS) 2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysExtCapabilityGssV02R00 = ciscoSysExtCapabilityGssV02R00.setStatus('current')
if mibBuilder.loadTexts: ciscoSysExtCapabilityGssV02R00.setDescription('GSS 2.0 CISCO-SYSTEM-EXT-MIB capabilities')
mibBuilder.exportSymbols("CISCO-SYSTEM-EXT-CAPABILITY", ciscoSysExtCapabilityGssV02R00=ciscoSysExtCapabilityGssV02R00, PYSNMP_MODULE_ID=ciscoSysExtCapability, ciscoSysExtCapabilityMDS3R0=ciscoSysExtCapabilityMDS3R0, ciscoSysExtCapability=ciscoSysExtCapability)
