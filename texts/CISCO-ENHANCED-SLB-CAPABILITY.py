#
# PySNMP MIB module CISCO-ENHANCED-SLB-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ENHANCED-SLB-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:07 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEnhancedSlbCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 507))
ciscoEnhancedSlbCapability.setRevisions(('2008-07-07 00:00', '2008-02-08 00:00', '2006-05-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEnhancedSlbCapability.setRevisionsDescriptions(('Added capability statement\n        ciscoEnhancedSlbCapc4710aceVA3R10 for\n        ACE 4710 Application Control Engine Appliance.', 'Added capability statement\n        ciscoEnhancedSlbCapc4710aceVA1R70 for\n        ACE 4710 Application Control Engine Appliance.', 'Initial version of this MIB\n        Added capability statement \n        ciscoEnhancedSlbCapACSWV03R000 for \n        Application Control Engine (ACE).',))
if mibBuilder.loadTexts: ciscoEnhancedSlbCapability.setLastUpdated('200807070000Z')
if mibBuilder.loadTexts: ciscoEnhancedSlbCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEnhancedSlbCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-slb@cisco.com')
if mibBuilder.loadTexts: ciscoEnhancedSlbCapability.setDescription('The capabilities description of\n        CISCO-ENHANCED-SLB-MIB.')
ciscoEnhancedSlbCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 507, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnhancedSlbCapACSWV03R000 = ciscoEnhancedSlbCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnhancedSlbCapACSWV03R000 = ciscoEnhancedSlbCapACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoEnhancedSlbCapACSWV03R000.setDescription('ACSW (Application Control Software) 3.0\n        CISCO ENHANCED SLB MIB capabilities')
ciscoEnhancedSlbCapc4710aceVA1R70 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 507, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnhancedSlbCapc4710aceVA1R70 = ciscoEnhancedSlbCapc4710aceVA1R70.setProductRelease('ACSW (Application Control Software) A1(7)\n                    for ACE 4710 Application Control Engine \n                    Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnhancedSlbCapc4710aceVA1R70 = ciscoEnhancedSlbCapc4710aceVA1R70.setStatus('current')
if mibBuilder.loadTexts: ciscoEnhancedSlbCapc4710aceVA1R70.setDescription('ACSW (Application Control Software) A1(7)\n        CISCO ENHANCED SLB MIB capabilities')
ciscoEnhancedSlbCapc4710aceVA3R10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 507, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnhancedSlbCapc4710aceVA3R10 = ciscoEnhancedSlbCapc4710aceVA3R10.setProductRelease('ACSW (Application Control Software) A3(1.0)\n                    for ACE 4710 Application Control Engine \n                    Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEnhancedSlbCapc4710aceVA3R10 = ciscoEnhancedSlbCapc4710aceVA3R10.setStatus('current')
if mibBuilder.loadTexts: ciscoEnhancedSlbCapc4710aceVA3R10.setDescription('ACSW (Application Control Software) A3(1.0)\n        CISCO ENHANCED SLB MIB capabilities')
mibBuilder.exportSymbols("CISCO-ENHANCED-SLB-CAPABILITY", ciscoEnhancedSlbCapACSWV03R000=ciscoEnhancedSlbCapACSWV03R000, ciscoEnhancedSlbCapc4710aceVA3R10=ciscoEnhancedSlbCapc4710aceVA3R10, PYSNMP_MODULE_ID=ciscoEnhancedSlbCapability, ciscoEnhancedSlbCapability=ciscoEnhancedSlbCapability, ciscoEnhancedSlbCapc4710aceVA1R70=ciscoEnhancedSlbCapc4710aceVA1R70)
