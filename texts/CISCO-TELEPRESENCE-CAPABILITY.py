#
# PySNMP MIB module CISCO-TELEPRESENCE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-TELEPRESENCE-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
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
ciscoTelepresenceCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 565))
ciscoTelepresenceCapability.setRevisions(('2008-06-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoTelepresenceCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoTelepresenceCapability.setLastUpdated('200806050000Z')
if mibBuilder.loadTexts: ciscoTelepresenceCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoTelepresenceCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: tb-sw@cisco.com')
if mibBuilder.loadTexts: ciscoTelepresenceCapability.setDescription('Agent capabilities for CISCO-TELEPRESENCE-MIB')
ciscoTelepresenceCapabilityCTSV120 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 565, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCapabilityCTSV120 = ciscoTelepresenceCapabilityCTSV120.setProductRelease('Cisco TelePresence System (CTS) 1.4.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCapabilityCTSV120 = ciscoTelepresenceCapabilityCTSV120.setStatus('current')
if mibBuilder.loadTexts: ciscoTelepresenceCapabilityCTSV120.setDescription('TELEPRESENCE MIB capabilities')
mibBuilder.exportSymbols("CISCO-TELEPRESENCE-CAPABILITY", PYSNMP_MODULE_ID=ciscoTelepresenceCapability, ciscoTelepresenceCapabilityCTSV120=ciscoTelepresenceCapabilityCTSV120, ciscoTelepresenceCapability=ciscoTelepresenceCapability)
