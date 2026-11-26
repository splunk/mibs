#
# PySNMP MIB module CISCO-VISM-DSX1-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-VISM-DSX1-CAPABILITY
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
ciscoVismDsx1Capability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 450))
ciscoVismDsx1Capability.setRevisions(('2005-09-26 00:00',))
if mibBuilder.loadTexts: ciscoVismDsx1Capability.setLastUpdated('200509260000Z')
if mibBuilder.loadTexts: ciscoVismDsx1Capability.setOrganization('Cisco Systems, Inc.')
cVismDsx1CapabilityV3325 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 450, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVismDsx1CapabilityV3325 = cVismDsx1CapabilityV3325.setProductRelease('Cisco VISM Release 3.3.25')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cVismDsx1CapabilityV3325 = cVismDsx1CapabilityV3325.setStatus('current')
mibBuilder.exportSymbols("CISCO-VISM-DSX1-CAPABILITY", ciscoVismDsx1Capability=ciscoVismDsx1Capability, cVismDsx1CapabilityV3325=cVismDsx1CapabilityV3325, PYSNMP_MODULE_ID=ciscoVismDsx1Capability)
