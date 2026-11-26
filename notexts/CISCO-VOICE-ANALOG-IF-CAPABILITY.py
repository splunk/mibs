#
# PySNMP MIB module CISCO-VOICE-ANALOG-IF-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VOICE-ANALOG-IF-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
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
ciscoVoiceAnalogIfCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 82))
ciscoVoiceAnalogIfCapability.setRevisions(('2003-04-28 00:00', '1997-06-15 00:00',))
if mibBuilder.loadTexts: ciscoVoiceAnalogIfCapability.setLastUpdated('200304280000Z')
if mibBuilder.loadTexts: ciscoVoiceAnalogIfCapability.setOrganization('Cisco Systems, Inc.')
ciscoVoiceAnalogIfCapabilityV11R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 82, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceAnalogIfCapabilityV11R03 = ciscoVoiceAnalogIfCapabilityV11R03.setProductRelease('Cisco IOS 11.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceAnalogIfCapabilityV11R03 = ciscoVoiceAnalogIfCapabilityV11R03.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-ANALOG-IF-CAPABILITY", PYSNMP_MODULE_ID=ciscoVoiceAnalogIfCapability, ciscoVoiceAnalogIfCapabilityV11R03=ciscoVoiceAnalogIfCapabilityV11R03, ciscoVoiceAnalogIfCapability=ciscoVoiceAnalogIfCapability)
