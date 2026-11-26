#
# PySNMP MIB module CISCO-VOICE-TONE-CADENCE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VOICE-TONE-CADENCE-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
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
ciscoVoiceToneCadenceCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 387))
ciscoVoiceToneCadenceCapability.setRevisions(('2004-02-02 00:00',))
if mibBuilder.loadTexts: ciscoVoiceToneCadenceCapability.setLastUpdated('200402020000Z')
if mibBuilder.loadTexts: ciscoVoiceToneCadenceCapability.setOrganization('Cisco Systems, Inc.')
cVoiceToneCadenceCapV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 387, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVoiceToneCadenceCapV5R00 = cVoiceToneCadenceCapV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVoiceToneCadenceCapV5R00 = cVoiceToneCadenceCapV5R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-TONE-CADENCE-CAPABILITY", ciscoVoiceToneCadenceCapability=ciscoVoiceToneCadenceCapability, PYSNMP_MODULE_ID=ciscoVoiceToneCadenceCapability, cVoiceToneCadenceCapV5R00=cVoiceToneCadenceCapV5R00)
