#
# PySNMP MIB module CISCO-WAN-FR-PORT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-WAN-FR-PORT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWanFrPortCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 359))
ciscoWanFrPortCapability.setRevisions(('2002-03-27 00:00',))
if mibBuilder.loadTexts: ciscoWanFrPortCapability.setLastUpdated('200203270000Z')
if mibBuilder.loadTexts: ciscoWanFrPortCapability.setOrganization('Cisco Systems, Inc.')
cwFrPortCapabilityFrsm12V3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 359, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwFrPortCapabilityFrsm12V3R00 = cwFrPortCapabilityFrsm12V3R00.setProductRelease('MGX8850 Release 3.0.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwFrPortCapabilityFrsm12V3R00 = cwFrPortCapabilityFrsm12V3R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-FR-PORT-CAPABILITY", ciscoWanFrPortCapability=ciscoWanFrPortCapability, PYSNMP_MODULE_ID=ciscoWanFrPortCapability, cwFrPortCapabilityFrsm12V3R00=cwFrPortCapabilityFrsm12V3R00)
