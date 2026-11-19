#
# PySNMP MIB module CISCO-CONTENT-SERVICES-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-CONTENT-SERVICES-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoContentServicesCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 581))
ciscoContentServicesCapability.setRevisions(('2010-12-23 00:00', '2010-02-11 00:00', '2009-08-21 00:00', '2009-05-09 00:00',))
if mibBuilder.loadTexts: ciscoContentServicesCapability.setLastUpdated('201012230000Z')
if mibBuilder.loadTexts: ciscoContentServicesCapability.setOrganization('Cisco Systems, Inc.')
ciscoContentServicesCapabilityAdcV01R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 581, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityAdcV01R00 = ciscoContentServicesCapabilityAdcV01R00.setProductRelease('Cisco IOS 12.4MF')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityAdcV01R00 = ciscoContentServicesCapabilityAdcV01R00.setStatus('current')
ciscoContentServicesCapabilityCSG2R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 581, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R03 = ciscoContentServicesCapabilityCSG2R03.setProductRelease('Cisco IOS 12.4(22)MD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R03 = ciscoContentServicesCapabilityCSG2R03.setStatus('current')
ciscoContentServicesCapabilityCSG2R0305 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 581, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R0305 = ciscoContentServicesCapabilityCSG2R0305.setProductRelease('Cisco IOS 12.4(22)MDA')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R0305 = ciscoContentServicesCapabilityCSG2R0305.setStatus('current')
ciscoContentServicesCapabilityCSG2R04 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 581, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R04 = ciscoContentServicesCapabilityCSG2R04.setProductRelease('Cisco IOS 12.4(24)MD')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R04 = ciscoContentServicesCapabilityCSG2R04.setStatus('current')
ciscoContentServicesCapabilityCSG2R06 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 581, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R06 = ciscoContentServicesCapabilityCSG2R06.setProductRelease('Cisco IOS R6')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContentServicesCapabilityCSG2R06 = ciscoContentServicesCapabilityCSG2R06.setStatus('current')
mibBuilder.exportSymbols("CISCO-CONTENT-SERVICES-CAPABILITY", ciscoContentServicesCapability=ciscoContentServicesCapability, ciscoContentServicesCapabilityCSG2R0305=ciscoContentServicesCapabilityCSG2R0305, PYSNMP_MODULE_ID=ciscoContentServicesCapability, ciscoContentServicesCapabilityCSG2R04=ciscoContentServicesCapabilityCSG2R04, ciscoContentServicesCapabilityAdcV01R00=ciscoContentServicesCapabilityAdcV01R00, ciscoContentServicesCapabilityCSG2R06=ciscoContentServicesCapabilityCSG2R06, ciscoContentServicesCapabilityCSG2R03=ciscoContentServicesCapabilityCSG2R03)
