#
# PySNMP MIB module CISCO-WAN-VISM-T38-FAX-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-WAN-VISM-T38-FAX-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:44 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "iso", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cwVismT38FaxCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 335))
cwVismT38FaxCapability.setRevisions(('2001-08-05 00:00', '2002-06-01 00:00',))
if mibBuilder.loadTexts: cwVismT38FaxCapability.setLastUpdated('200206010000Z')
if mibBuilder.loadTexts: cwVismT38FaxCapability.setOrganization('Cisco Systems, Inc.')
cwVismT38FaxCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 335, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwVismT38FaxCapabilityV2R00 = cwVismT38FaxCapabilityV2R00.setProductRelease('VISM Release3.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwVismT38FaxCapabilityV2R00 = cwVismT38FaxCapabilityV2R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-VISM-T38-FAX-CAPABILITY", PYSNMP_MODULE_ID=cwVismT38FaxCapability, cwVismT38FaxCapabilityV2R00=cwVismT38FaxCapabilityV2R00, cwVismT38FaxCapability=cwVismT38FaxCapability)
