#
# PySNMP MIB module CISCO-TELEPRESENCE-CALL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-TELEPRESENCE-CALL-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoTelepresenceCallCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 577))
ciscoTelepresenceCallCapability.setRevisions(('2011-02-02 00:00', '2008-11-30 00:00',))
if mibBuilder.loadTexts: ciscoTelepresenceCallCapability.setLastUpdated('201102020000Z')
if mibBuilder.loadTexts: ciscoTelepresenceCallCapability.setOrganization('Cisco Systems, Inc.')
ciscoTelepresenceCallCapabilityCTSV150 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 577, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCallCapabilityCTSV150 = ciscoTelepresenceCallCapabilityCTSV150.setProductRelease('Cisco TelePresence System (CTS) 1.5.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCallCapabilityCTSV150 = ciscoTelepresenceCallCapabilityCTSV150.setStatus('current')
ciscoTelepresenceCallCapabilityCTSV170 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 577, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCallCapabilityCTSV170 = ciscoTelepresenceCallCapabilityCTSV170.setProductRelease('Cisco TelePresence System (CTS) 1.7.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCallCapabilityCTSV170 = ciscoTelepresenceCallCapabilityCTSV170.setStatus('current')
mibBuilder.exportSymbols("CISCO-TELEPRESENCE-CALL-CAPABILITY", ciscoTelepresenceCallCapability=ciscoTelepresenceCallCapability, ciscoTelepresenceCallCapabilityCTSV150=ciscoTelepresenceCallCapabilityCTSV150, ciscoTelepresenceCallCapabilityCTSV170=ciscoTelepresenceCallCapabilityCTSV170, PYSNMP_MODULE_ID=ciscoTelepresenceCallCapability)
