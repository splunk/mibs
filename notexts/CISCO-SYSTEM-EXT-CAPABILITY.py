#
# PySNMP MIB module CISCO-SYSTEM-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SYSTEM-EXT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:24 2026
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
ciscoSysExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 569))
ciscoSysExtCapability.setRevisions(('2008-08-19 00:00', '2005-09-23 00:00',))
if mibBuilder.loadTexts: ciscoSysExtCapability.setLastUpdated('200808190000Z')
if mibBuilder.loadTexts: ciscoSysExtCapability.setOrganization('Cisco Systems, Inc.')
ciscoSysExtCapabilityMDS3R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 569, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysExtCapabilityMDS3R0 = ciscoSysExtCapabilityMDS3R0.setProductRelease('Cisco MDS 3.0(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysExtCapabilityMDS3R0 = ciscoSysExtCapabilityMDS3R0.setStatus('current')
ciscoSysExtCapabilityGssV02R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 569, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysExtCapabilityGssV02R00 = ciscoSysExtCapabilityGssV02R00.setProductRelease('Global Site Selector(GSS) 2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysExtCapabilityGssV02R00 = ciscoSysExtCapabilityGssV02R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-SYSTEM-EXT-CAPABILITY", ciscoSysExtCapability=ciscoSysExtCapability, ciscoSysExtCapabilityGssV02R00=ciscoSysExtCapabilityGssV02R00, PYSNMP_MODULE_ID=ciscoSysExtCapability, ciscoSysExtCapabilityMDS3R0=ciscoSysExtCapabilityMDS3R0)
