#
# PySNMP MIB module CISCO-VOICE-CAS-MODULE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VOICE-CAS-MODULE-CAPABILITY
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
ciscoVoiceCasModuleCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 401))
ciscoVoiceCasModuleCapability.setRevisions(('2004-03-29 00:00',))
if mibBuilder.loadTexts: ciscoVoiceCasModuleCapability.setLastUpdated('200403290000Z')
if mibBuilder.loadTexts: ciscoVoiceCasModuleCapability.setOrganization('Cisco Systems, Inc.')
cvcmCapabilityV321 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 401, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvcmCapabilityV321 = cvcmCapabilityV321.setProductRelease('Cisco VISM Release 3.2.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cvcmCapabilityV321 = cvcmCapabilityV321.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOICE-CAS-MODULE-CAPABILITY", ciscoVoiceCasModuleCapability=ciscoVoiceCasModuleCapability, PYSNMP_MODULE_ID=ciscoVoiceCasModuleCapability, cvcmCapabilityV321=cvcmCapabilityV321)
