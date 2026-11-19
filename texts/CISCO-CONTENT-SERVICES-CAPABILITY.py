#
# PySNMP MIB module CISCO-CONTENT-SERVICES-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-CONTENT-SERVICES-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:13 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoContentServicesCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 581))
ciscoContentServicesCapability.setRevisions(('2010-12-23 00:00', '2010-02-11 00:00', '2009-08-21 00:00', '2009-05-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoContentServicesCapability.setRevisionsDescriptions(('Added following object groups:\n        ciscoContentServicesLoadStatRadiusGroupSup1\n        ciscoContentServicesLoadStatUserDBGroupSup1\n        ciscoContentServicesLoadStatSessionGroupSup1\n        ciscoContentServicesLoadStatBMAGroupSup1\n        ciscoContentServicesLoadStatQuotaMgrGroupSup1\n        ciscoContentServicesLoadStatGxEventGroupSup1', 'Added following object group:\n        ciscoContentServicesBillingPlanStatsGroup', 'Added following object groups:\n        ciscoContentServiceProtocolStatsGroup\n        ciscoContentServicesLoadStatGxEventGroup', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoContentServicesCapability.setLastUpdated('201012230000Z')
if mibBuilder.loadTexts: ciscoContentServicesCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoContentServicesCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-csg@cisco.com')
if mibBuilder.loadTexts: ciscoContentServicesCapability.setDescription('Agent capabilities for CISCO-CONTENT-SERVICES-MIB')
ciscoContentServicesCapabilityAdcV01R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 581, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityAdcV01R00 = ciscoContentServicesCapabilityAdcV01R00.setProductRelease('Cisco IOS 12.4MF')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityAdcV01R00 = ciscoContentServicesCapabilityAdcV01R00.setStatus('current')
if mibBuilder.loadTexts: ciscoContentServicesCapabilityAdcV01R00.setDescription('Cisco Content Services MIB for AdControl capabilities')
ciscoContentServicesCapabilityCSG2R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 581, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R03 = ciscoContentServicesCapabilityCSG2R03.setProductRelease('Cisco IOS 12.4(22)MD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R03 = ciscoContentServicesCapabilityCSG2R03.setStatus('current')
if mibBuilder.loadTexts: ciscoContentServicesCapabilityCSG2R03.setDescription('Cisco Content Services MIB for CSG2 R3 capabilities')
ciscoContentServicesCapabilityCSG2R0305 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 581, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R0305 = ciscoContentServicesCapabilityCSG2R0305.setProductRelease('Cisco IOS 12.4(22)MDA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R0305 = ciscoContentServicesCapabilityCSG2R0305.setStatus('current')
if mibBuilder.loadTexts: ciscoContentServicesCapabilityCSG2R0305.setDescription('Added ciscoContentServicesCapabilityCSG2R0305 agent capabilities \n        for Content Service Gateway version 3.5. This verion contains \n        the statistics for Layer 7 protocols including Nbar protocol. \n        Also added load statistical information related to Gx Events.')
ciscoContentServicesCapabilityCSG2R04 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 581, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R04 = ciscoContentServicesCapabilityCSG2R04.setProductRelease('Cisco IOS 12.4(24)MD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R04 = ciscoContentServicesCapabilityCSG2R04.setStatus('current')
if mibBuilder.loadTexts: ciscoContentServicesCapabilityCSG2R04.setDescription('Added ciscoContentServicesCapabilityCSG2R04 agent capabilities\n        for Content Service Gateway 2 release 4. In addition to existing \n        features, the release also provides the statistics of associated\n        subscribers per billing plan.')
ciscoContentServicesCapabilityCSG2R06 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 581, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R06 = ciscoContentServicesCapabilityCSG2R06.setProductRelease('Cisco IOS R6')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R06 = ciscoContentServicesCapabilityCSG2R06.setStatus('current')
if mibBuilder.loadTexts: ciscoContentServicesCapabilityCSG2R06.setDescription('Added ciscoContentServicesCapabilityCSG2R06 agent capabilities\n        for Content Service Gateway 2 release 6. In addition to existing \n        features, the release also provides 64 bit version of allowed\n        and denial rate for load statistics.')
mibBuilder.exportSymbols("CISCO-CONTENT-SERVICES-CAPABILITY", ciscoContentServicesCapability=ciscoContentServicesCapability, ciscoContentServicesCapabilityCSG2R04=ciscoContentServicesCapabilityCSG2R04, ciscoContentServicesCapabilityCSG2R03=ciscoContentServicesCapabilityCSG2R03, ciscoContentServicesCapabilityCSG2R0305=ciscoContentServicesCapabilityCSG2R0305, ciscoContentServicesCapabilityAdcV01R00=ciscoContentServicesCapabilityAdcV01R00, PYSNMP_MODULE_ID=ciscoContentServicesCapability, ciscoContentServicesCapabilityCSG2R06=ciscoContentServicesCapabilityCSG2R06)
