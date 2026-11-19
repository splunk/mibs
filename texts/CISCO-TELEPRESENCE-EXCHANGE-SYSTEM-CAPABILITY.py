#
# PySNMP MIB module CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:14 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoTelepresenceExchangeSystemCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 615))
ciscoTelepresenceExchangeSystemCapability.setRevisions(('2013-04-11 00:00', '2012-08-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoTelepresenceExchangeSystemCapability.setRevisionsDescriptions(('Added ciscoTelepresenceCapabilityCTXV130 capabilities for\n        CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoTelepresenceExchangeSystemCapability.setLastUpdated('201304150000Z')
if mibBuilder.loadTexts: ciscoTelepresenceExchangeSystemCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoTelepresenceExchangeSystemCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-txbu-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoTelepresenceExchangeSystemCapability.setDescription('Agent capabilities for CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-MIB')
ciscoTelepresenceCapabilityCTXV120 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 615, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCapabilityCTXV120 = ciscoTelepresenceCapabilityCTXV120.setProductRelease('OS=TELEPRESENCE EXCHANGE SYSTEM\n                     OSVERSION=1.2.0\n                     PLATFORM=TelePresence (TP)\n                     INTERFACE=None')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCapabilityCTXV120 = ciscoTelepresenceCapabilityCTXV120.setStatus('current')
if mibBuilder.loadTexts: ciscoTelepresenceCapabilityCTXV120.setDescription('TELEPRESENCE EXCHANGE SYSTEM MIB Capabilities')
ciscoTelepresenceCapabilityCTXV130 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 615, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCapabilityCTXV130 = ciscoTelepresenceCapabilityCTXV130.setProductRelease('OS=TELEPRESENCE EXCHANGE SYSTEM\n                     OSVERSION=1.3.0\n                     PLATFORM=TelePresence (TP)\n                     INTERFACE=None')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCapabilityCTXV130 = ciscoTelepresenceCapabilityCTXV130.setStatus('current')
if mibBuilder.loadTexts: ciscoTelepresenceCapabilityCTXV130.setDescription('TELEPRESENCE EXCHANGE SYSTEM MIB Capabilities')
mibBuilder.exportSymbols("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-CAPABILITY", ciscoTelepresenceExchangeSystemCapability=ciscoTelepresenceExchangeSystemCapability, ciscoTelepresenceCapabilityCTXV120=ciscoTelepresenceCapabilityCTXV120, ciscoTelepresenceCapabilityCTXV130=ciscoTelepresenceCapabilityCTXV130, PYSNMP_MODULE_ID=ciscoTelepresenceExchangeSystemCapability)
