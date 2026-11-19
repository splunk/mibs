#
# PySNMP MIB module CISCO-VOICE-TONE-CADENCE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VOICE-TONE-CADENCE-CAPABILITY
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
ciscoVoiceToneCadenceCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 387))
ciscoVoiceToneCadenceCapability.setRevisions(('2004-02-02 00:00',))
if mibBuilder.loadTexts: ciscoVoiceToneCadenceCapability.setLastUpdated('200402020000Z')
if mibBuilder.loadTexts: ciscoVoiceToneCadenceCapability.setOrganization('Cisco Systems, Inc.')
cVoiceToneCadenceCapV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 387, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVoiceToneCadenceCapV5R00 = cVoiceToneCadenceCapV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVoiceToneCadenceCapV5R00 = cVoiceToneCadenceCapV5R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-TONE-CADENCE-CAPABILITY", cVoiceToneCadenceCapV5R00=cVoiceToneCadenceCapV5R00, PYSNMP_MODULE_ID=ciscoVoiceToneCadenceCapability, ciscoVoiceToneCadenceCapability=ciscoVoiceToneCadenceCapability)
