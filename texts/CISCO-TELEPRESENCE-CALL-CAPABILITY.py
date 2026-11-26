#
# PySNMP MIB module CISCO-TELEPRESENCE-CALL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-TELEPRESENCE-CALL-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:45 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoTelepresenceCallCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 577))
ciscoTelepresenceCallCapability.setRevisions(('2011-02-02 00:00', '2008-11-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoTelepresenceCallCapability.setRevisionsDescriptions(('Added capability for Cisco Telepresence System (CTS) 1.7.0.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoTelepresenceCallCapability.setLastUpdated('201102020000Z')
if mibBuilder.loadTexts: ciscoTelepresenceCallCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoTelepresenceCallCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: tsbu-snmp-dev@cisco.com')
if mibBuilder.loadTexts: ciscoTelepresenceCallCapability.setDescription('Agent capabilities for CISCO-TELEPRESENCE-CALL-MIB')
ciscoTelepresenceCallCapabilityCTSV150 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 577, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCallCapabilityCTSV150 = ciscoTelepresenceCallCapabilityCTSV150.setProductRelease('Cisco TelePresence System (CTS) 1.5.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCallCapabilityCTSV150 = ciscoTelepresenceCallCapabilityCTSV150.setStatus('current')
if mibBuilder.loadTexts: ciscoTelepresenceCallCapabilityCTSV150.setDescription('TELEPRESENCE CALL MIB capabilities')
ciscoTelepresenceCallCapabilityCTSV170 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 577, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCallCapabilityCTSV170 = ciscoTelepresenceCallCapabilityCTSV170.setProductRelease('Cisco TelePresence System (CTS) 1.7.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCallCapabilityCTSV170 = ciscoTelepresenceCallCapabilityCTSV170.setStatus('current')
if mibBuilder.loadTexts: ciscoTelepresenceCallCapabilityCTSV170.setDescription('TELEPRESENCE CALL MIB capabilities')
mibBuilder.exportSymbols("CISCO-TELEPRESENCE-CALL-CAPABILITY", ciscoTelepresenceCallCapabilityCTSV170=ciscoTelepresenceCallCapabilityCTSV170, PYSNMP_MODULE_ID=ciscoTelepresenceCallCapability, ciscoTelepresenceCallCapabilityCTSV150=ciscoTelepresenceCallCapabilityCTSV150, ciscoTelepresenceCallCapability=ciscoTelepresenceCallCapability)
