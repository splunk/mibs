#
# PySNMP MIB module CISCO-VOICE-DIAL-CONTROL-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VOICE-DIAL-CONTROL-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:44 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "iso", "Counter64", "Counter32")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoVoiceDialControlCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 83))
ciscoVoiceDialControlCapability.setRevisions(('2009-03-31 00:00', '2006-11-16 00:00', '2005-07-25 00:00', '1999-07-12 00:00', '1998-01-09 00:00', '1997-06-15 00:00',))
if mibBuilder.loadTexts: ciscoVoiceDialControlCapability.setLastUpdated('200903310000Z')
if mibBuilder.loadTexts: ciscoVoiceDialControlCapability.setOrganization('Cisco Systems, Inc.')
ciscoVoiceDialControlCapabilityV11R03 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 83, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapabilityV11R03 = ciscoVoiceDialControlCapabilityV11R03.setProductRelease('Cisco IOS 11.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapabilityV11R03 = ciscoVoiceDialControlCapabilityV11R03.setStatus('obsolete')
ciscoVoiceDialControlCapabilityV11R03Rev1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 83, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapabilityV11R03Rev1 = ciscoVoiceDialControlCapabilityV11R03Rev1.setProductRelease('Cisco IOS 11.3')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapabilityV11R03Rev1 = ciscoVoiceDialControlCapabilityV11R03Rev1.setStatus('current')
ciscoVoiceDialControlCapabilityV12R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 83, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapabilityV12R00 = ciscoVoiceDialControlCapabilityV12R00.setProductRelease('Cisco IOS 12.0(5)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapabilityV12R00 = ciscoVoiceDialControlCapabilityV12R00.setStatus('obsolete')
ciscoVoiceDialControlCapabilityV12R00Rev1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 83, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapabilityV12R00Rev1 = ciscoVoiceDialControlCapabilityV12R00Rev1.setProductRelease('Cisco IOS 12.0(5)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapabilityV12R00Rev1 = ciscoVoiceDialControlCapabilityV12R00Rev1.setStatus('current')
ciscoVoiceDialControlCapabilityV124R03T5400 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 83, 5))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapabilityV124R03T5400 = ciscoVoiceDialControlCapabilityV124R03T5400.setProductRelease('Cisco IOS 12.4(3)T on AS5400')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapabilityV124R03T5400 = ciscoVoiceDialControlCapabilityV124R03T5400.setStatus('current')
ciscoVoiceDialControlCapV12R04 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 83, 6))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapV12R04 = ciscoVoiceDialControlCapV12R04.setProductRelease('Cisco IOS 12.4 for all platforms except IAD2420')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapV12R04 = ciscoVoiceDialControlCapV12R04.setStatus('current')
ciscoVoiceDialControlCapV12R04Rev1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 83, 7))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapV12R04Rev1 = ciscoVoiceDialControlCapV12R04Rev1.setProductRelease('Cisco IOS 12.4T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoiceDialControlCapV12R04Rev1 = ciscoVoiceDialControlCapV12R04Rev1.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-DIAL-CONTROL-CAPABILITY", PYSNMP_MODULE_ID=ciscoVoiceDialControlCapability, ciscoVoiceDialControlCapabilityV11R03=ciscoVoiceDialControlCapabilityV11R03, ciscoVoiceDialControlCapV12R04=ciscoVoiceDialControlCapV12R04, ciscoVoiceDialControlCapability=ciscoVoiceDialControlCapability, ciscoVoiceDialControlCapabilityV124R03T5400=ciscoVoiceDialControlCapabilityV124R03T5400, ciscoVoiceDialControlCapabilityV11R03Rev1=ciscoVoiceDialControlCapabilityV11R03Rev1, ciscoVoiceDialControlCapV12R04Rev1=ciscoVoiceDialControlCapV12R04Rev1, ciscoVoiceDialControlCapabilityV12R00=ciscoVoiceDialControlCapabilityV12R00, ciscoVoiceDialControlCapabilityV12R00Rev1=ciscoVoiceDialControlCapabilityV12R00Rev1)
