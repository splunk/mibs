#
# PySNMP MIB module CISCO-WAN-FR-CONN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-WAN-FR-CONN-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:01 2026
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
ciscoWanFrConnCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 358))
ciscoWanFrConnCapability.setRevisions(('2002-03-27 00:00',))
if mibBuilder.loadTexts: ciscoWanFrConnCapability.setLastUpdated('200203270000Z')
if mibBuilder.loadTexts: ciscoWanFrConnCapability.setOrganization('Cisco Systems, Inc.')
cwFrConnCapabilityFrsm12V3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 358, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwFrConnCapabilityFrsm12V3R00 = cwFrConnCapabilityFrsm12V3R00.setProductRelease('MGX8850 Release 3.0.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwFrConnCapabilityFrsm12V3R00 = cwFrConnCapabilityFrsm12V3R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-FR-CONN-CAPABILITY", cwFrConnCapabilityFrsm12V3R00=cwFrConnCapabilityFrsm12V3R00, ciscoWanFrConnCapability=ciscoWanFrConnCapability, PYSNMP_MODULE_ID=ciscoWanFrConnCapability)
