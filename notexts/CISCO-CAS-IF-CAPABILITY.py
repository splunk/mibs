#
# PySNMP MIB module CISCO-CAS-IF-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-CAS-IF-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCasIfCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 122))
ciscoCasIfCapability.setRevisions(('2009-12-04 00:00', '2004-08-10 00:00', '2003-12-03 00:00',))
if mibBuilder.loadTexts: ciscoCasIfCapability.setLastUpdated('200912040000Z')
if mibBuilder.loadTexts: ciscoCasIfCapability.setOrganization('Cisco Systems, Inc.')
ciscoCasIfCapabilityV5R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 122, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCasIfCapabilityV5R000 = ciscoCasIfCapabilityV5R000.setProductRelease('MGX8850 Release 5.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCasIfCapabilityV5R000 = ciscoCasIfCapabilityV5R000.setStatus('current')
ciscoCasIfCapabilityV5R015 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 122, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCasIfCapabilityV5R015 = ciscoCasIfCapabilityV5R015.setProductRelease('MGX8850 Release 5.0.15')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCasIfCapabilityV5R015 = ciscoCasIfCapabilityV5R015.setStatus('current')
ciscoCasIfCapabilityV12R04TPC3xxx = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 122, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCasIfCapabilityV12R04TPC3xxx = ciscoCasIfCapabilityV12R04TPC3xxx.setProductRelease('CISCO IOS 12.4T for Integrate Service\n                     Router (ISR) c2xxx and c3xxx platforms.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCasIfCapabilityV12R04TPC3xxx = ciscoCasIfCapabilityV12R04TPC3xxx.setStatus('current')
mibBuilder.exportSymbols("CISCO-CAS-IF-CAPABILITY", PYSNMP_MODULE_ID=ciscoCasIfCapability, ciscoCasIfCapabilityV5R000=ciscoCasIfCapabilityV5R000, ciscoCasIfCapabilityV12R04TPC3xxx=ciscoCasIfCapabilityV12R04TPC3xxx, ciscoCasIfCapabilityV5R015=ciscoCasIfCapabilityV5R015, ciscoCasIfCapability=ciscoCasIfCapability)
