#
# PySNMP MIB module CISCO-VOICE-AALX-PROFILE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VOICE-AALX-PROFILE-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
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
ciscoVoiceAalxProfileCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 352))
ciscoVoiceAalxProfileCapability.setRevisions(('2004-02-07 00:00',))
if mibBuilder.loadTexts: ciscoVoiceAalxProfileCapability.setLastUpdated('200402070000Z')
if mibBuilder.loadTexts: ciscoVoiceAalxProfileCapability.setOrganization('Cisco Systems, Inc.')
cVoiceAalxProfileCapV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 352, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVoiceAalxProfileCapV5R00 = cVoiceAalxProfileCapV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVoiceAalxProfileCapV5R00 = cVoiceAalxProfileCapV5R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-AALX-PROFILE-CAPABILITY", cVoiceAalxProfileCapV5R00=cVoiceAalxProfileCapV5R00, ciscoVoiceAalxProfileCapability=ciscoVoiceAalxProfileCapability, PYSNMP_MODULE_ID=ciscoVoiceAalxProfileCapability)
