#
# PySNMP MIB module CISCO-ATM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ATM-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoAtmCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 9999))
ciscoAtmCapability.setRevisions(('2002-06-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAtmCapability.setRevisionsDescriptions(('Initial Version of the MIB module.',))
if mibBuilder.loadTexts: ciscoAtmCapability.setLastUpdated('200206120000Z')
if mibBuilder.loadTexts: ciscoAtmCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAtmCapability.setContactInfo('       Cisco Systems\n                        Customer Service\n\n                Postal: 170 W Tasman Drive\n                        San Jose, CA  95134\n                        USA\n\n                        Tel: +1 800 553-NETS\n\n                E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoAtmCapability.setDescription('The Agent Capabilities for ATM-MIB.')
ciscoAtmCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmCapabilityV2R00 = ciscoAtmCapabilityV2R00.setProductRelease('MGX8850 Release 2.00,\n                BPX SES Release 1.00.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmCapabilityV2R00 = ciscoAtmCapabilityV2R00.setStatus('current')
if mibBuilder.loadTexts: ciscoAtmCapabilityV2R00.setDescription('ATM MIB Capabilities')
mibBuilder.exportSymbols("CISCO-ATM-CAPABILITY", ciscoAtmCapabilityV2R00=ciscoAtmCapabilityV2R00, PYSNMP_MODULE_ID=ciscoAtmCapability, ciscoAtmCapability=ciscoAtmCapability)
