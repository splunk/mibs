#
# PySNMP MIB module CISCO-MODULE-VIRTUALIZATION-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-MODULE-VIRTUALIZATION-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoModuleVirtualizationCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 497))
ciscoModuleVirtualizationCapability.setRevisions(('2008-06-14 00:00', '2006-05-31 00:00', '2006-03-21 00:00',))
if mibBuilder.loadTexts: ciscoModuleVirtualizationCapability.setLastUpdated('200806140000Z')
if mibBuilder.loadTexts: ciscoModuleVirtualizationCapability.setOrganization('Cisco Systems, Inc.')
ciscoModuleVirtualizationCapabilityACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 497, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoModuleVirtualizationCapabilityACSWV03R000 = ciscoModuleVirtualizationCapabilityACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoModuleVirtualizationCapabilityACSWV03R000 = ciscoModuleVirtualizationCapabilityACSWV03R000.setStatus('current')
ciscoModVirtCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 497, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoModVirtCapc4710aceVA1R700 = ciscoModVirtCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                 for ACE 4710 Application Control Engine \n                 Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoModVirtCapc4710aceVA1R700 = ciscoModVirtCapc4710aceVA1R700.setStatus('current')
mibBuilder.exportSymbols("CISCO-MODULE-VIRTUALIZATION-CAPABILITY", PYSNMP_MODULE_ID=ciscoModuleVirtualizationCapability, ciscoModuleVirtualizationCapabilityACSWV03R000=ciscoModuleVirtualizationCapabilityACSWV03R000, ciscoModVirtCapc4710aceVA1R700=ciscoModVirtCapc4710aceVA1R700, ciscoModuleVirtualizationCapability=ciscoModuleVirtualizationCapability)
