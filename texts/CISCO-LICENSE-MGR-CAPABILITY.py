#
# PySNMP MIB module CISCO-LICENSE-MGR-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-LICENSE-MGR-CAPABILITY
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
ciscoLicenseMgrCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 495))
ciscoLicenseMgrCapability.setRevisions(('2008-07-21 00:00', '2006-03-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLicenseMgrCapability.setRevisionsDescriptions(('Added VARIATIONS for MIB objects clmLicenseGracePeriod and\n        clmNotificationsEnable to ciscoLicenseMgrCapabilityACSWV03R000\n        agent capability.\n\n        Added capability statement ciscoLicMgrCapc4710aceVA1R700 for\n        ACE 4710 Application Control Engine Appliance.', 'Added capability statement\n        ciscoLicenseMgrCapabilityACSWV03R000 for \n        Application Control Engine (ACE).',))
if mibBuilder.loadTexts: ciscoLicenseMgrCapability.setLastUpdated('200807210000Z')
if mibBuilder.loadTexts: ciscoLicenseMgrCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoLicenseMgrCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoLicenseMgrCapability.setDescription('The capabilities description of\n        CISCO-LICENSE-MGR-MIB.')
ciscoLicenseMgrCapabilityACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 495, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLicenseMgrCapabilityACSWV03R000 = ciscoLicenseMgrCapabilityACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLicenseMgrCapabilityACSWV03R000 = ciscoLicenseMgrCapabilityACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoLicenseMgrCapabilityACSWV03R000.setDescription('ACSW (Application Control Software) 3.0 CISCO\n        LICENSE MGR MIB capabilities')
ciscoLicMgrCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 495, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLicMgrCapc4710aceVA1R700 = ciscoLicMgrCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                 for ACE 4710 Application Control Engine \n                 Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLicMgrCapc4710aceVA1R700 = ciscoLicMgrCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: ciscoLicMgrCapc4710aceVA1R700.setDescription('ACSW (Application Control Software) A1(7) CISCO\n        LICENSE MGR MIB capabilities')
mibBuilder.exportSymbols("CISCO-LICENSE-MGR-CAPABILITY", ciscoLicenseMgrCapability=ciscoLicenseMgrCapability, ciscoLicenseMgrCapabilityACSWV03R000=ciscoLicenseMgrCapabilityACSWV03R000, ciscoLicMgrCapc4710aceVA1R700=ciscoLicMgrCapc4710aceVA1R700, PYSNMP_MODULE_ID=ciscoLicenseMgrCapability)
