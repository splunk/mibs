#
# PySNMP MIB module CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoTelepresenceExchangeSystemCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 615))
ciscoTelepresenceExchangeSystemCapability.setRevisions(('2013-04-11 00:00', '2012-08-17 00:00',))
if mibBuilder.loadTexts: ciscoTelepresenceExchangeSystemCapability.setLastUpdated('201304150000Z')
if mibBuilder.loadTexts: ciscoTelepresenceExchangeSystemCapability.setOrganization('Cisco Systems, Inc.')
ciscoTelepresenceCapabilityCTXV120 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 615, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCapabilityCTXV120 = ciscoTelepresenceCapabilityCTXV120.setProductRelease('OS=TELEPRESENCE EXCHANGE SYSTEM\n                     OSVERSION=1.2.0\n                     PLATFORM=TelePresence (TP)\n                     INTERFACE=None')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCapabilityCTXV120 = ciscoTelepresenceCapabilityCTXV120.setStatus('current')
ciscoTelepresenceCapabilityCTXV130 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 615, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCapabilityCTXV130 = ciscoTelepresenceCapabilityCTXV130.setProductRelease('OS=TELEPRESENCE EXCHANGE SYSTEM\n                     OSVERSION=1.3.0\n                     PLATFORM=TelePresence (TP)\n                     INTERFACE=None')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTelepresenceCapabilityCTXV130 = ciscoTelepresenceCapabilityCTXV130.setStatus('current')
mibBuilder.exportSymbols("CISCO-TELEPRESENCE-EXCHANGE-SYSTEM-CAPABILITY", PYSNMP_MODULE_ID=ciscoTelepresenceExchangeSystemCapability, ciscoTelepresenceExchangeSystemCapability=ciscoTelepresenceExchangeSystemCapability, ciscoTelepresenceCapabilityCTXV120=ciscoTelepresenceCapabilityCTXV120, ciscoTelepresenceCapabilityCTXV130=ciscoTelepresenceCapabilityCTXV130)
