#
# PySNMP MIB module CISCO-VOIP-TAP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VOIP-TAP-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:01 2026
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
ciscoVoipTapCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 593))
ciscoVoipTapCapability.setRevisions(('2010-08-24 00:00',))
if mibBuilder.loadTexts: ciscoVoipTapCapability.setLastUpdated('201008240000Z')
if mibBuilder.loadTexts: ciscoVoipTapCapability.setOrganization('Cisco Systems, Inc.')
ciscoVoipTapCapV15R01SXE31ASR1K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 593, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoipTapCapV15R01SXE31ASR1K = ciscoVoipTapCapV15R01SXE31ASR1K.setProductRelease('Cisco IOS XE 15.0(01)SXE31 on ASR 1000 \n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoipTapCapV15R01SXE31ASR1K = ciscoVoipTapCapV15R01SXE31ASR1K.setStatus('current')
mibBuilder.exportSymbols("CISCO-VOIP-TAP-CAPABILITY", ciscoVoipTapCapV15R01SXE31ASR1K=ciscoVoipTapCapV15R01SXE31ASR1K, ciscoVoipTapCapability=ciscoVoipTapCapability, PYSNMP_MODULE_ID=ciscoVoipTapCapability)
