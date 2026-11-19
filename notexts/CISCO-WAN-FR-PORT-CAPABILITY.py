#
# PySNMP MIB module CISCO-WAN-FR-PORT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-WAN-FR-PORT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:23 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
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
