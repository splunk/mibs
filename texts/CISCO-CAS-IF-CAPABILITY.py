#
# PySNMP MIB module CISCO-CAS-IF-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-CAS-IF-CAPABILITY
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
ciscoCasIfCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 122))
ciscoCasIfCapability.setRevisions(('2009-12-04 00:00', '2004-08-10 00:00', '2003-12-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCasIfCapability.setRevisionsDescriptions(('Added capability statement ciscoCasIfCapabilityV12R04TPC3xxx.', 'Added ciscoCasIfCapabilityV5R015 for \n         MGX8850 release 5.0.15.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoCasIfCapability.setLastUpdated('200912040000Z')
if mibBuilder.loadTexts: ciscoCasIfCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCasIfCapability.setContactInfo('        Cisco Systems\n                 Customer Service\n        Postal: 170 W Tasman Drive\n                San Jose, CA 95134\n                USA\n           Tel: +1 800 553-NETS\n        E-mail: cs-voice-gateway@cisco.com')
if mibBuilder.loadTexts: ciscoCasIfCapability.setDescription('The agent capabilities for CISCO-CAS-IF-MIB.')
ciscoCasIfCapabilityV5R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 122, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCasIfCapabilityV5R000 = ciscoCasIfCapabilityV5R000.setProductRelease('MGX8850 Release 5.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCasIfCapabilityV5R000 = ciscoCasIfCapabilityV5R000.setStatus('current')
if mibBuilder.loadTexts: ciscoCasIfCapabilityV5R000.setDescription('CISCO-CAS-IF-MIB Capabilities for Voice \n                         Switch Service Module(VXSM) in \n                         Release 5.0.0.')
ciscoCasIfCapabilityV5R015 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 122, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCasIfCapabilityV5R015 = ciscoCasIfCapabilityV5R015.setProductRelease('MGX8850 Release 5.0.15')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCasIfCapabilityV5R015 = ciscoCasIfCapabilityV5R015.setStatus('current')
if mibBuilder.loadTexts: ciscoCasIfCapabilityV5R015.setDescription('CISCO-CAS-IF-MIB Capabilities for Voice \n                         Switch Service Module(VXSM) in \n                         Release 5.0.15.')
ciscoCasIfCapabilityV12R04TPC3xxx = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 122, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCasIfCapabilityV12R04TPC3xxx = ciscoCasIfCapabilityV12R04TPC3xxx.setProductRelease('CISCO IOS 12.4T for Integrate Service\n                     Router (ISR) c2xxx and c3xxx platforms.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCasIfCapabilityV12R04TPC3xxx = ciscoCasIfCapabilityV12R04TPC3xxx.setStatus('current')
if mibBuilder.loadTexts: ciscoCasIfCapabilityV12R04TPC3xxx.setDescription('CISCO-CAS-IF-MIB Capabilities')
mibBuilder.exportSymbols("CISCO-CAS-IF-CAPABILITY", ciscoCasIfCapabilityV5R015=ciscoCasIfCapabilityV5R015, PYSNMP_MODULE_ID=ciscoCasIfCapability, ciscoCasIfCapabilityV5R000=ciscoCasIfCapabilityV5R000, ciscoCasIfCapability=ciscoCasIfCapability, ciscoCasIfCapabilityV12R04TPC3xxx=ciscoCasIfCapabilityV12R04TPC3xxx)
