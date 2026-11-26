#
# PySNMP MIB module CISCO-VOIP-TAP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VOIP-TAP-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:46 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoVoipTapCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 593))
ciscoVoipTapCapability.setRevisions(('2010-08-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVoipTapCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVoipTapCapability.setLastUpdated('201008240000Z')
if mibBuilder.loadTexts: ciscoVoipTapCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVoipTapCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-li@cisco.com')
if mibBuilder.loadTexts: ciscoVoipTapCapability.setDescription('The capabilities description of CISCO-VOIP-TAP-MIB.')
ciscoVoipTapCapV15R01SXE31ASR1K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 593, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoipTapCapV15R01SXE31ASR1K = ciscoVoipTapCapV15R01SXE31ASR1K.setProductRelease('Cisco IOS XE 15.0(01)SXE31 on ASR 1000 \n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoipTapCapV15R01SXE31ASR1K = ciscoVoipTapCapV15R01SXE31ASR1K.setStatus('current')
if mibBuilder.loadTexts: ciscoVoipTapCapV15R01SXE31ASR1K.setDescription('CISCO-VOIP-TAP-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-VOIP-TAP-CAPABILITY", PYSNMP_MODULE_ID=ciscoVoipTapCapability, ciscoVoipTapCapability=ciscoVoipTapCapability, ciscoVoipTapCapV15R01SXE31ASR1K=ciscoVoipTapCapV15R01SXE31ASR1K)
