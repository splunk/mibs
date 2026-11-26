#
# PySNMP MIB module CISCO-AAA-SERVER-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-AAA-SERVER-CAPABILITY
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
ciscoAAAServerCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 129))
ciscoAAAServerCapability.setRevisions(('2008-07-21 00:00', '2006-02-21 00:00', '2003-11-14 00:00', '2000-01-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAAAServerCapability.setRevisionsDescriptions(('Added VARIATION for casKey object in\n        ciscoAAAServerCapabilityACSWV03R000 agent capability.\n\n        Added Agent capabilities ciscoAAAServerCapc4710aceVA1R70 for\n        ACE 4710 Application Control Engine Appliance.', 'Agent capabilities for Application\n        Control Engine (ACE).', 'Agent capabilities for Cisco MDS 1.3.', 'Initial version of this MIB.',))
if mibBuilder.loadTexts: ciscoAAAServerCapability.setLastUpdated('200807210000Z')
if mibBuilder.loadTexts: ciscoAAAServerCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAAAServerCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-aaa@cisco.com')
if mibBuilder.loadTexts: ciscoAAAServerCapability.setDescription('Agent capabilities for CISCO-AAA-SERVER-MIB')
ciscoAAAServerCapabilityV10R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 129, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerCapabilityV10R00 = ciscoAAAServerCapabilityV10R00.setProductRelease('Cisco IOS 12.0(4)XJ')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerCapabilityV10R00 = ciscoAAAServerCapabilityV10R00.setStatus('current')
if mibBuilder.loadTexts: ciscoAAAServerCapabilityV10R00.setDescription('Cisco AAA Server MIB capabilities')
ciscoAAAServerCapabilityMDS13R1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 129, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerCapabilityMDS13R1 = ciscoAAAServerCapabilityMDS13R1.setProductRelease('Cisco MDS 1.3(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerCapabilityMDS13R1 = ciscoAAAServerCapabilityMDS13R1.setStatus('current')
if mibBuilder.loadTexts: ciscoAAAServerCapabilityMDS13R1.setDescription('Cisco AAA Server MIB capabilities')
ciscoAAAServerCapabilityACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 129, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerCapabilityACSWV03R000 = ciscoAAAServerCapabilityACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerCapabilityACSWV03R000 = ciscoAAAServerCapabilityACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoAAAServerCapabilityACSWV03R000.setDescription('Cisco AAA Server MIB capabilities\n        for ACSW 3.0')
ciscoAAAServerCapc4710aceVA1R70 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 129, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerCapc4710aceVA1R70 = ciscoAAAServerCapc4710aceVA1R70.setProductRelease('ACSW (Application Control Software) A1(7)\n                         for ACE 4710 Application Control Engine \n                         Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAAAServerCapc4710aceVA1R70 = ciscoAAAServerCapc4710aceVA1R70.setStatus('current')
if mibBuilder.loadTexts: ciscoAAAServerCapc4710aceVA1R70.setDescription('Cisco AAA Server MIB capabilities\n        for ACSW A1(7)')
mibBuilder.exportSymbols("CISCO-AAA-SERVER-CAPABILITY", ciscoAAAServerCapability=ciscoAAAServerCapability, PYSNMP_MODULE_ID=ciscoAAAServerCapability, ciscoAAAServerCapabilityMDS13R1=ciscoAAAServerCapabilityMDS13R1, ciscoAAAServerCapc4710aceVA1R70=ciscoAAAServerCapc4710aceVA1R70, ciscoAAAServerCapabilityACSWV03R000=ciscoAAAServerCapabilityACSWV03R000, ciscoAAAServerCapabilityV10R00=ciscoAAAServerCapabilityV10R00)
