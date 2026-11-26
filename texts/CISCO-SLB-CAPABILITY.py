#
# PySNMP MIB module CISCO-SLB-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SLB-CAPABILITY
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
ciscoSlbCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 181))
ciscoSlbCapability.setRevisions(('2008-07-24 00:00', '2008-02-07 00:00', '2006-12-09 00:00', '2006-03-21 00:00', '2001-03-09 00:00', '2000-10-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSlbCapability.setRevisionsDescriptions(('Added ciscoSlbCapc4710aceVA3R100 agent\n        capabilities for ACE 4710 Application Control \n        Engine Appliance.', 'Added ciscoSlbCapc4710aceVA1R700 agent\n        capabilities for ACE 4710 Application Control \n        Engine Appliance.', '- Added ciscoSlbCapabilityACSWV300RA12 agent\n        capabilities for Application Control Engine (ACE).\n\n        - Following change is done for ciscoSlbCapabilityV12R01:\n         * STATUS changed to obsolete.\n         * Commented out the VARIATION and\n          other clauses for non-existent objects.\n\n        - Added ciscoSlbCapabilityNewV12R01 which is same\n        as ciscoSlbCapabilityV12R01 except it is not \n        referencing the non-existent objects/groups.', 'Added ciscoIfCapabilityACSWV03R000 agent\n        capabilities for Application Control Engine (ACE).', 'Extended MIB support for ciscoSlbEntriesGroup,\n        and serveral new objects in the\n        ciscoSlbVirtualServersGroup.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoSlbCapability.setLastUpdated('200807240000Z')
if mibBuilder.loadTexts: ciscoSlbCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSlbCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-slb@cisco.com')
if mibBuilder.loadTexts: ciscoSlbCapability.setDescription('Agent capabilities for the SLB-MIB')
ciscoSlbCapabilityV12R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 181, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbCapabilityV12R01 = ciscoSlbCapabilityV12R01.setProductRelease('Cisco IOS 12.0(10)W05(17.29) and 12.1(01.06)E01')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbCapabilityV12R01 = ciscoSlbCapabilityV12R01.setStatus('obsolete')
if mibBuilder.loadTexts: ciscoSlbCapabilityV12R01.setDescription('IOS 12.1 Cisco SLB MIB capabilities')
ciscoIfCapabilityACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 181, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityACSWV03R000 = ciscoIfCapabilityACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIfCapabilityACSWV03R000 = ciscoIfCapabilityACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoIfCapabilityACSWV03R000.setDescription('ACSW (Application Control Software) 3.0\n        CISCO SLB MIB capabilities')
ciscoSlbExtCapabilityACSWV300RA12 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 181, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbExtCapabilityACSWV300RA12 = ciscoSlbExtCapabilityACSWV300RA12.setProductRelease('ACSW (Application Control Software)\n                version 3.0(0)A1(2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbExtCapabilityACSWV300RA12 = ciscoSlbExtCapabilityACSWV300RA12.setStatus('current')
if mibBuilder.loadTexts: ciscoSlbExtCapabilityACSWV300RA12.setDescription('ACSW (Application Control Software) 3.0\n        CISCO SLB MIB capabilities')
ciscoSlbCapabilityNewV12R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 181, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbCapabilityNewV12R01 = ciscoSlbCapabilityNewV12R01.setProductRelease('Cisco IOS 12.0(10)W05(17.29) and 12.1(01.06)E01')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbCapabilityNewV12R01 = ciscoSlbCapabilityNewV12R01.setStatus('current')
if mibBuilder.loadTexts: ciscoSlbCapabilityNewV12R01.setDescription('IOS 12.1 Cisco SLB MIB capabilities')
ciscoSlbCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 181, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbCapc4710aceVA1R700 = ciscoSlbCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbCapc4710aceVA1R700 = ciscoSlbCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: ciscoSlbCapc4710aceVA1R700.setDescription('ACSW (Application Control Software) A1(7)\n        CISCO SLB MIB capabilities.')
ciscoSlbCapc4710aceVA3R100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 181, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbCapc4710aceVA3R100 = ciscoSlbCapc4710aceVA3R100.setProductRelease('ACSW (Application Control Software) A3(1) for\n                     ACE 4710 Application Control Engine Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbCapc4710aceVA3R100 = ciscoSlbCapc4710aceVA3R100.setStatus('current')
if mibBuilder.loadTexts: ciscoSlbCapc4710aceVA3R100.setDescription('ACSW (Application Control Software) A3(1)\n        CISCO SLB MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SLB-CAPABILITY", ciscoSlbCapabilityNewV12R01=ciscoSlbCapabilityNewV12R01, ciscoSlbCapc4710aceVA3R100=ciscoSlbCapc4710aceVA3R100, ciscoSlbExtCapabilityACSWV300RA12=ciscoSlbExtCapabilityACSWV300RA12, ciscoSlbCapc4710aceVA1R700=ciscoSlbCapc4710aceVA1R700, ciscoSlbCapability=ciscoSlbCapability, ciscoIfCapabilityACSWV03R000=ciscoIfCapabilityACSWV03R000, ciscoSlbCapabilityV12R01=ciscoSlbCapabilityV12R01, PYSNMP_MODULE_ID=ciscoSlbCapability)
