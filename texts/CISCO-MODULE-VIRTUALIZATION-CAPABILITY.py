#
# PySNMP MIB module CISCO-MODULE-VIRTUALIZATION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-MODULE-VIRTUALIZATION-CAPABILITY
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
ciscoModuleVirtualizationCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 497))
ciscoModuleVirtualizationCapability.setRevisions(('2008-06-14 00:00', '2006-05-31 00:00', '2006-03-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoModuleVirtualizationCapability.setRevisionsDescriptions(('Added capability statement\n        ciscoModVirtCapc4710aceVA1R700 for \n        ACE 4710 Application Control Engine \n        Appliance.', 'Corrected the contact E-mail id:\n        cs-l4l7security@cisco.com', 'Added capability statement\n        ciscoModuleVirtualizationCapabilityACSWV03R000 \n        for Application Control Engine (ACE).',))
if mibBuilder.loadTexts: ciscoModuleVirtualizationCapability.setLastUpdated('200806140000Z')
if mibBuilder.loadTexts: ciscoModuleVirtualizationCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoModuleVirtualizationCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-l4l7security@cisco.com,\n            cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoModuleVirtualizationCapability.setDescription('The capabilities description of\n        CISCO-MODULE-VIRTUALIZATION-MIB.')
ciscoModuleVirtualizationCapabilityACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 497, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoModuleVirtualizationCapabilityACSWV03R000 = ciscoModuleVirtualizationCapabilityACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoModuleVirtualizationCapabilityACSWV03R000 = ciscoModuleVirtualizationCapabilityACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: ciscoModuleVirtualizationCapabilityACSWV03R000.setDescription('CISCO-MODULE-VIRTUALIZATION-MIB capabilities.')
ciscoModVirtCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 497, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoModVirtCapc4710aceVA1R700 = ciscoModVirtCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                 for ACE 4710 Application Control Engine \n                 Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoModVirtCapc4710aceVA1R700 = ciscoModVirtCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: ciscoModVirtCapc4710aceVA1R700.setDescription('CISCO-MODULE-VIRTUALIZATION-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-MODULE-VIRTUALIZATION-CAPABILITY", ciscoModuleVirtualizationCapability=ciscoModuleVirtualizationCapability, PYSNMP_MODULE_ID=ciscoModuleVirtualizationCapability, ciscoModVirtCapc4710aceVA1R700=ciscoModVirtCapc4710aceVA1R700, ciscoModuleVirtualizationCapabilityACSWV03R000=ciscoModuleVirtualizationCapabilityACSWV03R000)
