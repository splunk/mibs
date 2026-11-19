#
# PySNMP MIB module CISCO-VOICE-AALX-PROFILE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VOICE-AALX-PROFILE-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Gauge32, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, Bits, iso, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "Bits", "iso", "Unsigned32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoVoiceAalxProfileCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 352))
ciscoVoiceAalxProfileCapability.setRevisions(('2004-02-07 00:00',))
if mibBuilder.loadTexts: ciscoVoiceAalxProfileCapability.setLastUpdated('200402070000Z')
if mibBuilder.loadTexts: ciscoVoiceAalxProfileCapability.setOrganization('Cisco Systems, Inc.')
cVoiceAalxProfileCapV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 352, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVoiceAalxProfileCapV5R00 = cVoiceAalxProfileCapV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVoiceAalxProfileCapV5R00 = cVoiceAalxProfileCapV5R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-AALX-PROFILE-CAPABILITY", cVoiceAalxProfileCapV5R00=cVoiceAalxProfileCapV5R00, PYSNMP_MODULE_ID=ciscoVoiceAalxProfileCapability, ciscoVoiceAalxProfileCapability=ciscoVoiceAalxProfileCapability)
