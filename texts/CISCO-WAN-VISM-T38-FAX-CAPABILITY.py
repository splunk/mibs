#
# PySNMP MIB module CISCO-WAN-VISM-T38-FAX-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-WAN-VISM-T38-FAX-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:14 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cwVismT38FaxCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 335))
cwVismT38FaxCapability.setRevisions(('2001-08-05 00:00', '2002-06-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cwVismT38FaxCapability.setRevisionsDescriptions(('Initial version of this MIB module', '\n                t38FaxInfoFieldSize variation was modified.\n                t38HsDataPacketSize variation was added.\n                t38LsDataRedundancy variation was modified.\n                t38HsDataRedundancy variation was modified.\n                t38ErrCorrection variation was added.\n                t38NSFCountryCode variation was modified.\n                t38NSFVendorCode variation was added.\n                t38Redundancy variation was added.\n                ',))
if mibBuilder.loadTexts: cwVismT38FaxCapability.setLastUpdated('200206010000Z')
if mibBuilder.loadTexts: cwVismT38FaxCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cwVismT38FaxCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-vism@cisco.com')
if mibBuilder.loadTexts: cwVismT38FaxCapability.setDescription('The Agent Capabilities for CISCO-WAN-T38-FAXRELAY-MIB.')
cwVismT38FaxCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 335, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwVismT38FaxCapabilityV2R00 = cwVismT38FaxCapabilityV2R00.setProductRelease('VISM Release3.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwVismT38FaxCapabilityV2R00 = cwVismT38FaxCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: cwVismT38FaxCapabilityV2R00.setDescription('CISCO-WAN-T38-FAXRELAY-MIB Capabilities')
mibBuilder.exportSymbols("CISCO-WAN-VISM-T38-FAX-CAPABILITY", cwVismT38FaxCapability=cwVismT38FaxCapability, PYSNMP_MODULE_ID=cwVismT38FaxCapability, cwVismT38FaxCapabilityV2R00=cwVismT38FaxCapabilityV2R00)
