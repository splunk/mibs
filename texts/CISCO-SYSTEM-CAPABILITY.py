#
# PySNMP MIB module CISCO-SYSTEM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SYSTEM-CAPABILITY
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
ciscoSystemCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 276))
ciscoSystemCapability.setRevisions(('2008-07-02 00:00', '2007-07-31 00:00', '2003-09-15 00:00', '2002-03-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSystemCapability.setRevisionsDescriptions(('Added ciscoSystemCapACSWV03R000 agent capabilities for\n        Application Control Engine (ACE) Module.\n\n        Added ciscoSystemCapc4710aceVA1R700 agent capabilities for \n        ACE 4710 Application Control Engine Appliance.', 'Added ciscoSystemCapabilityMGXV5R0500.', 'Added ciscoSystemCapCatOSV08R0101.', 'Initial version of the MIB module.',))
if mibBuilder.loadTexts: ciscoSystemCapability.setLastUpdated('200807020000Z')
if mibBuilder.loadTexts: ciscoSystemCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSystemCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-snmp@cisco.com,\n            cs-lan-switch-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoSystemCapability.setDescription('The Agent Capabilities for CISCO-SYSTEM-MIB.')
ciscoSystemCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 276, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapabilityV2R00 = ciscoSystemCapabilityV2R00.setProductRelease('MGX8850 Release 2.00,\n                         BPX SES Release 1.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapabilityV2R00 = ciscoSystemCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: ciscoSystemCapabilityV2R00.setDescription('CISCO-SYSTEM-MIB capabilities.')
ciscoSystemCapCatOSV08R0101 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 276, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapCatOSV08R0101 = ciscoSystemCapCatOSV08R0101.setProductRelease('Cisco CatOS 8.1(1).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapCatOSV08R0101 = ciscoSystemCapCatOSV08R0101.setStatus('current')
if mibBuilder.loadTexts: ciscoSystemCapCatOSV08R0101.setDescription('CISCO-SYSTEM-MIB capabilities.')
ciscoSystemCapabilityMGXV5R0500 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 276, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapabilityMGXV5R0500 = ciscoSystemCapabilityMGXV5R0500.setProductRelease('MGX8850 5.5 Release')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapabilityMGXV5R0500 = ciscoSystemCapabilityMGXV5R0500.setStatus('current')
if mibBuilder.loadTexts: ciscoSystemCapabilityMGXV5R0500.setDescription('CISCO-SYSTEM-MIB capabilities.')
ciscoSystemCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 276, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapACSWV03R000 = ciscoSystemCapACSWV03R000.setProductRelease('ACSW (Application Control Software)\n                    version 3.0(0)A1(2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapACSWV03R000 = ciscoSystemCapACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoSystemCapACSWV03R000.setDescription('CISCO-SYSTEM-MIB capabilities.')
ciscoSystemCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 276, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapc4710aceVA1R700 = ciscoSystemCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSystemCapc4710aceVA1R700 = ciscoSystemCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: ciscoSystemCapc4710aceVA1R700.setDescription('CISCO-SYSTEM-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-SYSTEM-CAPABILITY", ciscoSystemCapCatOSV08R0101=ciscoSystemCapCatOSV08R0101, PYSNMP_MODULE_ID=ciscoSystemCapability, ciscoSystemCapabilityMGXV5R0500=ciscoSystemCapabilityMGXV5R0500, ciscoSystemCapability=ciscoSystemCapability, ciscoSystemCapc4710aceVA1R700=ciscoSystemCapc4710aceVA1R700, ciscoSystemCapACSWV03R000=ciscoSystemCapACSWV03R000, ciscoSystemCapabilityV2R00=ciscoSystemCapabilityV2R00)
