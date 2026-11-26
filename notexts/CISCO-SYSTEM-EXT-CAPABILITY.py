#
# PySNMP MIB module CISCO-SYSTEM-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SYSTEM-EXT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
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
mibBuilder.exportSymbols("CISCO-SYSTEM-EXT-CAPABILITY", ciscoSysExtCapability=ciscoSysExtCapability, PYSNMP_MODULE_ID=ciscoSysExtCapability, ciscoSysExtCapabilityMDS3R0=ciscoSysExtCapabilityMDS3R0, ciscoSysExtCapabilityGssV02R00=ciscoSysExtCapabilityGssV02R00)
