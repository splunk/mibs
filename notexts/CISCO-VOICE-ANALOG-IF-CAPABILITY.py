#
# PySNMP MIB module CISCO-VOICE-ANALOG-IF-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VOICE-ANALOG-IF-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:24 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVoiceAnalogIfCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 82))
ciscoVoiceAnalogIfCapability.setRevisions(('2003-04-28 00:00', '1997-06-15 00:00',))
if mibBuilder.loadTexts: ciscoVoiceAnalogIfCapability.setLastUpdated('200304280000Z')
if mibBuilder.loadTexts: ciscoVoiceAnalogIfCapability.setOrganization('Cisco Systems, Inc.')
ciscoVoiceAnalogIfCapabilityV11R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 82, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceAnalogIfCapabilityV11R03 = ciscoVoiceAnalogIfCapabilityV11R03.setProductRelease('Cisco IOS 11.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceAnalogIfCapabilityV11R03 = ciscoVoiceAnalogIfCapabilityV11R03.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-ANALOG-IF-CAPABILITY", PYSNMP_MODULE_ID=ciscoVoiceAnalogIfCapability, ciscoVoiceAnalogIfCapability=ciscoVoiceAnalogIfCapability, ciscoVoiceAnalogIfCapabilityV11R03=ciscoVoiceAnalogIfCapabilityV11R03)
